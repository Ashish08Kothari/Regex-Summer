  
# download one of the latest version of kafka \=\>  
wget https://downloads.apache.org/kafka/3.7.0/kafka\_2.12-3.7.0.tgz

# previous version  \=\>  
wget https://downloads.apache.org/kafka/3.7.1/kafka\_2.13-3.7.1.tgz

# extracting Kafka file  
tar \-xvf kafka\_2.12-3.3.1.tgz

-----------------------  
# to check  java version \=\>  
java \-version

# to install java \=\>  
sudo yum install java-1.8.0-openjdk

java \-version

cd kafka\_2.12-3.3.1

-------------------------------  
# Change private DNS server to with the public IP  
## change server.properties so that it can run in public IP 

sudo nano config/server.properties

43.204.214.228  
\=\> look for network thread , uncomment the advertised.listeners file  
cat  config/server.properties | grep \-i 'advertise'  
\---------------  
# Start Zoo-keeper : services and basic config properties  
sudo bin/zookeeper-server-stop.sh        \[In case zookeeper is running\]

bin/zookeeper-server-start.sh config/zookeeper.properties

----------------------------------------  
43.204.214.228  
# Start Kafka-server  
## Duplicate the session & enter in a new console ( to increae the amount of space)

export KAFKA\_HEAP\_OPTS="-Xmx256M \-Xms128M"  
cd kafka\_2.12-3.3.1  
bin/kafka-server-start.sh config/server.properties

-----------------------------  
# Create the topic:  
## Create your 3rd session   
### My public IP is : 3.111.41.37  
cd kafka\_2.12-3.3.1  
bin/kafka-topics.sh \--create \--topic demo\_testing \--bootstrap-server  43.204.214.228:9092 \--replication-factor 1 \--partitions 1
--------------------------  

# Start Producer:  
bin/kafka-console-producer.sh \--topic demo\_testing \--bootstrap-server 43.204.214.228:9092

-------------------------  
# Start Consumer:  Create one more session & enter in a new console   
cd kafka\_2.12-3.3.1  
bin/kafka-console-consumer.sh \--topic demo\_testing \--bootstrap-server 43.204.214.228:9092  
