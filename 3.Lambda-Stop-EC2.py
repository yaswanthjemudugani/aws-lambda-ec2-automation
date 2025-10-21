import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Replace with your EC2 instance ID
    instance_id = 'i-009d288436dea7b1a'
    
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} stopped successfully.")
    
    return {
        'statusCode': 200,
        'body': f"EC2 instance {instance_id} stopped successfully in ap-south-1"
    }
