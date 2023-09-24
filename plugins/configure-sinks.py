import time

import requests

# URL da API do Kafka Connect
url = "http://connect:8083/connectors"

# Configuração do conector
configs = [
    {
        "name": "mongodb-sink-1",
        "config": {
            "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
            "tasks.max": "1",
            "topics": "topico001",
            "connection.uri": "mongodb://mongodb:27017",
            "database": "kafka",
            "collection": "testes",
            "key.converter": "org.apache.kafka.connect.json.JsonConverter",
            "value.converter": "org.apache.kafka.connect.json.JsonConverter",
            "key.converter.schemas.enable": "false",
            "value.converter.schemas.enable": "false"
        }
    },
    {
        "name": "mongodb-sink-2",
        "config": {
            "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
            "tasks.max": "1",
            "topics": "topico001",
            "connection.uri": "mongodb://mongodb:27017",
            "database": "kafka",
            "collection": "testes2",
            "key.converter": "org.apache.kafka.connect.json.JsonConverter",
            "value.converter": "org.apache.kafka.connect.json.JsonConverter",
            "key.converter.schemas.enable": "false",
            "value.converter.schemas.enable": "false"
        }
    }
]

for config in configs:
    name = config.get('name')
    status = 400
    tries = 5
    while (status != 201) & (tries > 0):
        tries -= 1
        try:
            # Envia a solicitação HTTP POST
            response = requests.post(url, json=config, headers={"Content-Type": "application/json"})
            status = response.status_code
        except Exception:
            time.sleep(10)

    # Verifica a resposta
    if response.status_code == 201:
        print(f"Conector {name} configurado com sucesso.")
    else:
        print(f"Erro ao configurar o conector {name}. Código de resposta:", response.status_code)
        print("Mensagem de erro:", response.text)
