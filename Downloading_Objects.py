import boto3
import os
from list_objects_key_filter import list_objects_keys

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)
    
if __name__ == '__main__':

    bucket = 'mfoster-boto3-050123'
    key = 'test_file_string.txt'
    filename = 'test_file_string.txt'
    
    s3 = boto3.client('s3')
    
    
        
    keys = list_objects_keys(s3, bucket, prefix='folder')
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)



# Simple download 
# s3 = boto3.client('s3')

# s3.download_file('mfoster-boto3-050123', 'test_file_string.txt ', 'test_file_string.txt'