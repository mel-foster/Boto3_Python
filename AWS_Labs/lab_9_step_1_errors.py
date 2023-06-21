import logging
import boto3
from botocore.exceptions import ClientError

try:
    client = boto3.client('translate')
except ClientError as e:
    logging.warning("<your msg> {}".format(e))
