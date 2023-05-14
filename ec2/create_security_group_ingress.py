import boto3

security_group_id = "sg-0eac9d2641e760344"

ec2 = boto3.client('ec2')

response = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)
