__author__ = "Sumanth Kumar Batchu"

import boto3

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2',
           'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1']


def print_instance_details(response):
    for item in response["Reservations"]:
        for instance in item["Instances"]:
            print('{:50s}'.format(instance["PublicDnsName"]), end=': ')
            print('{:20s}'.format(instance["PublicIpAddress"]), end='   ')
            print(instance["Placement"]["AvailabilityZone"])
            print("---------------------------------------------------------------------------------------")

        

for region in regions:
    ec2_conn = boto3.client('ec2', region_name=region)
    print_instance_details(ec2_conn.describe_instances())

# This is the end of the file
