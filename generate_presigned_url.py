import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object',Params={'Bucket': "mfoster-boto3-050123",'Key': "test_file.txt"},ExpiresIn=300)

print(response)