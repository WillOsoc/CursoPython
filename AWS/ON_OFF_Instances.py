import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

for r in response["Reservations"]:
	for i in r["Instances"]:
		
		print("Instance ID: " + str(i["InstanceId"]))
		turn_on_off = input(print("Encender (ON) o Apagar (OFF) Instancia? "))
		# instance_id = sys.argv[2]
		instance_id = i["InstanceId"]
		# action = sys.argv[1].upper()
		action = turn_on_off.upper()
		
		if action == "ON":
			# Do a dryrun first to verify permissions
			try:
				ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
			except ClientError as e:
				if 'DryRunOperation' not in str(e):
					raise

			# Dry run succeeded, run start_instances without dryrun
			try:
				response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
				print(response)
			except ClientError as e:
				print(e)

		elif action == "OFF":
			# Do a dryrun first to verify permissions
			try:
				ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
			except ClientError as e:
				if 'DryRunOperation' not in str(e):
					raise

			# Dry run succeeded, call stop_instances without dryrun
			try:
				response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
				print(response)
			except ClientError as e:
				print(e)
		else:
			print("Option not valid. Program Ends")