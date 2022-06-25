# aws-cdk-py-s3-01

Using AWS CDK Python to create S3 bucket

## Generate the project
- Prerequisite
  - [Node.js & NPM](https://heynode.com/tutorial/install-nodejs-locally-nvm/) 
  - Python - pre-installed with Ubuntu
  - PIP 
    ```
    apt install python3-pip
    ```
  - Python virtual environment
    ```
    apt install python3-virtualenv
    ```
  - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- Configure CDK default region in the `~/.aws/config` file
```
[default]
region=us-west-2
```

- Configure CDK credential `~/.aws/credential` file. The IAM user credential
  to be used for deploying to AWS. Also see "Set Policy" below, if the user
  does not belong to the Administrator group.  
```
[default]
aws_access_key_id=AKIAI44QH8DHBEXAMPLE
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
```

- [Skip] This repo contains artifacts generated by the following codes:
```
$ cd ~/projects
$ mkdir aws-cdk-py-s3-01
$ cd aws-cdk-py-s3-01
$ cdk init sample-app --language python
```

- Create python virtual environment
```
$ virtualenv .venv
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
```

- CDK Bootstrap; if not already done on the account previously 
```
// Get acct-number from AWS console or
$ aws sts get-caller-identity
// Get the default region for the profile
$ aws configure get region

$ cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

- Set Policy; the policies are needed for CloudFormation & S3.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "cloudformation:DescribeStacks",
                "cloudformation:CreateChangeSet",
                "cloudformation:DescribeChangeSet",
                "cloudformation:ExecuteChangeSet",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DeleteChangeSet",
                "cloudformation:DeleteStack",
                "cloudformation:GetTemplate",
                "s3:CreateBucket"
            ],
            "Resource": "*"
        }
    ]
}
```

- Build
```
$ cdk synth
```

- Deploy
```
$ cdk deploy
```

- Destroy; see the `..\aws-cdk-py-s3-01\aws_cdk_py_s3_01\aws_cdk_py_s3_01_stack.py`
  for whether to delete S3 bucket during dismantling. 
```
cdk destroy
```

Output:
```
✨  Synthesis time: 10.26s

This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
Please confirm you intend to make the following modifications:

IAM Statement Changes
┌───┬───────────────────────────────────┬────────┬───────────────────────────────────┬───────────────────────────────────┬───────────┐
│   │ Resource                          │ Effect │ Action                            │ Principal                         │ Condition │
├───┼───────────────────────────────────┼────────┼───────────────────────────────────┼───────────────────────────────────┼───────────┤
│ + │ ${Custom::S3AutoDeleteObjectsCust │ Allow  │ sts:AssumeRole                    │ Service:lambda.amazonaws.com      │           │
│   │ omResourceProvider/Role.Arn}      │        │                                   │                                   │           │
├───┼───────────────────────────────────┼────────┼───────────────────────────────────┼───────────────────────────────────┼───────────┤
│ + │ ${MyCdkSample01Bucket-20220624-dz │ Allow  │ s3:DeleteObject*                  │ AWS:${Custom::S3AutoDeleteObjects │           │
│   │ ong.Arn}                          │        │ s3:GetBucket*                     │ CustomResourceProvider/Role.Arn}  │           │
│   │ ${MyCdkSample01Bucket-20220624-dz │        │ s3:List*                          │                                   │           │
│   │ ong.Arn}/*                        │        │                                   │                                   │           │
└───┴───────────────────────────────────┴────────┴───────────────────────────────────┴───────────────────────────────────┴───────────┘
IAM Policy Changes
┌───┬───────────────────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────┐
│   │ Resource                                                      │ Managed Policy ARN                                             │
├───┼───────────────────────────────────────────────────────────────┼────────────────────────────────────────────────────────────────┤
│ + │ ${Custom::S3AutoDeleteObjectsCustomResourceProvider/Role}     │ {"Fn::Sub":"arn:${AWS::Partition}:iam::aws:policy/service-role │
│   │                                                               │ /AWSLambdaBasicExecutionRole"}                                 │
└───┴───────────────────────────────────────────────────────────────┴────────────────────────────────────────────────────────────────┘
(NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

Do you wish to deploy these changes (y/n)? y
aws-cdk-py-s3-01: deploying...
```

## Original Doc

### Welcome to your CDK Python project!

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`aws_cdk_py_s3_01_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

### Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
