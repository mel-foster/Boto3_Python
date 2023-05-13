import boto3

route_table_id = "rtb-006169e1400f08dd0"
internet_gateway_id = "igw-008261ad506221275"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GateWayId=internet_gateway_id,
    RouteTableId=route_table_id
)

#Note that this is a script to create a route to the IGW