![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)![AmazonDynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white)

# Running AWS DynamoDB Local with Docker-Compose

> Adapted from: https://medium.com/platform-engineer/running-aws-dynamodb-local-with-docker-compose-6f75850aba1e

DynamoDB is a fully managed NoSQL database provided by AWS. Since it’s a pay-as-you-go cloud resource, developers may often need to opt-out from accessing AWS every time to keep their cloud bills at a minimum during the development and testing stages. However, you may still need to run and test the code that consumes DynamoDB features via stubs / mock interfaces / some cost-effective and convenient-to-setup solution locally. Also, the daily CI/CD pipelines may want to run some parts of automated test suites very frequently without relying on the AWS resources. These are some common developer pain points when using managed cloud services like DyanamoDB.

DynamoDB Local initiative by the official AWS DynamoDB Team address many development-related concerns by providing a self-contained version of DyanamoDB for local and offline use
In this quick tutorial, let’s learn how to,
1. — Setup DynamDB Local with Docker / Docker-Compose
2. — Connect programmatically with AWS-CLI / AWS-SDK
3. — View tables with DyanmoDB Admin Dashboard GUI
4. — Inspiration for testing with stubs

## 1 — Setup DynamoDB Local with Docker/Docker-Compose

### (1.1) Docker way

With the below command, you can pull dynamodb-local image from Docker Hub and run it locally on port 8000 in detached mode (-d).

```
docker run -d -p 8000:8000 --name my-dynamodb amazon/dynamodb-localdocker logs -f my-dynamodb
```

Please feel free to add other optional flags as per your preferences.

### (1.2) Docker-Compose way

You can do the same with Docker-Compose by adding the below record to your ```docker-compose.yaml``` file.

```
version: '3.7'
services:
  dynamodb:
    image:  amazon/dynamodb-local
    container_name: my-dynamodb
    hostname: dynamodb
    restart: always
    volumes:
      -  ./my-dynamodb-data:/home/dynamodblocal/data
    ports:
      - 8000:8000
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath /home/dynamodblocal/data/"
```

Here are the commands you can use for that:

```
mkdir -p my-dynamodb-data
vi docker-compose.yaml
docker-compose up -d dynamodbdocker logs -f my-dynamodb
```

## 2 — Connect to DynamoDB Local programmatically

After getting your local DyanamoDB instance successfully set up, now you should be able to see it running on http://localhost:8000 . We can pass this address to **AWS-CLI** (https://docs.aws.amazon.com/cli/latest/reference/dynamodb/) or **AWS-SDK** (https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html) as our preferred DynamoDB endpoint URL and start accessing it.

### (2.1) AWS-CLI Way

```
aws dynamodb <command> --endpoint-url http://localhost:8000e.g.
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

### (2.2) AWS-SDK Way

Here’re some sample code snippets to use with AWS-SDK in a few programming languages.

```
2.2.1 — Node.jsimport { DynamoDB, DocumentClient } from "aws-sdk"// via DynamoDB
const dbClient = new DynamoDB({
  endpoint: "http://localhost:8000",
  .....
})// via DocumentClient
const docClient = new DocumentClient({
  endpoint: "http://localhost:8000",
  .....
})2.2.2 — Golangimport (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/dynamodb"
)sess, err := session.NewSession(&aws.Config{     
    Endpoint: aws.String("http://localhost:8000")}, 
)
if err != nil {     
    // Handle Session creation error 
}
// Create DynamoDB client 
svc := dynamodb.New(sess)2.2.3 - Javaimport software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;DynamoDbClient client = DynamoDbClient.builder()
   .region(Region.US_WEST_2) 
   .endpointOverride(
        URI.create("http://localhost:8000")
   ).build();2.2.4 - Python (Boto3)import boto3# Get the service client
db = boto3.client('dynamodb',endpoint_url='http://localhost:8000')# Get the service resource
db = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')
```

## 3 — View DynamoDB Local tables with DyanmoDB Admin GUI

There’s plenty of Admin GUI tools for DynamoDB — both free and paid, with many advanced features (e.g. Dynobase, Retool). However, since we run this instance only for development and testing purposes, a simple and free tool like **dynamodb-admin** (https://www.npmjs.com/package/dynamodb-admin) will be fit for the purpose.

This tool comes as an NPM package, so just by installing it globally, you can start using it right away. Now when you do that, do not forget to set the environment variable — DYNAMO_ENDPOINT=http://localhost:8000.

```
npm install -g dynamodb-admin// For Windows
set DYNAMO_ENDPOINT=http://localhost:8000
dynamodb-admin// For Mac/Linux
DYNAMO_ENDPOINT=http://localhost:8000 dynamodb-admin
```

Now visit ```http://localhost:8001``` on your web browser to access the dynamodb-admin GUI.

## 4 — Inspiration for testing with stubs

When you update your code for consuming DynamoDB Local, you may need to write some logic to switch between different DynamoDB clients based on your environment settings. This might look hacky most of the times in your code. Therefore, a nice way to handle this use case is to stub the DynamoDB client creation logic using an appropriate test framework of your choice.

The following are some general steps with code examples in Sinon.js (a popular framework to create fakes, mocks, and stubs when writing tests in Node.js). Hope you’ll be able to replicate the same concepts in other technology stacks too.

### (a) First, wrap the actual DynamoDB client creation logic inside a function.

```
export namespace AWSServices {
   export function getDynamoDBClient(): DocumentClient {
     if (docClient == undefined) {
        docClient = new AWS.DynamoDB.DocumentClient({
           region:..., 
           apiVersion:...
        });
     }
     return docClient
   }
}
```

### (b) Now stub that function. Make sure you include DynamoDB’s endpoint — ```http://localhost:8000``` when passing configs for the DynamoDB client.

```
import * as sinon from 'sinon';const docClient = new AWS.DynamoDB.DocumentClient({
    region:...,
    apiVersion:...,
    endpoint: "http://localhost:8000"
});const dbStub = sinon.stub(
      AWSServices, "getDynamoDBClient"
    ).returns(docClient);
```

Also make sure you tear up the stub at the end of testing, in order to reset your code to consume AWS resources and services as usual.

```
before(async () => {
    await createTables();
})after(async () => {
    await deleteTables();    dbStub.restore();
})
```