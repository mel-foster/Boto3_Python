import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    
    InstanceId= 'i-0179c894afc7e98f0', 
    Name= 'Green Group AMI DEMO')
    
print(response["ImageId"])

#Used for creating an AMI off of an Existing Instance