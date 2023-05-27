import boto3 
import json

from datetime import datetime

def lambda_handler(event, context):
    # creating sqs client
    sqs = boto3.client('sqs')  
    # using the now() function to get a datetime object containing current date and time.
    now = datetime.now() 
    # using datetime.strftime() function to create a string representing
    # the current time
    time_date = now.strftime("%H:%M:%S %m/%d/%Y")  
   
     
    # sending the message to the sqs queue
    sqs.send_message(  
        # sqs queue url: found in SQS Details
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/796344786736/fosterwk15', 
        MessageBody = time_date)
    return {
        'statusCode': '200',
        'body': json.dumps('Order_Processed')
    }