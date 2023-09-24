# kafka-connect-mongodb-sink
Kafka Connect + MongoDB sink example. 

## Services
You need to run the project's docker compose:
`docker-compose up -d`

This will start these services:
* zookeeper
* kafka
* schema-registry
* connect
* kafdrop
* mongodb

After the `connect` service starts, another service will run and finish: `configure-sink`. It will
configure the connector/sinks contained in `plugins/configure-sinks.py` file. By default, it will create the
`mongodb-sink-1` and `mongodb-sink-2`, to show you that you can create 2 different sinks from the same kafka topic.

After everything start, you would run the `producer_tests.py` file, which will publish a message in the topic 
`topico001`. This is the same topic configured in the `mongodb-sink-1` and `mongodb-sink-2`, so you will see the
data in the MongoDB service, if you want to.
