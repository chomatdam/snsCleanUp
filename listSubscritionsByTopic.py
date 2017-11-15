import boto3

sns = boto3.client('sns', region_name='eu-west-1')
topic_arn = ''

result = sns.list_subscriptions_by_topic(TopicArn=topic_arn)

subscriptions_processed = 0

# Check if otuput is paginated or not (i.e if NextToken is present in the response)
if ('NextToken' in result):
    next_token = result['NextToken']
    while next_token:
        subscriptions = result['Subscriptions']
        subscriptions_processed = len(subscriptions) + subscriptions_processed
        result = sns.list_subscriptions_by_topic(TopicArn=topic_arn, NextToken=next_token)
        next_token = result['NextToken']
    # here we process the last call that does not contain NextToken
    subscriptions_processed = len(result['Subscriptions']) + subscriptions_processed


print("Number of subscriptions: %d" % (subscriptions_processed))
