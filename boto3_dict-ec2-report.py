import boto3
import logging
import csv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("EC2_logger")

def list_all_ec2():
    """
    Lists all EC2 instances in the specified AWS region.
    """
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    response = ec2_client.describe_instances()
    instances_details = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_details = {
                'AmiLaunchIndex': instance.get('AmiLaunchIndex', 'N/A'),
                'InstanceId': instance.get('InstanceId', 'N/A'),
                'ImageId': instance.get('ImageId', 'N/A'),
                'Tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            }
            instances_details.append(instance_details)
    
    return instances_details

if __name__ == "__main__":
    instances_details = list_all_ec2()
    for instance_detail in instances_details:
        logger.info(instance_detail)

def generate_csv_report(instances_details):
    """
    Generates a CSV file containing details of EC2 instances.
    """
    fieldnames = ['AmiLaunchIndex', 'InstanceId', 'ImageId', 'Tags']
    with open('ec2_instances_report.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for instance_detail in instances_details:
            writer.writerow(instance_detail)
    logger.info("CSV report generated successfully.")

if __name__ == "__main__":
    instances_details = list_all_ec2()
    generate_csv_report(instances_details)
def create_s3_bucket(bucket_name, region_name):
    """
    Creates an S3 bucket in the specified region.
    """
    try:
        s3_client = boto3.client('s3', region_name=region_name)
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region_name}
        )
        logger.info(f"Bucket '{bucket_name}' created successfully in '{region_name}'.")
    except Exception as e:
        logger.error(f"Error creating bucket '{bucket_name}': {e}")

if __name__ == '__main__':
    bucket_name = 'myec2-report'
    region_name = "us-west-2"  # Corrected region
    create_s3_bucket(bucket_name, region_name)
def upload_csv_to_bucket(file_name, bucket_name):
    """
    Uploads a CSV file to the specified S3 bucket.
    """
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        logger.info(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'.")
    except Exception as e:
        logger.error(f"Error uploading file '{file_name}' to bucket '{bucket_name}': {e}")

if __name__ == '__main__':
    file_name = 'ec2_instances_report.csv'
    bucket_name = 'myec2-report'
    upload_csv_to_bucket(file_name, bucket_name)
def create_sns_topic(topic_name):
    """
    Creates an SNS topic with the given name.
    """
    try:
        sns_client = boto3.client('sns', region_name="us-west-2")  
        response = sns_client.create_topic(Name=topic_name)
        topic_arn = response['TopicArn']
        logger.info(f"Created SNS topic with ARN: {topic_arn}")
        return topic_arn
    except Exception as e:
        logger.error(f"Error creating SNS topic '{topic_name}': {e}")
        return None

if __name__ == "__main__":
    topic_name = "Myec2-report_uploaded"
    topic_arn = create_sns_topic(topic_name)

def subscribe_sns_topic(topic_arn, email):
    """
    Subscribes an email address to the specified SNS topic.
    """
    try:
        sns_client = boto3.client('sns', region_name="us-west-2")  # Corrected region
        response = sns_client.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
        logger.info(f"Subscription request sent to {email}. Subscription ARN: {response['SubscriptionArn']}")
    except Exception as e:
        logger.error(f"Failed to subscribe {email} to topic ARN '{topic_arn}': {e}")

if __name__ == "__main__":
    email = "aazonpil@gmail.com"
    subscribe_sns_topic(topic_arn, email)

    
def publish_sns_topic(topic_arn, message, subject):
    """
    Publishes a message to the specified SNS topic.
    """
    try:
        sns_client = boto3.client('sns', region_name="us-west-2") 
        response = sns_client.publish(TopicArn=topic_arn, Message=message, Subject=subject)
        logger.info(f"Message published to topic ARN '{topic_arn}'")
    except Exception as e:
        logger.error(f"Error publishing message to topic ARN '{topic_arn}': {e}")

if __name__ == "__main__":
    message = "Hello, the EC2-report has been uploaded to S3."
    subject = "EC2 Report Uploaded"
    publish_sns_topic(topic_arn, message, subject)
    

