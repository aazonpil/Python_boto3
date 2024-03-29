import boto3
import logging

# Initialize the S3 client
s3_client = boto3.client('s3')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("S3_logger")

def create_s3_bucket(bucket_name, region):
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        logger.info(f"Bucket '{bucket_name}' created successfully in '{region}'. Response: {response}")
    except s3_client.exceptions.BucketAlreadyExists:
        logger.error(f"Bucket '{bucket_name}' already exists.")
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        logger.error(f"Bucket '{bucket_name}' is already owned by you.")
    except Exception as e:
        logger.error(f"Error creating bucket: {e}")

# Example usage with the new bucket name 'armaud-botp3-s3' and specifying the region 'us-east-1'
create_s3_bucket('boto3-s3-arnaud', 'eu-west-1')



