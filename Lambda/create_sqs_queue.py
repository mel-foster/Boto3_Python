# Imports the Boto3 library
import boto3

# Creates the client for SQS
sqs = boto3.client('sqs')

# Creates the SQS Queue and names it wk15_sqs_queue
response = sqs.create_queue(
    QueueName='wk15_sqs_queue')

# Prints the data
print(response)
