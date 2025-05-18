 # Meu primeiro projeto Pulumi 

 Esse projeto foi inteiramente construído seguindo apenas a documentação oficial da Pulumi <https://www.pulumi.com/docs/iac/get-started/>, que usa uma S3 como exemplo, porém adaptei para VPC.
 
 Neste projeto eu apenas configuro minha máquina para conseguir fazer o deploy de uma VPC em minha conta pessoal da AWS usando o Pulumi com Python.

 ## O que eu precesei configurar previamente na minha máquina e conta AWS:

 - Na minha conta AWS eu criei um usuário específico para o caso, com as permissões limitadas ao necessário
 - Na minha máquina eu instalei as dependências:
   - python
   - pulumi
   - pip
   - AWS CLI (e configurei com o user criado para o caso)
 - Por fim, configurei uma venv. (Quando dei o comando de deploy me apareceu um erro pedindo instalação de alguns pacotes, segui a instrução do erro e deu certo.)

 Pronto!
 O passo a passo até o deploy consta na documentação oficial.

 ---

 # AWS Python Vpc Pulumi Template

 A minimal Pulumi template for provisioning a single AWS VPC using Python.

 ## Overview

 This template provisions an VPC in your AWS account and exports its ID as an output. It’s an ideal starting point when:
  - You want to learn Pulumi with AWS in Python.
  - You prefer a minimal template without extra dependencies.

 ## Prerequisites

 - An AWS account with permissions to create VPC.
 - AWS credentials configured in your environment (for example via AWS CLI or environment variables).
 - Python 3.6 or later installed.
 - Pulumi CLI already installed and logged in.

 ## Getting Started

 1. Generate a new project from this template:
    ```bash
    pulumi new aws-python
    ```
 2. Follow the prompts to set your project name and AWS region (default: `us-east-1`).
 3. Change into your project directory:
    ```bash
    cd <project-name>
    ```
 4. Preview the planned changes:
    ```bash
    pulumi preview
    ```
 5. Deploy the stack:
    ```bash
    pulumi up
    ```
 6. Tear down when finished:
    ```bash
    pulumi destroy
    ```

 ## Project Layout

 After running `pulumi new`, your directory will look like:
 ```
 ├── __main__.py         # Entry point of the Pulumi program
 ├── Pulumi.yaml         # Project metadata and template configuration
 ├── requirements.txt    # Python dependencies
 └── Pulumi.<stack>.yaml # Stack-specific configuration (e.g., Pulumi.dev.yaml)
 ```

 ## Configuration

 This template defines the following config value:

 - `aws:region` (string)
   The AWS region to deploy resources into.
   Default: `us-east-1`

 View or update configuration with:
 ```bash
 pulumi config get aws:region
 pulumi config set aws:region us-west-2
 ```

 ## Outputs

 Once deployed, the stack exports:

 - `bucket_name` — the ID of the created S3 bucket.

 Retrieve outputs with:
 ```bash
 pulumi stack output bucket_name
 ```

 ## Next Steps

 - Customize `__main__.py` to add or configure additional resources.
 - Explore the Pulumi AWS SDK: https://www.pulumi.com/registry/packages/aws/
 - Break your infrastructure into modules for better organization.
 - Integrate into CI/CD pipelines for automated deployments.

 ## Help and Community

 If you have questions or need assistance:
 - Pulumi Documentation: https://www.pulumi.com/docs/
 - Community Slack: https://slack.pulumi.com/
 - GitHub Issues: https://github.com/pulumi/pulumi/issues

 Contributions and feedback are always welcome!