from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_s3 as s3
)

################################################################################
#
# API docs:
# AWS CDK Python Reference:
#     https://docs.aws.amazon.com/cdk/api/v2/python/index.html
# AWS aws_cdk.aws_s3:
#     https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3.html
# PyPi aws-cdk.aws-s3: 
#     https://pypi.org/project/aws-cdk.aws-s3/
#   NOTE: need to figure out the difference between AWS and PyPi!!!
#         this tutorial use PyPi.
################################################################################

class AwsCdkPyS301Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create bucket: no encryption, retain bucket during dismantling
        # bucket = s3.Bucket(self, "aws-cdk-py-s3-01-retain-20220624-gabepublic")
        # the above is equivalent to the following default:
        # {removalPolicy: cdk.RemovalPolicy.RETAIN,}
        
        # create bucket: no encryption, auto delete objects in the bucket, and
        # the bucket during dismantling
        bucket = s3.Bucket(self, "aws-cdk-py-s3-01-destroy-20220624-gabepublic",
                  removal_policy = RemovalPolicy.DESTROY,
                  auto_delete_objects = True,
                  block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
        

