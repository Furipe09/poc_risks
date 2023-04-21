# Lambda para enviar mensagem para uma fila SQS na AWS

Esta é uma função Lambda em Python que envia uma mensagem para uma fila SQS na AWS. Ela usa a biblioteca boto3 para criar um cliente SQS e enviar uma mensagem para a fila.

## Requisitos

Antes de utilizar o código, é necessário ter os seguintes requisitos instalados:

- Python 3.x
- Biblioteca boto3
- Além disso, é necessário ter uma conta na AWS e configurar as credenciais de acesso.

## Utilização

Para utilizar o código, siga os seguintes passos:

- Clone o repositório para sua máquina local.

- Configure as credenciais de acesso à AWS.

- Configure a URL da fila SQS no arquivo infra/variables.tf.

- Siga os passos do arquivo infra/readme

- Execute a lambda no console da aws, passando parametros de json conforme o exemplo abaixo:
  
  ```bash
  { "IdTransacao": "99",  "IdCliente": "99", "name": "John Does", "email": "johndoe@example.comm" }
  ```

## Validando

A execução pode ser validada no cloudwatch logs

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou uma issue para discutir sobre o código.

## Licença

Este código é licenciado sob a licença MIT. Consulte o arquivo LICENSE.md para mais informações.
