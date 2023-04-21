# Risks POC

## Este projeto tem como objetivo a validação de uma POC que deve

- Enviar mensagens a uma fila SQS atravé de uma lambda;

- Fazer o trigger de outra lambda toda as vezes que a fila sqs receber msgs novas;
  
- Capturar as mensagem de uma fila SQS em uma Lambda e grava em uma tabela DynamoDB;

### Os recursos de Infra abaixo serão criados

![poc_risk](./media/poc_risk.svg)

- DynamoDB Table;
- SQS Queue;
- Lambda - Envia mensagem ao SQS foi criada no diretório 'lambda-send-sqs';
- Lambda Event Source Mapping - obtem eventos da fila sqs para a lambda;
- Lambda - Escuta e recebe as mensagem do SQS e grava no DynamoDB está no diretório 'lambda-sqs-dynamodb';

Importante: este repositório usa vários serviços da AWS e há custos associados a esses serviços após o uso do nível gratuito - consulte o [AWS Pricing page](https://aws.amazon.com/pricing/) para detalhes. Você é responsável por quaisquer custos da AWS incorridos. Nenhuma garantia está implícita neste exemplo.

## Demo

Aqui segue o [video](https://www.loom.com/share/c13ecb64b720423b983029482789cabe) demo de implementação e execução deste projeto.

## Instruções de implantação

1. Crie um novo diretório, navegue até esse diretório em um terminal e clone o repositório GitHub:

    ```bash
    git clone https://github.com/Furipe09/poc_risks.git
    ```

2. Altere o diretório para o diretório padrão:

    ```bash
    cd poc_risks
    ```

3. **Opcional** - Caso ache necessario, altere os valores das variaveis de entradas dos 3 repositórios do terraform, conforme arquivos abaixo:
   - poc_risks/backend_infrastructure/infra/variables.tf
   - poc_risks/lambda_send_sqs/infra/variables.tf
   - poc_risks/lambda_sqs_dynamodb/infra/variables.tf

4. Na linha de comando, use o Terraform para implantar os recursos da AWS:

    - Implantação dos recursos de infraestrutura - **SQS e DynamoDB**:

    ```bash
    terraform -chdir=backend_Infrastructure/infra init

    terraform -chdir=backend_Infrastructure/infra apply -auto-approve
    ```

    - Implantação da lambda de envio de msgs ao **SQS - Lambda**:

    ```bash
    terraform -chdir=lambda_send_sqs/infra init

    terraform -chdir=lambda_send_sqs/infra apply -auto-approve
    ```

    - Implantação do service map e da lambda de recepção de msgs do SQS e envio ao DynamoDB - **Lambda e service map**:

    ```bash
    terraform -chdir=lambda_sqs_dynamodb/infra init

    terraform -chdir=lambda_sqs_dynamodb/infra apply -auto-approve
    ```

5. Observe as saídas do processo de implantação do Terraform. Estes contêm os nomes de recursos e/ou ARNs que são usados ​​para teste.

## Excluir recursos

1. Excluir a stack - Dentro da pasta infra:

    ```bash
    terraform -chdir=lambda_sqs_dynamodb/infra destroy -auto-approve
    
    terraform -chdir=lambda_send_sqs/infra destroy -auto-approve
    
    terraform -chdir=backend_Infrastructure/infra destroy -auto-approve
    ```
