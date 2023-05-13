import boto3

vpc_id = "vpc-0534227e08150d0f1"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

#Note to update VPC before running 
