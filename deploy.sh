#!/bin/bash

docker build -t clean-sns .
for index in {1..5}
do
    while IFS= read -r edition; do
        docker run --name "clean-$edition-$index" -d -e ARN=arn:aws:sns:eu-west-1:512347748389:upday_prod_pusher_editions_$edition-$index -e AWS_ACCESS_KEY_ID=$1 -e AWS_SECRET_ACCESS_KEY=$2 clean-sns;
    done <./editions.properties
done
