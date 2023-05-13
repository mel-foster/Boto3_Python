import boto3

internet_gateway_id = "igw-008261ad506221275"
vpc_id = "vpc-0534227e08150d0f1"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

#Script to delete the attachement for an IGW to a VPC