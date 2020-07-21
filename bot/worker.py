#!/usr/bin/env python

"""
      worker.py
      ----------
      This modules implements the AMQP protocol for the bot using
      pika, a lightweight implementation of a message broker for
      python. It handles messages that could not be understood by
      the bot. Once this module is executed, the bot will listen
      to requests on the RabbitMQ default port.
"""

__author__ = "Arian Gallardo"

import pika
import requests
from requests.auth import HTTPBasicAuth
from features import process_stock

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='financial')

def callback(ch, method, properties, body):
    """ Handles AMQP requests from a producer.

        :type ch: pika.adapters.blocking_connection.BlockingChannel
        :param ch: Blocking Channel to establish connection from the producer.

        :type method: pika.spec.Basic.Deliver
        :param method: AMQP deliver method.

        :type properties: pika.spec.BasicProperties
        :param method: Properties of the AMQP connection.

        :type body: bytes
        :param body: Body of the message sent.
    """
    body = body.decode('ascii')
    param_pos = body.find('=')
    id_user_pos = body.find('$')
    id_chatroom_pos = body.find('#')

    response = ""
    id_user = int(body[id_user_pos + 1:id_chatroom_pos])
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
    
    body = {'id_user': id_user, 'id_chatroom': id_chatroom,'msg_body': response} 

    requests.post('http://localhost:9997/api/message', json=body, auth=HTTPBasicAuth('ariangallardo21@gmail.com', 'Test_pwd21'))

channel.basic_consume(
    queue='financial', on_message_callback=callback, auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL + C')
channel.start_consuming()