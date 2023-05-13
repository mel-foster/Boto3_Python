import boto3

internet_gateway_id = "igw-008261ad506221275"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)

#Script to delete a IGW 
#Make sure to enter in the IGW you want to delete after it has been detached from a VPC