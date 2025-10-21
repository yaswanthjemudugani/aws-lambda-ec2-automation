import boto3

def lambda_handler(event, context):
    # Create EC2 client for Mumbai region
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Replace with your EC2 instance ID
    instance_id = 'i-009d288436dea7b1a'
    
    # Terminate the EC2 instance
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} terminated successfully.")
    
    return {
        'statusCode': 200,
        'body': f"EC2 instance {instance_id} terminated successfully in ap-south-1"
    }
