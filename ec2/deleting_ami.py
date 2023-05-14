import boto3

ami_id = "ami-06971f60c03d084df"

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId=ami_id
)

#Rember to update the AMI ID