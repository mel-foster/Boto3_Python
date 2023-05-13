import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
   Bucket='mfoster-boto3-050123'
)
    
print(response)
