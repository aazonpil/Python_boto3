import boto3
import logging
import csv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AWS Automation Logger")

# Initialize AWS clients
ec2_client = boto3.client('ec2', region_name='us-west-2')
s3_client = boto3.client('s3', region_name='us-west-2')
sns_client = boto3.client('sns', region_name='us-west-2')

def list_all_ec2():
    """
    Lists all EC2 instances in the specified AWS region.
    """
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

def generate_csv_report(instances_details, topic_arn):
    """
    Generates a CSV file containing details of EC2 instances and publishes a notification.
    """
    file_name = 'ec2_instances_report.csv'
    fieldnames = ['AmiLaunchIndex', 'InstanceId', 'ImageId', 'Tags']
    try:
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for instance_detail in instances_details:
                writer.writerow(instance_detail)
        logger.info("CSV report generated successfully.")
        publish_sns_topic(topic_arn, "EC2 Report has been generated.", "Report Generation Complete")
    except Exception as e:
        logger.error(f"Failed to generate CSV report: {e}")

def create_s3_bucket(bucket_name):
    """
    Creates an S3 bucket in the specified region.
    """
    try:
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
        logger.info(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        logger.error(f"Error creating bucket '{bucket_name}': {e}")

def upload_csv_to_bucket(file_name, bucket_name, topic_arn):
    """
    Uploads a CSV file to the specified S3 bucket and publishes a notification.
    """
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        logger.info(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'.")
        publish_sns_topic(topic_arn, "EC2 Report has been uploaded to S3.", "Report Upload Complete")
    except Exception as e:
        logger.error(f"Error uploading file '{file_name}' to bucket '{bucket_name}': {e}")

def create_sns_topic(topic_name):
    """
    Creates an SNS topic with the given name.
    """
    try:
        response = sns_client.create_topic(Name=topic_name)
        topic_arn = response['TopicArn']
        logger.info(f"Created SNS topic '{topic_name}' with ARN: {topic_arn}")
        return topic_arn
    except Exception as e:
        logger.error(f"Error creating SNS topic '{topic_name}': {e}")
        return None

def subscribe_sns_topic(topic_arn, email):
    """
    Subscribes an email address to the specified SNS topic.
    """
    try:
        response = sns_client.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=email)
        logger.info(f"Subscription request sent to {email}. ARN: {response['SubscriptionArn']}")
    except Exception as e:
        logger.error(f"Failed to subscribe {email} to topic ARN '{topic_arn}': {e}")

def publish_sns_topic(topic_arn, message, subject):
    """
    Publishes a message to the specified SNS topic.
    """
    try:
        sns_client.publish(TopicArn=topic_arn, Message=message, Subject=subject)
        logger.info(f"Message published to topic ARN '{topic_arn}'")
    except Exception as e:
        logger.error(f"Error publishing message to topic ARN '{topic_arn}': {e}")

if __name__ == "__main__":
    # Define the bucket and topic names
    bucket_name = 'myec2-report'
    topic_name = 'Myec2-report_notifications'
    
    # Create an S3 bucket
    create_s3_bucket(bucket_name)
    
    # Create an SNS topic
    topic_arn = create_sns_topic(topic_name)
    
    # List EC2 instances and generate a report
    instances_details = list_all_ec2()
    generate_csv_report(instances_details, topic_arn)
    
    # Upload the report to the S3 bucket
    upload_csv_to_bucket('ec2_instances_report.csv', bucket_name, topic_arn)
    
    # Subscribe to the SNS topic
    email = "example@example.com"
    subscribe_sns_topic(topic_arn, email)
    
    # Send a test message
    publish_sns_topic(topic_arn, "This is a test message from AWS automation script.", "AWS Automation Notification")
