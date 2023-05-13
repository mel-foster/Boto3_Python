import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    
    InstanceId= 'ENTER EC2 ID HERE', 
    Name= 'LIST CUSTOM NAME HERE')
    
print(response["ImageId"])