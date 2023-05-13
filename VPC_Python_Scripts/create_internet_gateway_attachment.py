import boto3

internet_gateway_id = 'igw-008261ad506221275'
vpc_id = 'vpc-0534227e08150d0f1'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)
    
#Note: this script is to attach an Internet Gateway to a VPC
#Make sure to update with the custom IGW & VPC that were previously 
#Created or that you want to use.
