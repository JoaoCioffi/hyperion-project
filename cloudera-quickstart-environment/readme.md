# How to install and running Cloudera Docker Container on Ubuntu

> Adapted from: https://dataakkadian.medium.com/how-to-install-and-running-cloudera-docker-container-on-ubuntu-b7c77f147e03

This tutorial will show how to install and configure version 5.7.0 of Cloudera Distribution Hadoop (CDH 5) on Ubuntu 16.04 host using Docker.

## What’s CDH?

CDH (Cloudera’s Distribution Including Apache Hadoop) is the most complete, tested, and widely deployed distribution of Apache Hadoop. CDH is 100% open source and is the only Hadoop solution to offer batch processing, interactive SQL and interactive search as well as enterprise-grade continuous availability. More enterprises have downloaded CDH than all other distributions combined.

## Why Docker?

Getting down to the nuts and bolts, Docker allows applications to be isolated into containers with instructions for exactly what they need to survive that can be easily ported from machine to machine. Virtual machines also allow the exact same thing. While Docker has a more simplified structure compared to both of these, the real area where it causes disruption is resource efficiency.
Install Docker

Installing docker is very easy. The choice here is Ubuntu 16.04, so before start with the installation takes into consideration the requirements then follow this guide.

## Uninstall old versions

Older versions of Docker were called docker or docker-engine. If these are installed, uninstall them:

```
$ sudo apt-get remove docker docker-engine docker.io
```

The contents of /var/lib/docker, including images, containers, volumes, and networks, are preserved. Check the content using these commands below.

```
$ sudo ls /var/lib/docker
```

## Install using the repository

Update the apt package index, install packages to allow apt to use a repository over HTTPS, and add Docker’s official GPG key:

```
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

```
$ sudo apt-key fingerprint 0EBFCD88
```

Use the following command to set up the stable repository. You always need the stable repository, even if you want to install builds from the edge or test repositories as well.

```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

## Install Docker CE

Update the apt package index, list the available versions in the repo, then select and install a version of Docker CE:

```
$ sudo apt-get update
$ apt-cache madison docker-ce
```

Install a specific version by its fully qualified package name, for example, docker-ce=5:18.09.0~3-0~ubuntu-xenial, and verify that Docker CE is installed correctly by running the hello-world image.

```
$ sudo apt-get install docker-ce=5:18.09.0~3-0~ubuntu-xenial
docker run hello-world
```

The last command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

## Importing the Cloudera QuickStart Image

Before importing the image assure Docker is running, and type this into the terminal in the home directory /home/your_name. This will take a couple of minutes to complete because it’s a large file size so you can take a cup of tea or whatever you like.

```
$ docker pull cloudera/quickstart:latest
```

The next image is to check if everything working fine.

## Running a Cloudera QuickStart Container

To run a container using the image, you must know the name or hash of the image. If you followed the instructions above, the name could be cloudera/quickstart: latest. The hash is also printed in the terminal when you import, or you can look up the hashes of all imported images with:

```
$ docker images
```

Once you know the name or hash of the image, you can run it:

```
docker run -m 4G --memory-reservation 2G --memory-swap 8G --hostname=quickstart.cloudera --privileged=true -t -i -v $(pwd):/zaid --publish-all=true -p8888 -p8088 cloudera/quickstart /usr/bin/docker-quickstart
```

Basically, this command is telling docker to run an image with 4GByte the maximum amount of memory the container can use, with 2GByte as soft limit smaller than 4GByte which is activated when Docker detects contention or low memory on the host machine, and 8GByte the amount of memory this container is allowed to swap to disk. Privileged mode is required for HBase database, with option -i means interactive, option -t means to open it in the terminal, and option -v allows to share volumes with the container, so anything that we put in the home directory, will show up in the Docker container under the directory /zaid . We have to change this to the directory of our files. The option — publish-all=true opens up all the host ports to the docker ports, so you can access programs like the Hue in the port 8888 and YARN in the port 8088, and others programs.

Using the command below we can check if the deployment of the image working smoothly.

```
docker ps -a
```

## Getting HUE and YARN to work

We need to check if Hue and YARN are working in our docker machine, so we take the container Id from the information generated by the last command and we utilize these Id with the docker inspect command.

```
docker inspect [CONTAINER ID]
```

For an example, we take into account that Hue is working on the port 8888 inside the docker machine, 32768 outside the docker machine which means on our localhost, and YARN 8088 inside, 32769 outside.

## Collect system information

Docker CE defaults values is to use of the system's memory. So the minimum you should use is 4GB, The laptop for this guide only has 8GB, so we allocate 4GB to docker when its running

Using the command below we can check that the laptop memory is 8031140 kB.

```
sudo cat /proc/meminfo
```

And to see if we are running Docker CE with the minimum configuration we use this command.

```
docker stats [CONTAINER ID]
```

Once we used the last command it showed a live stream of statistics when the memory usage of Docker image is between 1.77 GBytes and 4GBytes.

Alternatively, you can get a Medium subscription for $5/month. If you use this link, it will support me.

## After installation

After setting up our cloudera environment using docker, you can simply execute ```run.sh``` file to automatically open your cloudera-quickstart application.

But first ensure that this file has the correct permissions by typing:

```
chmod +x run.sh
```

Since . refers to the current directory: if yourscript.sh is in the current directory, you can simplify this to:

```
./run.sh
```

## Important!

Obs: To copy a file from your Ubuntu host OS to the Cloudera QuickStart container, you can follow these steps:

1. Identify the file you want to copy: Make sure you know the path and name of the file you want to transfer from your Ubuntu host to the Cloudera container.

2. Copy the file to the container: You can use the docker cp command to copy the file from your host to the container. The syntax for the command is as follows:

```docker cp <path_to_local_file> <container_name_or_id>:<path_in_container>```

Replace <path_to_local_file> with the full path to the file on your Ubuntu host, <container_name_or_id> with the name or ID of your running Cloudera QuickStart container, and <path_in_container> with the desired path inside the container where you want to place the file.

For example, if you want to copy a file named example.txt located in your home directory (/home/your_username/example.txt) to the /zaid directory inside the container, the command would be:

```docker cp /home/your_username/example.txt my_cloudera_container:/zaid/```

Note: You can use the docker ps command to list the running containers and find the name or ID of your Cloudera QuickStart container.

3. Access the file in the Cloudera environment: Once the file is copied, you can access it within the Cloudera QuickStart container at the specified path (/zaid in the example above). You can use the Cloudera user interface or command-line tools within the container to work with the file as needed.

Remember that the Cloudera QuickStart container operates as an isolated environment with its own file system. It doesn't directly share the same root file system as your Ubuntu host. Therefore, to transfer files between the host and container, you need to use the docker cp command as outlined above.

# Cloudera Quickstart on VM

You can also run a cloudera-quickstart machine using a VM (such as virtualbox) following this tutorial: https://www.simplilearn.com/tutorials/big-data-tutorial/cloudera-quickstart-vm

In this case you need to download a full built app (e.g a CentOS redhat based) that has the Cloudera environment inside.

In a nutshell: first install virtual-box in your OS and then import your cloudera-quickstart appliance using a VM.

# 🔴 Disclaimer 🔴

The original tutorial was built to work with Ubuntu 16.04 and I tried it using Ubuntu 22.04.2 LTS.
It worked normally including all the Cloudera basic services, it demonstrated a stable response. The only issue I've noticed was some warning msgs related to deprecated versions (probably related to the docker older images). You can use it by your own risk.