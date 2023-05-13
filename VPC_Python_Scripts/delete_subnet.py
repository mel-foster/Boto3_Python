import boto3

subnet_id = "subnet-012871fe59ce20b25"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

#Script to delete Subnets
#Make sure to update info before executing