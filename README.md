### Passo a Passo

1. Instalação
    1. AWS CLI: https://aws.amazon.com/cli/
        1. `aws configure`
    1. SAM CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

1. SAM
    1. `sam init`
    1. Explorar arquivos
    1. `sam deploy --guided`
    1. Testes na API

1. Site Estático
    1. Executar template do site estático (Cloudfront + S3)
    1. Upload .html
    1. Cloudfront invalidation
    1. Testar!

1. Atualizar API
    1. Alterar template.yaml
    1. `sam deploy`
    1. Alterar URL da API no .html e invalidar
    1. Preencher dados DynamoDB
    1. Atualizar código da aplicação
    1. `sam deploy`

1. Destroy!
    1. Remover o .html do S3