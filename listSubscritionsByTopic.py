sns = boto3.client('sns', region_name='eu-west-1')
topic_arn = ''

result = sns.list_subscriptions_by_topic(TopicArn=topic_arn)

subscriptions_processed = 0

# Check if otuput is paginated or not (i.e if NextToken is present in the response)
if ('NextToken' in result):
    next_token = result['NextToken']
    while next_token:
        endpoints = result['Endpoints']
        subscriptions_processed = len(endpoints) + subscriptions_processed
        result = sns.list_subscriptions_by_topic(TopicArn=topic_arn)
    # here we process the last call that does not contain NextToken
    subscriptions_processed = len(result['Endpoints']) + subscriptions_processed


print("Number of subscriptions: %d" % (subscriptions_processed))
