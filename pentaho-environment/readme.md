![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


# **Pentaho Server - Deployment Steps using Docker:**

1- Send the "pentaho-server-docker" package (folder with dockerfile, docker-compose, lib, data) to the HML/PRD server.

2- Build the Pentaho Server 9 image based on the dockerfile (command: docker-compose build).

   If the HML/PRD server doesn't have internet access, it won't be possible to create the image directly. In this case, perform additional steps before running:
   - Generate the image on a machine with internet access and export the image (docker save) to a .tar file.
   - Load the file on the HML/PRD server (docker load).

3- Run the image to create the container and initialize it (command: docker-compose up).

4- Upload the jobs/transformations zip to the Pentaho Server web interface (http://server_ip:8081/pentaho/Login).

5- Adjust the database connection settings and user control.

6- Configure the schedule for JOB execution.

**Done!**

_**Note: You can also:**_ 
 - Commit the container to generate a snapshot.
 - Store the image in a docker-hub or nexus repository using the image registry concept.

## Set of Docker / Compose Commands

### build (creates image)
docker build -t lpaschoal/pentaho_server:9.0 .

**_Using compose:_** 
> docker-compose build

### Check existing images/containers
>  - docker images  
>  - docker ps  
>  - docker ps -a
>  - docker inspect
>  - docker logs --follow (container_id)

### First-time run (creates container)
> docker run -p 127.0.0.1:8081:8080 lpaschoal/pentaho_server:9.0 

**_Using compose:_** 
> docker-compose up

### Browse container files
> docker exec -t -i pentaho-server /bin/bash

### Start an existing container
> docker container start pentaho-server

**_Using compose:_** 
> docker-compose up

### Stop an existing container
> docker container stop pentaho-server

**_Usando compose:_** 
> docker-compose stop

### Customize container with configurations and then generate an image (snapshot)
> docker commit (container_id)  lpaschoal/pentaho_server_snapshot:2.0
