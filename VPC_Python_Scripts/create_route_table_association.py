import boto3

route_table_id = "rtb-006169e1400f08dd0"
subnet_id = "subnet-012871fe59ce20b25"

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])

#This script is used for associating a subnet to a route table
