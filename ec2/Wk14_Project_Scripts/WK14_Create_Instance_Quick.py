import boto3

ec2 = boto3.resource ('ec2')

instance = ec2.create_instances(
    ImageId = 'ami-0889a44b331db0194',
    MinCount = 3,
    MaxCount = 3, 
   
#ADDING IN ADDITIONAL INFORMATION & TAGS
    InstanceType = 't2.micro',
    KeyName= 'COMPLEXWK14',
    TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Linux Server'},
                {'Key': 'Env','Value': 'Dev'}]
                          },
                      ],
                      )
print(instance)
