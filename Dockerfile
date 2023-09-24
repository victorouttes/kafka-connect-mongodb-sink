FROM confluentinc/cp-kafka-connect:latest

# Copie o seu JAR personalizado para o diretório de plugins do Kafka Connect
COPY ./plugins/mongo-kafka-connect-1.11.0-all.jar /usr/share/java/
