import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='financial')

channel.basic_publish(exchange='', routing_key='financial', body='/stock=aapl.us')
print(" [x] Sent 'aapl.us'")
connection.close()