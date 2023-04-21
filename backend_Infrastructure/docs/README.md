# Amazon SQS para AWS Lambda com Terraform

Este repositório cria uma tabela Dynamodb, uma fila SQS.

Importante: este repositório usa vários serviços da AWS e há custos associados a esses serviços após o uso do nível gratuito - consulte o [AWS Pricing page](https://aws.amazon.com/pricing/) para detalhes. Você é responsável por quaisquer custos da AWS incorridos. Nenhuma garantia está implícita neste exemplo.

## Pré Requisitos

* [Criar uma conta da AWS](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) Se você ainda não tiver um, faça login. O usuário do IAM que você usa deve ter permissões suficientes para fazer as chamadas de serviço necessárias da AWS e gerenciar os recursos da AWS.

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) instalado e configurado
* [Git Instalado](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) com a versão 1.x instalada (este padrão foi testado com a versão 1.1.7)

## Instruções de implantação

1. Crie um novo diretório, navegue até esse diretório em um terminal e clone o repositório GitHub:

    ```bash
    git clone https://github.com/Furipe09/poc_risks.git
    ```

2. Altere o diretório para o diretório padrão:

    ```bash
    cd poc_risks/backend-infrastructure/infra
    ```

3. Opcional - Caso ache necessario, as variaveis de entradas podem ser alteradas no arquivo poc_risks/backend_infrastructure/infra/terraform.vars
<br>
4. Na linha de comando, use o Terraform para implantar os recursos da AWS para o padrão conforme especificado nos arquivos dynamodb.tf e sqs.tf:

    ```bash
    terraform init
    terraform apply --auto-approve
    ```

5. Observe as saídas do processo de implantação do Terraform. Estes contêm os nomes de recursos e/ou ARNs que são usados ​​para teste.

## Excluir recursos

1. Excluir a stack - Dentro da pasta infra:

    ```bash
    terraform destroy --auto-approve
    ```
