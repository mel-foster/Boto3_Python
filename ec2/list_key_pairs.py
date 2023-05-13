import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_key_pairs()
        
for keypair in response["KeyPairs"]:
    print(keypair["KeyName"], keypair["KeyPairId"])
    
#Note you will only get results if you have active keypairs created