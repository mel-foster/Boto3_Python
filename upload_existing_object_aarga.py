import boto3

s3 = boto3.client('s3')

s3.upload_file('/home/ec2-user/environment/Boto3_Python/test_text.txt', 'mfoster-boto3-050123', 'test_text_upload.txt',ExtraArgs={'ContentType':''})   
