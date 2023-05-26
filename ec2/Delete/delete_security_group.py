import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-07a816a696150987e',
)

print(response)

#Remember to update SGID"