import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket="mfoster-boto3-050123", Key="test_file_string.txt", Body="Hey, this is a string", ContentType="text/plain")
 
