![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

* **Official Download Source:** https://spark.apache.org/downloads.html

# PySpark on Ubuntu 22.04:

> Tutorial Adapted from: https://linuxhint.com/install-pyspark-ubuntu-22-04/

1. First, start by opening your terminal and updating the package repository:

    ```sudo apt update```

2. Next, you must install Java if you’ve not already installed it. Apache Spark requires Java version 8 or later. You can run the following command to quickly install Java:

    ```sudo apt install default-jdk -y```

    After the installation is completed, check the installed Java version to confirm that the installation is success:

    ```java --version```

3. For our case, let’s install the Spark version 3.3.2 with the following command:

    ```wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3-scala2.13.tgz```

    The downloaded file is archived. Extract it using tar as shown in the following. Replace the archive filename to match the one that you downloaded:

    ```tar xvf spark-3.3.2-bin-hadoop3-scala2.13.tgz```

    Once extracted, a new folder which contains all the Spark files are created in your current directory. We can list the directory contents to verify that we have the new directory. You then should move the created spark folder to your /opt/spark directory. Use the move command to achieve this.

    ```sudo mv <filename> /opt/spark```

4. Before we can use the Apache Spark on the system, we must set up an environment path variable. Run the following two commands on your terminal to export the environmental paths in the “.bashrc” file:

    ```
    export SPARK_HOME=/opt/spark

    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
    ```

    Refresh the file to save the environmental variables with the following command:

    ```Source ~/.bashrc```

5. With that, you now have Apache Spark installed on your Ubuntu 22.04. With Apache Spark installed, it implies that you have PySpark also installed with it. Let’s first verify that Apache Spark is installed successfully. Open the spark shell by running the spark-shell command.
    
    ```spark-shell```

    If the installation is successful, it oepns an Apache Spark shell window where you can start interacting with the Scala interface.

    The Scala interface is not everyone’s choice, depending on the task that you want to accomplish. You can verify that PySpark is also installed by running the pyspark command on your terminal.

    ```pyspark```

    It should open the PySpark shell where you can start executing the various scripts and creating programs that utilize the PySpark.

    Suppose you don’t get PySpark installed with this option, you can utilize pip to install it. For that, run the following pip command:

    ```pip install pyspark```

    Pip downloads and sets up PySpark on your Ubuntu 22.04. You can start using it for your data analytics tasks.