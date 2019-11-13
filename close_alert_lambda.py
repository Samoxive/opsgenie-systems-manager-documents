import boto3
import json
from botocore.vendored import requests
def handler(event, ctx):
	genieKey = event['genieKey']
	identifier = event['identifier']
	identifierType = event['identifierType']
	if not identifierType:
		identifierType = 'id'
	data = {}
	user = event['user']
	if user:
		data['user'] = user
	source = event['source']
	if source:
		data['source'] = source
	note = event['note']
	if note:
		data['note'] = note
	genieUrl = event['genieUrl']
	if not genieUrl:
		genieUrl = 'https://api.opsgenie.com'
	headers = {'Content-Type': 'application/json', 'Authorization': 'GenieKey {}'.format(genieKey)}
	params = {'identifierType': identifierType}
	response = requests.post('{}/v2/alerts/{}/close'.format(genieUrl, identifier), headers=headers, data=json.dumps(data), params=params)
	if not response.ok:
		raise Exception('API responded with error! ' + response.text)
	return 'success!'