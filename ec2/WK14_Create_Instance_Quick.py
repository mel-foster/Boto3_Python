import boto3

ec2 = boto3.resource ('ec2')

instance = ec2.create_instances(
    ImageId = 'ami-0889a44b331db0194',
    MinCount = 3,
    MaxCount = 3, 
    InstanceType = 't2.micro',
    )
print(instance)

