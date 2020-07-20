import pika
from features import process_stock

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='financial')

def callback(ch, method, properties, body):
    body = body.decode('ascii')
    print(body)
    param_pos = body.find('=')

    if param_pos == -1:
        return {'response': '%s does not represent proper bot command. Commands = [/COMMAND=STOCK_CODE].' % body}

    cmd = body[:param_pos]
    param = body[param_pos+1:]

    if cmd == '/stock':
        print({'response': process_stock(param)})
    else:
        print({'response': '%s command not implemented.' % cmd})
    

channel.basic_consume(
    queue='financial', on_message_callback=callback, auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL + C')
channel.start_consuming()