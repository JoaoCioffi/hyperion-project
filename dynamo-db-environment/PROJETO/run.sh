# depois do término do processo de main.py (isto é, geração das tabelas e inserção dos dados),
# podemos rodar esse arquivo bash ou simplesmente replicar os comandos no terminal (Linux)
# estrutura padrão de comandos via AWS-CLI: aws dynamodb <command> --endpoint-url http://localhost:8000

# documentação jq: https://jqlang.github.io/jq/
# jq is a lightweight and flexible command-line JSON processor.
# jq is like sed for JSON data - you can use it to slice and filter
# and map and transform structured data with the same ease that sed,
# awk, grep and friends let you play with text.

# 1. Listar as tabelas para confirmar a existência das mesmas
aws dynamodb list-tables \
    --endpoint-url http://localhost:8000

# 2. Informar a quantidade total de boletins de ocorrência registrados:
aws dynamodb describe-table \
    --table-name TB_REGISTRO \
    --query 'Table.ItemCount' \
    --endpoint-url http://localhost:8000

# 3. Informar os modelos de celulares mais roubados:
aws dynamodb scan \
    --table-name TB_TELEFONE \
    --projection-expression "MARCA_CELULAR" \
    --endpoint-url http://localhost:8000 \
    | jq '[.Items[].MARCA_CELULAR.S] | group_by(.) | map({ "Modelo": .[0], "Total de Ocorrências": length }) | sort_by(-."Total de Ocorrências") | .[:10]'

# 4. Informar qual bairro possui o maior índice de assalto:
aws dynamodb scan \
    --table-name TB_ENDERECO \
    --projection-expression "BAIRRO" \
    --endpoint-url http://localhost:8000 \
    | jq '[.Items[].BAIRRO.S] | group_by(.) | map({ "Bairro": .[0], "Total de Ocorrências": length }) | sort_by(-."Total de Ocorrências") | .[0]'

# 5. Informar quais são os períodos de ocorrências mais frequentes (manhã, tarde, noite):
aws dynamodb scan \
    --table-name TB_REGISTRO \
    --projection-expression "PERIDOOCORRENCIA" \
    --endpoint-url http://localhost:8000 \
    | jq '[.Items[].PERIDOOCORRENCIA.S] | group_by(.) | map({ "Período de Ocorrência": .[0], "Total de Ocorrências": length })'

# 6. Informar a quantidade de registros de vítimas fatais:
aws dynamodb scan \
    --table-name TB_VITIMA \
    --projection-expression "VITIMAFATAL" \
    --endpoint-url http://localhost:8000 \
    | jq '[.Items[].VITIMAFATAL.S] | map(select(. == "Sim")) | length'

# 7. Informar qual cidade possui o maior índice de assalto:
aws dynamodb scan \
    --table-name TB_ENDERECO \
    --projection-expression "CIDADE" \
    --endpoint-url http://localhost:8000 \
    | jq '[.Items[].CIDADE.S] | group_by(.) | map({Cidade: .[0], "Total de Ocorrências": length}) | sort_by(-."Total de Ocorrências") | .[0]'

# 8. Informar qual dia do mês houve o maior número de assaltos:
aws dynamodb scan \
    --table-name TB_REGISTRO \
    --projection-expression "DATAOCORRENCIA" \
    --endpoint-url http://localhost:8000 \
    | jq '[.Items[].DATAOCORRENCIA.S] | map(. / "/") | map(split("-")[1]) | group_by(.) | map({Dia: .[0], "Total de Ocorrências": length}) | sort_by(-."Total de Ocorrências") | .[0]'