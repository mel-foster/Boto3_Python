import boto3

s3 = boto3.client('s3')

#with open("test_text.txt", 'rb') as f:
#    s3.put_object(Bucket="mfoster-boto3-050123", Key="test_file.txt", Body=f, ContentType="text/plain")
#Ran this way in the Udemy Lab resulted errors, worked for others so keep this for reference

with open("/home/ec2-user/environment/Boto3_Python/test_text.txt", 'rb') as f:
    s3.put_object(Bucket="mfoster-boto3-050123", Key="test_file.txt", Body=f, ContentType="text/plain")
 
 
