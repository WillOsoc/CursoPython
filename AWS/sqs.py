import boto3

sqs = boto3.resource('sqs')
# Create a new Queue
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds':'5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

