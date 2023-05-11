import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket="mfoster-boto3-050123")

extension = ".txt"

for content in response["Contents"]:
    
    if(extension in content["Key"][-(len(extension)):]): 
        print(content["Key"])



