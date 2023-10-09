Disponível em: https://www.kaggle.com/competitions/desafio-visagio-2023-analytics

# Desafio Visagio 2023 - Analytics
> Treine suas técnicas e habilidades de modelagem de dados com um desafio de previsão de abandono escolar!

## Overview

Bem-vindos ao Desafio Visagio 2023 para Analytics e Data Science!

Ficamos super felizes com a participação de vocês no nosso desafio! Apenas para lembrar, nessa primeira fase, teremos um desafio ao estilo de batalha de dados do Kaggle, onde as equipes participantes desenvolverão um modelo preditivo e submeterão a solução para um problema posto.

Se você é novo aqui no Kaggle, fique tranquilo! Ele é bem tranquilo! O Kaggle é uma plataforma de competição de Data Science. Nela você pode aprender bastante observando as discussões em desafios passados com muitos tutoriais, bases de dados e diferentes tipos de problemas hospedados.

## O Desafio

O objetivo dessa fase do desafio é o desenvolvimento de um modelo de previsão de abandono de alunos do instituto PROA com base em um dataset que contém informações pessoais fornecidas pelos ingressantes e dados relacionando à inscrição e início de cada um. Todos os dados são mascarados e anonimizados.

Uma aplicação para uma solução como essa é ajudar na priorização de aprovações durante a matrícula, pois as vagas são limitadas e o instituto deseja sempre minimizar a aprovação de candidatos que não vão finalizar o curso.

Será necessário que cada grupo trate e modele os dados da forma que achar mais adequada, selecione features e desenvolva uma solução que seja capaz de prever, durante a etapa de pré-matrícula e matrícula, se um aluno irá abandonar o curso no futuro. Mais detalhes sobre as informações da base de dados são fornecidas na aba de dados do desafio.

## Contexto: Instituto PROA

O Instituto PROA é uma organização que tem o objetivo de capacitar e inserir jovens de baixa renda, vindos principalmente de escolas públicas, no mercado de trabalho, por meio de desenvolvimento pessoal e profissional. Uma de suas iniciativas para atingir isso, é a Plataforma PROA, que busca educar e preparar jovens para o mercado de trabalho.

Parte do processo seletivo consiste na resposta de um formulário, com diversas informações pessoais, pelo aluno. Essas respostas são usadas para durante o processo seletivo, na tentativa de identificar alunos com uma menor propensão a abandonar o curso antes de finalizá-lo.

Portanto, um modelo que consiga prever o abandono dos alunos com acurácia, pode ser uma importante ferramenta para incrementar o processo de seleção.

## Evaluation

**1. Objetivo:** A equipe deve prever se um aluno irá abandonar o curso antes de seu término, com o valor 0 indicando o não abandono, e o valor 1 indicando o abandono.

**2. Métrica:** A pontuação é a porcentagem de alunos que a equipe previu corretamente com abandono ou não-abandono.

## Formato do Arquivo de Submissão

Você deve enviar um arquivo csv com exatamente 1.594 entradas mais uma linha de cabeçalho. Seu envio mostrará um erro se você tiver colunas extras (além de ID_Aluno e Abandono_curso) ou linhas.

A arquivo deve conter exatamente 2 colunas:

- ```ID_Aluno``` -> em qualquer ordem

- ```Abandono_curso``` -> contendo uma variável binária de predição: 1 para abandono, 0 para sem abandono

```
ID_Aluno,Abandono_curso 
1,1
2,0
3,0
4,1
etc... 
```

---

# Dataset Description

- **Dataset_Treino.csv:** Base para treino do modelo contendo todos os dados disponibilizados para os alunos e a coluna indicando se aquele aluno abandonou o curso antes de terminá-lo

- **Dataset_Resposta.csv:** Base com informações de matrículas correntes que deve ser usada para prever se os alunos irão abandonar o curso. A coluna de ID_Aluno deste dataset, junto com a coluna de Abandono_curso calculada pelo modelo desenvolvido, devem compor o arquivo de submissão.

- **Sample_Submission.csv:** Arquivo que exemplifica o formato exato que o arquivo de submissão deve ter, com as duas colunas de ID_Aluno e Abandono_curso separadas por vírgulas. Ele deve ter uma linha de cabeçalho, mais 1594 linhas contendo o ID de cada aluno no Dataset_Resposta.csv e a previsão de Abandono_curso. A coluna de Abandono_curso do Sample_Submission.csv está em branco, mas deverá ser preenchida com 1 e 0 (abandona e não abandona, respectivamente) nos arquivos de submissão das equipes.

## Descrição dos campos
Todas as colunas de Idade até Horario_Estudando são fornecidas pelo aluno ao preencher o formulário de inscrição no curso. Por isso, podem haver campos em branco ou com preenchimento inesperado nos datasets.

- **ID_Aluno:** Número de identificação de cada aluno. Será a chave usada para relacionar a previsão do arquivo resposta
Idade: Idade do aluno no momento da matrícula
- **Tipo_escola:** Tipo de escola/faculdade em que ele estuda ou estudou
- **Escolaridade:** Nível de escolaridade e status atual
- **Estado:** Estado de residência do aluno
- **Municipio:** Município de residência do aluno
- **Trabalhando:** Se está trabalhando atualmente
- **Estudando:** Se está estudando atualmente
- **Concluiu_EAD:** Se já conclui curso à distância alguma vez e de que forma estudou à distância
- **Aprender_EAD:** Capacidade que aluno julga ter de aprender com EAD (Educação à Distância)
- **Recursos:** Quais recursos o aluno tem disponível individualmente ou em sua casa para estudar à distância
- **Disponibilidade_Tutoria:** Disponibilidade declarada para participar das tutorias. Tutorias são sessões presenciais que acontecem ao longo do curso, sendo 12 no total. Não é obrigatória a participação em todas, mas é altamente recomendável que cada aluno participe de boa parte delas.
- **Disponibilidade_3_Meses:** Disponibilidade declarada de esperar os 3 meses de curso antes de procurar um novo ou um outro emprego
- **Pessoas_Casa:** Quantas pessoas residem na mesma casa que o aluno mora
- **Renda_Familiar:** Renda familiar, estimada pelo aluno
- **Conheceu_PROA:** Canal pelo qual conheceu o PROA
- **Horario_Estudando:** Qual período do dia a pessoa está estudando. Há opção para quem não está mais estudando

As colunas a partir de Data_Inscrição são fornecidas e calculadas pela administração do Processo Seletivo do PROA.

- **Data_Inscrição:** Data na qual o aluno fez a inscrição para participar do curso
- **Dias_Espera_Aprovacao:** Dias de espera entre a data da inscrição e da aprovação no Processo Seletivo
- **Dias_Espera_Inicio:** Dias de espera entre a data da inscrição e de início do curso
- **Abandono_curso:** Variável resposta presente apenas no dataset de treinamento. Indica se aquele aluno abandonou o curso antes do fim