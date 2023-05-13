import boto3

route_table_id = "rtb-006169e1400f08dd0"

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)

#Script to delete a route table
#Make sure to update the Route Table Id
#Remember to have to detach subnets, and IGW before deleting
