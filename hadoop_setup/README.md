# Setup Guide for Standalone Hadoop Cluster

## Prerequisites

● Operation system: Ubuntu 18.04 LTS (highly recommended)

● Chipset: x86 (optional to the expected version of Hadoop)

● If you do not have Ubuntu, consider virtual machines

○ VMWare Fusion (MacOS)

○ Oracle Virtual Box (Windows)

○ Docker (Windows)

## Installation

Install Hadoop

1. Install Java 8 (highly recommended)

```bash
sudo apt install openjdk-17-jre-headless
sudo apt install openjdk-17-jdk-headless
```
2. Install ssh and pdsh
```bash
sudo apt install ssh
sudo apt install pdsh
```
3. Setup passphrase for ssh

```bash
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys

# ensure the file ~/.ssh/authorized_keys exists
# check whether you can ssh to localhost
ssh localhost
```
4. Configure rcmd to ssh as default
```bash
sudo nano /etc/pdsh/rcmd_default

# add “ssh” to the file
# save & quit
# HOẶC có thể dùng lệnh sau
# sudo echo “ssh” > /etc/pdsh/rcmd_default
```
5. Download Hadoop 3.2.1 (highly recommended) 
https://hadoop.apache.org/release/3.2.1.html

```bash
cd Desktop
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
tar -xvf hadoop-3.2.1.tar.gz
```
6. Declare JAVA_HOME for Hadoop
```bash
# cd to the extracted folder of Hadoop
nano etc/hadoop/hadoop-env.sh
# add this line to the end of the file
# check your own Java path if different
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
# save & quit
```
7. Verify installation
```
# cd to the extracted folder of Hadoop
bin/hadoop
```


## Set up Pseudo-Distributed Mode

### Configuration

Edit these following files

- `etc/hadoop/core-site.xml`
```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
- `etc/hadoop/hdfs-site.xml`
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

### Run a MapReduce job locally

1. Format the filesystem
```bash
bin/hdfs namenode -format
```


2. Start NameNode daemon and DataNode daemon
```bash
sbin/start-dfs.sh
# check log output in .../logs as needed
# if you fail to start a daemon then,
sbin/stop-all.sh
sudo rm -rf /tmp/*
sudo reboot
bin/hdfs namenode -format -force

# then try to start again
```




3. Browse the web interface for the NameNode; by default it is available at: http://localhost:9870/

4. Make the HDFS directories required to execute MapReduce jobs:
```bash
bin/hdfs dfs -mkdir /user
bin/hdfs dfs -mkdir /user/<username>
```


5. Copy the input files into the distributed file system:
```bash
bin/hdfs dfs -mkdir input
bin/hdfs dfs -put etc/hadoop/*.xml /user/abc/input
```


6. Run some of the examples provided (need to set up YARN in advance)
```bash
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar grep input output 'dfs[a-z.]+'
```


### Ensure the corresponding jar file exists in the folder mapreduce/

**Note**: after setting up YARN, this step requires [Connecting to ResourceManager at /0.0.0.0:8032]

7. Examine the output files: Copy the output files from the distributed file system to the local filesystem and examine them:
```bash
bin/hdfs dfs -get output output
cat output/*
```


or

View the output files on the distributed file system:
```bash
bin/hdfs dfs -cat output/*
```


8. When you’re done, stop the daemons with:
```bash
sbin/stop-dfs.sh
```


## Execute job on YARN

The following instructions assume that 1. ~ 4. steps of the above instructions are already executed.

5. Configure parameters as follows:

- `etc/hadoop/mapred-site.xml`
```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```


- `etc/hadoop/yarn-site.xml`
```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```
6. Start ResourceManager daemon and NodeManager daemon:
```bash
sbin/start-yarn.sh
```

7. Browse the web interface for the ResourceManager; by default it is available at: http://localhost:8088/

8. Run a MapReduce job.

9. When you’re done, stop the daemons with:
```bash
sbin/stop-yarn.sh
```


### Read more about modes of Hadoop here

● Local (Standalone) Mode

● Pseudo-Distributed Mode

● Fully-Distributed Mode

# References 
● https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html 

● https://www.programmersought.com/article/93394144266/ 

● clean up Hadoop: https://stackoverflow.com/questions/26545524/there-are-0-datanodes-running-and-no-nodes-are-excluded-in-this-operation 

● Turn off safemode: https://stackoverflow.com/questions/15803266/name-node-is-in-safe-mode-not-able-to-leave