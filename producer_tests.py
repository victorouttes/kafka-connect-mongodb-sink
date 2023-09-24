from confluent_kafka import Producer
import json

producer_config = {
    'bootstrap.servers': 'localhost:29092',  # Endereço do servidor Kafka
    'client.id': 'python-producer'
}

producer = Producer(producer_config)

topic = 'topico001'

mensagem = {'database': 'kafka', 'collection': 'testes', 'nome': 'Pedro'}
mensagem_str = json.dumps(mensagem)
producer.produce(topic, mensagem_str)

producer.flush()
