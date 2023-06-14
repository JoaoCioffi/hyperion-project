import pandas as pd

def tablesGenerator(filename='rawData.csv'):

    # loading dataset from a .csv file (raw)
    df_raw = pd.read_csv(
        './data_source/' + filename,
        encoding='utf-8',
        delimiter=';'
        )

    # creating specific datasets for DynamoDB tables
    TB_REGISTRO = df_raw[
        [
            'NUM_BO','ANO_BO','DATAOCORRENCIA',
            'HORAOCORRENCIA','PERIDOOCORRENCIA','DATACOMUNICACAO',
            'DATAELABORACAO','FLAGRANTE','EXAME',
            'SOLUCAO','STATUS'
        ]
    ]

    TB_ENDERECO = df_raw[
        [
            'NUM_BO','LOGRADOURO','NUMERO',
            'BAIRRO','CIDADE','UF',
            'DESCRICAOLOCAL','DELEGACIA_NOME'
        ]
    ]

    TB_VITIMA = df_raw[
        [
            'NUM_BO','TIPOPESSOA','VITIMAFATAL',
            'NACIONALIDADE','SEXO','DATANASCIMENTO',
            'IDADE'
        ]
    ]

    TB_TELEFONE = df_raw[
        [
            'NUM_BO','ANO_FABRICACAO','ANO_MODELO',
            'QUANT_CELULAR','MARCA_CELULAR'
        ]
    ]

    createdTables={
        'TB_REGISTRO':TB_REGISTRO,
        'TB_ENDERECO':TB_ENDERECO,
        'TB_VITIMA':TB_VITIMA,
        'TB_TELEFONE':TB_TELEFONE
    }

    return createdTables

if __name__ == "__main__":
    tablesGenerator()