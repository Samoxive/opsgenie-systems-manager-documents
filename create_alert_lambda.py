import boto3
import json
from botocore.vendored import requests
def handler(event, ctx):
	genieKey = event['genieKey']
	message = event['message']
	genieUrl = event['genieUrl']
	message = event['message']
	data = {'message': message}
	alias = event['alias']
	if alias:
		data['alias'] = alias
	description = event['description']
	if description:
		data['description'] = description
	actions = event['actions']
	if actions:
		data['actions'] = actions.split(',')
	tags = event['tags']
	if tags:
		data['tags'] = tags.split(',')
	entity = event['entity']
	if entity:
		data['entity'] = entity
	source = event['source']
	if source:
		data['source'] = source
	priority = event['priority']
	if priority:
		data['priority'] = priority
	user = event['user']
	if user:
		data['user'] = user
	note = event['note']
	if note:
		data['note'] = note
	headers = {'Content-Type': 'application/json', 'Authorization': 'GenieKey {}'.format(genieKey)}
	if genieUrl == '':
		genieUrl = 'https://api.opsgenie.com'
	response = requests.post('{}/v2/alerts'.format(genieUrl), headers=headers, data=json.dumps(data))
	if not response.ok:
		raise Exception('API responded with error! ' + response.text)
	return 'success!'