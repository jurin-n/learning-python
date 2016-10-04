# -*- coding: utf-8 -*-

import boto3
import sys
import json

operation = sys.argv[1] # start:ec2インスタンス起動、stop:ec2インスタンス停止
instance_id = sys.argv[2] # 操作対象のEC2インスタンスのインスタンスID

client = boto3.client('ec2')

if operation == 'start':
    response = client.start_instances(
        InstanceIds=[instance_id],
        AdditionalInfo='',
        DryRun=False)

if operation == 'stop':
    response = client.stop_instances(
        InstanceIds=[instance_id],
        DryRun=False,
        Force=False
        )

print(json.dumps(response,indent=4))