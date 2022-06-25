#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_py_s3_01.aws_cdk_py_s3_01_stack import AwsCdkPyS301Stack


app = cdk.App()
AwsCdkPyS301Stack(app, "aws-cdk-py-s3-01")

app.synth()
