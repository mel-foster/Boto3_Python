import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket="mfoster-boto3-050123", Key="test_file_string.txt", Body="Hey, this is a string", ContentType="text/plain")
 
#s3.put_objects(Bucket="mfoster-boto3-050123",
                #Key="folder/foldera/folder1/test_test_string.txt,
                #Body="Hey this is a string",
                #ContentType= "text/plain")