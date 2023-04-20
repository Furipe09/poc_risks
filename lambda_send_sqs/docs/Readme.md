# Lambda para enviar mensagem para uma fila SQS na AWS
Esta é uma função Lambda em Python que envia uma mensagem para uma fila SQS na AWS. Ela usa a biblioteca boto3 para criar um cliente SQS e enviar uma mensagem para a fila.

# Requisitos
Antes de utilizar o código, é necessário ter os seguintes requisitos instalados:

- Python 3.x
- Biblioteca boto3
- Além disso, é necessário ter uma conta na AWS e configurar as credenciais de acesso.

# Utilização
Para utilizar o código, siga os seguintes passos:

* Clone o repositório para sua máquina local.
* Configure as credenciais de acesso à AWS.
* Configure a URL da fila SQS no arquivo infra/variables.tf.
* Siga os passos do arquivo infra/readme
* Execute a lambda no console da aws, passando parametros de json conforme o exemplo abaixo:
  ```bash
  { "userId": "2",  "name": "John Does", "email": "johndoe@example.comm" }
  ```
# Validando
A execução pode ser validada no cloudwatch logs

# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou uma issue para discutir sobre o código.

# Licença
Este código é licenciado sob a licença MIT. Consulte o arquivo LICENSE.md para mais informações.






Dessa forma, o código foi dividido em três arquivos:

sqs_message_sender.py contém a definição da classe SQSMessageSender, que é responsável por enviar mensagens para a fila do SQS.
lambda_handler.py contém a definição da classe LambdaHandler, que é responsável por gerenciar as operações do Lambda, como obter a URL da fila e enviar a mensagem para a fila.
lambda_function.py é o arquivo que será executado pelo Lambda e importa a classe LambdaHandler.
Com essa abordagem, é possível separar as responsabilidades do código e torná-lo mais modular e fácil de manter.


Nesta implementação, foram adicionados os seguintes recursos:

aws_lambda_powertools.Logger: um logger que captura informações de contexto do Lambda, como a função e a versão do Lambda, e envia logs para o CloudWatch.
aws_lambda_powertools.Tracer: um tracer que captura informações de rastreamento do X-Ray.
aws_lambda_powertools.logging.structured_logger: um logger estruturado que envia logs para o CloudWatch em formato JSON.
aws_lambda_powertools.metrics: um pacote que permite emitir métricas personalizadas para o CloudWatch.
A classe LambdaHandler foi atualizada para utilizar esses recursos. O método handle_request agora é decorado com o método logger.inject_lambda_context para capturar informações de contexto do Lambda e o método tracer.capture_lambda_handler() para capturar informações de rastreamento do X-Ray. Além disso, o método metrics.add_metric foi utilizado para registrar a quantidade de mensagens processadas.

No bloco try-except, foi adicionado o método logger.exception para registrar exceções no CloudWatch.