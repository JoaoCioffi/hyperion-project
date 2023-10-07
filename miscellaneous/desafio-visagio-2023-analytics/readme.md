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

