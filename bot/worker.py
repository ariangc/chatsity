import pika
import requests
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
    id_user_pos = body.find('$')
    id_chatroom_pos = body.find('#')

    response = ""
    id_user = int(body[id_user + 1:id_chatroom_pos])
    id_chatroom = int(body[id_chatroom_pos + 1:])

    if param_pos == -1:
        response = 'Message %s does not represent proper bot command. Commands = [/COMMAND=STOCK_CODE].' % body

    else:
        cmd = body[:param_pos]
        param = body[param_pos+1:id_user_pos]

        if cmd == '/stock':
           response = process_stock(param)
        else:
            response = 'Command %s not implemented.' % cmd
    
    requests.put('https://localhost:9997/api/message', json={
                                                            'id_user': id_user,
                                                            'id_chatroom': id_chatroom,
                                                            'msg_body': response
                                                        })

channel.basic_consume(
    queue='financial', on_message_callback=callback, auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL + C')
channel.start_consuming()