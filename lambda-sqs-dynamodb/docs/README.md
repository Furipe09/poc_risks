# Amazon SQS para AWS Lambda com Terraform

O modelo Terraform implanta uma função Lambda, uma fila SQS e as permissões IAM necessárias para executar o aplicativo. A função Lambda publica uma mensagem na fila SQS quando invocada.

Saiba mais sobre esse padrão em Serverless Land Patterns: [serverlessland.com/patterns/sqs-lambda](https://serverlessland.com/patterns/sqs-lambda)
https://github.com/aws-samples/serverless-patterns/blob/main/lambda-sqs-terraform/src/app.js

Importante: este aplicativo usa vários serviços da AWS e há custos associados a esses serviços após o uso do nível gratuito - consulte o [AWS Pricing page](https://aws.amazon.com/pricing/) para detalhes. Você é responsável por quaisquer custos da AWS incorridos. Nenhuma garantia está implícita neste exemplo.

## Requisitos

* [Criar uma conta da AWS](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) Se você ainda não tiver um, faça login. O usuário do IAM que você usa deve ter permissões suficientes para fazer as chamadas de serviço necessárias da AWS e gerenciar os recursos da AWS.

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) instalado e configurado
* [Git Instalado](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) com a versão 1.x instalada (este padrão foi testado com a versão 1.1.7)

## Instruções de implantação

1. Crie um novo diretório, navegue até esse diretório em um terminal e clone o repositório GitHub:
    ```
    git clone https://github.com/...
    ```
2. Altere o diretório para o diretório padrão:
    ```
    cd lambda-sqs-terraform-python
    ```
3. Na linha de comando, use o Terraform para implantar os recursos da AWS para o padrão conforme especificado no arquivo main.tf:
    ```
    terraform init
    terraform apply --auto-approve
    ```

4. Observe as saídas do processo de implantação do Terraform. Estes contêm os nomes de recursos e/ou ARNs que são usados ​​para teste.

## Payload de exemplo do SQS para o Lambda

```
{                                                                                                                   
    "Messages": [
        {
            "MessageId": "12345678-876d-41f7-b32c-1234567890",
            "ReceiptHandle": "AQEBZfn1234567890O78Kn0C1234567890/z1+1234567890f2bQYOvD9RL1234567890Srr7+XQ/U1234567890j7nL+uaDVnJL1234567890mASoiwI/yQ1234567890gv/h17BW12345678908Pry0JM1234567890DfHE1g1234567890aMisj1234567890M+rC+ZF21234567890QdQpEwrX01234567890Fw6w2+Po0OA1234567890DkKgGuEmebp1234567890w7nNXujzSnzIXj1234567890CqfDOb2D1234567890kCk841+01234567890OaYzXV1234567890C+ruRXj1234567890AR5+vj8+U1234567890SJplJLjd1234567890YWV8o1234567890gJXb12345678901234567890",
            "MD5OfBody": "1234567890eb64e60d1234567890",
            "Body": "Message at Wed Feb 10 2021 13:47:31 GMT+0000 (Coordinated Universal Time)"
        }
    ]
}

```

## Testando

Use a [AWS CLI](https://aws.amazon.com/cli/) para invocar a função Lambda. O nome da função está nas saídas da implantação do Terraform (a chave é QueuePublisherFunction

1. Envie a mensagem ao SQS:
```bash
aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME response.json
```
2. Recupere a mensagem da fila SQS, usando o URL da fila das saídas de implantação do Terraform:
```bash
aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
```

## Limpar

1. Altere o diretório para o diretório padrão:
    ```bash
    cd lambda-send-sqs-terraform-python&\infra

    ```

2. Excluir a stack
    ```bash
    terraform destroy --auto-approve
    ```

3. Confirme se todos os recursos criados foram excluídos
   ```bash
   terraform show
   ```