#This code will create a standard SQS
import boto3

#Create a low-level SQS Client
sqs = boto3.client('sqs', region_name = 'us-east-1')

#Creating the Queue
response = sqs.create_queue(
    QueueName= 'fosterwk15')
print(response)