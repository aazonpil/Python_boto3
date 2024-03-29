import boto3
import csv

def list_all_ec2():
    """
    The function lists all the instances that exist.
    """
    # Set up the client
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    # List all instances
    response = ec2_client.describe_instances()

    list_instances = []  # Initialize the list outside the loop
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ImageId=instance['ImageId']
            InstanceId=instance['InstanceId']
            InstanceType=instance['InstanceType']
            InstanceName=instance['Tags'][0]['Value']
            list_instances.append([InstanceName, InstanceId, ImageId, InstanceType])
        return list_instances
if __name__ == "__main__":
    list_instances=list_all_ec2()

    for item in list_instances:
        print(item)

def generate_csv_report(list_instances):
    """
    Generates a CSV report from the list of EC2 instance details.
    Each instance detail is expected to be a list in the order of:
    [InstanceName, InstanceId, ImageId,InstanceType]
    """
    fieldnames = ['Instance Name', 'Instance ID', 'Image ID', 'Instance Type']
    with open('ec2_report.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldnames)  # Write the header row
        csvwriter.writerows(list_instances)  # Write the instance details
    print("CSV report generated successfully.")

if __name__ == "__main__":
    # Assuming list_all_ec2() is defined elsewhere and returns a list of lists.
    list_instances = list_all_ec2()
    generate_csv_report(list_instances)


