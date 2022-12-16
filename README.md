# acppred

By Pedro Reisser

a tool to predict anticancer peptides

## Setup

```
$ make setup

```
command 'acppred-train' -- Treina um modelo usando dados fornecido pelo usuario, são necesarios 3 atributos, um output, uma lista de peptidios anticanceriginos e uma lista de peptidios sem potencia anticancerigino.
    output: escolhe o diretorio de saida do report da ferramenta, formato de saida '.csv'
      sintax: '--output'
    positive_peptides: entrada de uma lista de peptideos COM carecteriscas anticanceriginas, formato de entrada'.txt'
      sintax: '--positive_peptides'
    negative_peptides: entrada de uma lista de peptideos SEM carecteriscas anticanceriginas, formato de entrada'.txt'
      sintax: '--negative_peptides'
    
command 'acppred-predict' -- Utiliza o modelo criado pelo 'acppred-train' para prever a ação de um peptidio fornecido pelo usuario. Sao necessarios tres atributos, um input, um output, e um modelo.
    input: lista de peptidios a serem testados, formato '.fasta'.
      sintax: '--input'
    output: escolhe o diretorio de saida do report da ferramenta, formato de saida '.csv'.
      sintax: '--output"
    model: localização do modelo pré-treinado, caminho salvo peloa função 'acppred-train'
      sintax: '--model'
