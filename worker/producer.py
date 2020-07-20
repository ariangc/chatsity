import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

def send_message_to_bot(cmd):
    channel = connection.channel()

    channel.queue_declare(queue = 'bot_queue')
    
    channel.basic_publish(
        exchange='', 
        routing_key='bot_key', 
        body=cmd
    )

    channel.close()