#!/usr/bin/python

import boto3
import os
import json

queue_url = "https://sqs.eu-west-1.amazonaws.com/547823592358/Jenkins.fifo" 

access_key = os.environ['AWS_ACCESS_KEY_ID']
secret_key = os.environ['AWS_SECRET_ACCESS_KEY']

sqs_client = boto3.client('sqs', region_name='us-east-1')

sqs_message = "{\n   AccessKeyID : " + access_key + ",\n   SecretAccessKey : " + secret_key + "\n}"
print sqs_message
sqs_client.send_message(QueueUrl=queue_url, MessageBody=sqs_message, MessageGroupId="1", MessageDeduplicationId="2")
