# opsgenie-systems-manager-documents
AWS Systems Manager scripts to automate alert API actions in Atlassian Opsgenie.

You can use the files `create_alert_document.json` and `close_alert_document.json` to create Automation Documents within AWS Systems Manager.

Documents essentially create a CloudFormation stack with an IAM Role and a Lambda function then execute the function with the role and given parameters. Executing the document itself requires following permissions:

```json
[
    "iam:GetRole",
    "iam:PassRole",
    "iam:CreateRole",
    "iam:DeleteRole",
    "lambda:CreateFunction",
    "lambda:InvokeFunction",
    "lambda:GetFunction",
    "lambda:InvokeAsync",
    "lambda:DeleteFunction"
]
```

The IAM role created for the Lambda function only contains `sts:AssumeRole`, which is required to invoke the function. After document executes all created resources are cleaned up.

To view non-minified versions of the CloudFormation stack document and Lambda python scripts, refer to `*_alert_stack.json` and `*_alert_lambda.py` files. 