import boto3

def empty_bucket(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)
    
    if "Contents" in response:
        objects = [{'Key': content["Key"]} for content in response["Contents"]]
        
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects':objects
            }
        )

        while response.get("NextContinuationToken"):
            response = client.list_objects_v2(Bucket=bucket, 
                            ContinuationToken=response["NextContinuationToken"])
                            
            
            objects = [{'Key': content["Key"]} for content in response["Contents"]]
            
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects':objects
                }
            )

s3 = boto3.client('s3')

bucket = "mfoster-boto3-050123"

empty_bucket(s3, bucket)

response = s3.delete_bucket(
    Bucket=bucket
    )


#Note: Just running the code below will not work as it will cause an error if bucket is not empty If it is empty it will delete:
#import boto3

#s3 = boto3.client('s3')

#bucket = "mfoster-boto3-050123"

#response = s3.delete_bucket(
   # Bucket=bucket
    #)


#The code below in this section will empty out an S3 bucket:
    
#import boto3

#def empty_bucket(client, bucket):
#    response = client.list_objects_v2(Bucket=bucket)
    
#    if "Contents" in response:
#        objects = [{'Key': content["Key"]} for content in response["Contents"]]
#        
#        response = client.delete_objects(
#            Bucket=bucket,
#            Delete={
#                'Objects':objects
#            }
#        )

#        while response.get("NextContinuationToken"):
#            response = client.list_objects_v2(Bucket=bucket, 
#                            ContinuationToken=response["NextContinuationToken"])
                            
            
#            objects = [{'Key': content["Key"]} for content in response["Contents"]]
            
#            response = client.delete_objects(
#               Bucket=bucket,
#                Delete={
#                    'Objects':objects
               # }
            #)

#s3 = boto3.client('s3')

#bucket = "mfoster-boto3-050123"

#empty_bucket(s3, bucket)
