#!/bin/sh
#touch $( date '+%Y-%m-%d_%H-%M-%S' )_ec2.txt
aws_region=$1
echo The region is $aws_region
curl https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/20201203195321/$aws_region/index.csv | grep 'db.t3' >> $( date  +"%Y-%m-%dT%H%M")_ec2.txt
#date +"%Y-%m-%dT%H%M"

