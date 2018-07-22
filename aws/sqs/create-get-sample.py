# -*- coding: utf-8 -*-

import boto3
import sys
import json
import pprint

operation = sys.argv[1]  # create:Queue作成、get:Queue取得
queue_name = sys.argv[2]  # Queue名

if operation == 'create':
    # Get the service resource
    sqs = boto3.resource('sqs')
    
    # Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(QueueName=queue_name, Attributes={'DelaySeconds': '5'})
    
    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
    
if operation == 'get':
    # Get the service resource
    sqs = boto3.resource('sqs')
    
    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    
    # You can now access identifiers and attributes
    # print(queue.url)
    # print(queue.attributes.get('DelaySeconds'))
    # pprint.pprint(queue.attributes)

    messages = queue.receive_messages(
        AttributeNames=[
            'All',
        ]
    )
    for message in messages:
        print(message.body)
        data = json.loads(message.body)
        print('Message=' + data.get('Message'))
        message.delete()

if operation == 'get-all':
    # Get the service resource
    sqs = boto3.resource('sqs')
    
    # Print out each queue name, which is part of its ARN
    for queue in sqs.queues.all():
        print(queue.url)
