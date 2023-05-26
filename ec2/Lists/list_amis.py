import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images(Owners=['amazon'])

for image in response["Images"]:
    print(image["ImageId"], image["Name"], image["CreationDate"])




#Notes:
#Owners changed to 'self' would show if you had AMI's created