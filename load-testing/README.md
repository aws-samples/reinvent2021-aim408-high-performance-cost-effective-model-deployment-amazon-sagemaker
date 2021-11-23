# Deploying CloudWatch dashboard using CloudFormation
[![launch_stack](../images/LaunchStack.jpg)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://raw.githubusercontent.com/aws-samples/reinvent2021-aim408-achieve-high-performance-cost-effective-model-deployment-amazon-sagemaker/main/multi-model-endpoint/cloudformation/create-cw-dashboard.yaml)

^^ *Note the URL above is not working until the repo is created.*

1. In the **Specify template** section, choose Next.
1. In the **Specify stack details** section, for **Stack name**, enter a name and choose **Next**.
1. In the **Configure stack options** section, choose **Next**.
1. In the **Review** section, select **I acknowledge that AWS CloudFormation might create IAM resources** and choose **Next**.
1. When the stack status changes to `CREATE_COMPLETE`, go to the **Resources** tab to find the dashboard created.

Alternatively, you can create the stack using AWS Command Line Interface (AWS CLI).

```shell
aws cloudformation create-stack --stack-name cw-dashboard \
     --template-body file://../cloudformation/create-cw-dashboard.yml \
     --parameters ParameterKey=EndpointC5XL,ParameterValue={endpoint_name} \
                  ParameterKey=EndpointC52XL,ParameterValue={endpoint_name_2}
```
You will get a response like below.
```
{
    "StackId": "arn:aws:cloudformation:<region>:<account-id>:stack/cw-dashboard/5616f040-4255-11ec-8b9b-12e592422393"
}
```

The CloudWatch dashboard has a name like **MMECloudWatchDashboard-xxxxxxxxx**.

# [Load testing dashboards in Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#dashboards:name=mme-load-testing-combined;expand=true;autoRefresh=60;start=PT15M)