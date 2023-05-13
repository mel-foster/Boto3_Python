import boto3

vpc_id = 'vpc-0534227e08150d0f1'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])

#Note: Remember to update the VPC ID# to be for the VPC you are using
