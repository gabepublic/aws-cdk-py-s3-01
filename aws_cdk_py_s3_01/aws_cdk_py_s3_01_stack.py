from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3
)


class AwsCdkPyS301Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create bucket: no encryption, retain bucket during dismantling
        # bucket = s3.Bucket(self, "MyCdkSample01Bucket-20220624-dzong")
        # the above is equivalent to the following default:
        # {removalPolicy: cdk.RemovalPolicy.RETAIN,}
        
        # create bucket: no encryption, auto delete objects in the bucket, and
        # the bucket during dismantling
        bucket = s3.Bucket(self, "MyCdkSample01Bucket-20220624-dzong",
                  removal_policy = RemovalPolicy.DESTROY,
                  auto_delete_objects = True)
        

