# Processing Messages
import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')

for m in queue.receive_messages(MessageAttributeNames=['Author']):
	author_text=''
	if m.message_attributes is not None:
		author_name = m.message_attributes.get('Author').get('StringValue')
		if author_name:
			author_text = ' ({0})'.format(author_name)

	print('Hello,{0}!{1}'.format(m.body,author_text))

	m.delete()

