sns = boto3.client('sns', region_name='eu-west-1')
sns_app_platform_arn = ''

result = sns.list_endpoints_by_platform_application(PlatformApplicationArn=sns_app_platform_arn)

endpoints_processed = 0

# Check if otuput is paginated or not (i.e if NextToken is present in the response)
if ('NextToken' in result):
    next_token = result['NextToken']
    while next_token:
        endpoints = result['Endpoints']
        for endpoint in endpoints:
            print(endpoint['Attributes']['Enabled'])
            if endpoint['Attributes']['Enabled'] == 'true':
                endpoints_processed = endpoints_processed + 1
        result = sns.list_endpoints_by_platform_application(PlatformApplicationArn=sns_app_platform_arn,
                                                            NextToken=next_token)
        next_token = result['NextToken']
        # Could be you will need to handle the last request that comes without a NextToken
else:
    next_token = None
    endpoints = result['Endpoints']
    for endpoint in endpoints:
        print(endpoint['Attributes']['Enabled'])
        if endpoint['Attributes']['Enabled'] == 'true':
            endpoints_processed = endpoints_processed + 1

print("Number of enabled platform endpoints: %d" % (endpoints_processed))
