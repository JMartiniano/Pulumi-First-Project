"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# Criar uma VPC
vpc = aws.ec2.Vpc(
    "my-vpc-pulumi",
    cidr_block="10.0.0.0/24",
    enable_dns_support=True,
    enable_dns_hostnames=True,
    tags={
        "Name": "my-vpc-pulumi"
    }
)

# Exportar o ID da VPC
pulumi.export("vpc_id", vpc.id)