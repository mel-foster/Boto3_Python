import boto3

route_table_id = "rtb-006169e1400f08dd0"

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)
