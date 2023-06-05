![ApacheCassandra](https://img.shields.io/badge/cassandra-%231287B1.svg?style=for-the-badge&logo=apache-cassandra&logoColor=white)

# Important!

Docker is needed to run a Cassandra image. Use the following commands in a terminal (Linux):

```
sudo docker pull cassandra:latest
```

```
sudo docker run --restart=always --name cass_cluster cassandra:latest
```

and wait for some minutes until the image gets loaded in the container. To confirm if the process is running you can type in a second terminal: 

```
sudo docker ps -a
```

and to load a cassandra shell type:

```
sudo docker exec -it cass_cluster cqlsh
```

Now you are in a Cassandra environment (shell). With it you can create tables and load the desired data.