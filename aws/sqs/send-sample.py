# -*- coding: utf-8 -*-

import boto3
import sys
import pprint

operation = sys.argv[1]  # 1:send a message 、2:send a message with attributes、3:batch send
queue_name = sys.argv[2]  # Queue名
message = sys.argv[3]  # メッセージ

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName=queue_name)
    
if operation == '1':
    # Create a new message
    response = queue.send_message(MessageBody=message)
    
    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))

    
if operation == '2':
    response = queue.send_message(MessageBody=message
                       , MessageAttributes={'Author': {
                                                'StringValue': 'Daniel',
                                                'DataType': 'String'
                                                } })
    
    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))
    
if operation == '3':
    response = queue.send_messages(Entries=[
        {
            'Id': '1',
            'MessageBody': message
        },
        {
            'Id': '2',
            'MessageBody': 'boto3',
            'MessageAttributes': {
                'Author': {
                    'StringValue': 'Daniel',
                    'DataType': 'String'
                }
            }
        }
    ])
    
    # Print out any failures
    print(response.get('Failed'))
    
    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))
    pprint.pprint(response)