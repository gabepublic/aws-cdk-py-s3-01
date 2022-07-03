import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_cdk_py_s3_01.aws_cdk_py_s3_01_stack import AwsCdkPyS301Stack


################################################################################
#
# API docs:
# aws_cdk.assertions : 
#    https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/README.html
# aws_cdk.assertions.Match :
#    https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Match.html 
# aws_cdk.assertions.Template : 
#    https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
#
################################################################################

# Test S3 bucket is created
def test_s3_bucket_created():
    app = core.App()
    stack = AwsCdkPyS301Stack(app, "aws-cdk-py-s3-01")
    template = assertions.Template.from_stack(stack)
    # One bucket has been created
    template.resource_count_is("AWS::S3::Bucket", 1)


# The bucket was configured with:
#     removal_policy = RemovalPolicy.DESTROY,
#     auto_delete_objects = True
# Test removal-policy
def test_s3_bucket_prop_tag_removalpolicy():
    app = core.App()
    stack = AwsCdkPyS301Stack(app, "aws-cdk-py-s3-01")
    template = assertions.Template.from_stack(stack)

    template.has_resource("AWS::S3::Bucket", 
      {
        "DeletionPolicy": "Delete"
      }
    )


# The bucket was configured with:
#     removal_policy = RemovalPolicy.DESTROY,
#     auto_delete_objects = True
# Test auto-delete-objects
def test_s3_bucket_prop_tag_autodeleteobj():
    app = core.App()
    stack = AwsCdkPyS301Stack(app, "aws-cdk-py-s3-01")
    template = assertions.Template.from_stack(stack)
    # NOTE: the inconsistency; bucket was setup using underscore attribute
    # (i.e., auto_delete_objects) but the tag was setup using dash
    # (i.e., auto-delete-objects)
    template.has_resource_properties("AWS::S3::Bucket", 
      {
        "Tags": [
          {
            "Key": "aws-cdk:auto-delete-objects",
            "Value": "true"
          }
        ]
      }
    )


# The bucket was configured with:
#     block_public_access=s3.BlockPublicAccess.BLOCK_ALL
# Test block-public-access; or blobk all public access
def test_s3_bucket_prop_tag_blockpublicaccess():
    app = core.App()
    stack = AwsCdkPyS301Stack(app, "aws-cdk-py-s3-01")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::S3::Bucket", 
      {
        "PublicAccessBlockConfiguration": assertions.Match.object_like({
          "BlockPublicPolicy": True
        })
      })
