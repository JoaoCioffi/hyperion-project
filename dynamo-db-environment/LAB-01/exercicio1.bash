#### -------------------------------------------------------------------------------
## se o link nao funcionar mais, eh so descarregar os zips exemplo1.zip e exemplo2.zip
aws s3 sync s3://jeaneth-exercicio-edb016 .

unzip exemplo1.zip

#### -------------------------------------------------------------------------------
aws dynamodb create-table \
    --table-name ProductCatalog \
    --attribute-definitions AttributeName=Id,AttributeType=N \
    --key-schema AttributeName=Id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=5


#### -------------------------------------------------------------------------------

aws dynamodb batch-write-item --request-items file://exemplo1/ProductCatalog.json


#### -------------------------------------------------------------------------------
aws dynamodb scan --table-name ProductCatalog


#### -------------------------------------------------------------------------------
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"101"}}'


aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"101"}}' \
    --projection-expression "ProductCategory, Price, Title" \
    --return-consumed-capacity TOTAL



aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id":{"N":"101"}}' \
    --consistent-read \
    --projection-expression "ProductCategory, Price, Title" \
    --return-consumed-capacity TOTAL


#### -------------------------------------------------------------------------------


aws dynamodb update-item \
    --table-name ProductCatalog \
    --key '{
        "Id" : {"N": "201"}
    }' \
    --update-expression "SET #Color = list_append(#Color, :values)" \
    --expression-attribute-names '{"#Color": "Color"}' \
    --expression-attribute-values '{
        ":values" : {"L": [{"S" : "Blue"}, {"S" : "Yellow"}]}
    }' \
    --return-consumed-capacity TOTAL

#### -------------------------------------------------------------------------------


aws dynamodb delete-table --table-name ProductCatalog
