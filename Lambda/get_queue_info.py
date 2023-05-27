import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = '[ENTER Queue URL]

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        '[ENTER CUSTOM TEXT HERE]'
    )
)

print(response['MessageId'])