# Imports the JSON and Boto3 libraries
import json
import boto3

# Imports the date and time
from datetime import datetime


def lambda_handler(event, context):
    
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S:%p')
    
    sqs = boto3.client("sqs")
    sqs.send_message(
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/277399983651/wk15_sqs_queue',
        MessageBody = current_time
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }