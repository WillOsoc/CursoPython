# Select queue and create a new message
import boto3

sqs = boto3.resource('sqs')
# Select queue by name
queue = sqs.get_queue_by_name(QueueName='test')

print("Queue:",queue.url)
print("Delay Seconds:",queue.attributes.get('DelaySeconds'))

# Print all queues
for q in sqs.queues.all():
	print(queue.attributes['QueueArn'])
	print("Extract queue name:",queue.attributes['QueueArn'].split(':')[-1])

# Create new message
"""response = queue.send_message(MessageBody='world')

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

response =queue.send_message(MessageBody='boto3',
	MessageAttributes={
	'Author': {
		'StringValue':'Daniel',
		'DataType':'String'
	}
})"""

# send several messages in a row: "send_messageS"
response = queue.send_messages(Entries=[
	{
		'Id':'3',
		'MessageBody':'world3'
	},
	{
		'Id':'4',
		'MessageBody':'boto33',
		'MessageAttributes':{
			'Author': {
				'StringValue':'Will',
				'DataType':'String'
			}
		}
	}
])

# Print any failures
print(response.get('Failed'))