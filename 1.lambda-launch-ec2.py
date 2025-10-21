import boto3

def lambda_handler(event, context):
    # Create an EC2 client for the Mumbai region
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Launch a new EC2 instance
    response = ec2.run_instances(
        ImageId='ami-06fa3f12191aa3337',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='AL2023',  # Replace with your actual key pair
        SecurityGroupIds=['sg-0703680985f56f283'],  # Replace with your SG ID
        SubnetId='subnet-0b9b0f798dbe19be2',  # Replace with your subnet ID (if applicable)
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Lambda-Launched-Instance'}
                ]
            }
        ]
    )
    
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Launched EC2 instance with ID: {instance_id}")
    
    return {
        'statusCode': 200,
        'body': f"EC2 instance {instance_id} launched successfully in ap-south-1"
    }
