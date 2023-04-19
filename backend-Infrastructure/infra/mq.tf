# resource "aws_mq_configuration" "mq_config" {
#   count          = var.create_mq ? 1 : 0
#   description    = var.mq_conf_description
#   name           = var.mq_conf_name
#   engine_type    = var.mq_conf_engine_type
#   engine_version = var.mq_conf_engine_version

#   data = <<DATA
# <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <broker xmlns="http://activemq.apache.org/schema/core">
#   <plugins>
#     <forcePersistencyModeBrokerPlugin persistenceFlag="true"/>
#     <statisticsBrokerPlugin/>
#     <timeStampingBrokerPlugin ttlCeiling="86400000" zeroExpirationOverride="86400000"/>
#   </plugins>
# </broker>
# DATA
# }

# resource "aws_mq_broker" "one" {
#   count       = var.create_mq ? 1 : 0
#   broker_name = var.mq_broker_name

#   configuration {
#     id       = aws_mq_configuration.mq_config[0].id
#     revision = aws_mq_configuration.mq_config[0].latest_revision
#   }

#   engine_type        = var.broker_engine_type
#   engine_version     = var.broker_engine_version
#   host_instance_type = var.mq_host_instance_type
#   # security_groups    = [aws_security_group.allow_tls.id]

#   user {
#     username = var.mq_username
#     password = var.mq_password
#   }
# }
