# Nancian - Pacote para solução de problemas básicos de estatística

Pacote criado com a ideia de aprender sobre estatística. Utilizando de poucas funções prontas foi criado durante as aulas de estatística.

## Funções disponíveis

As funções vão sendo adicionadas com o decorrer das aulas. A lista de funções já programada está abaixo.

### Distribuição de frequências (R)

- <code>tabled</code>: Função para criar uma tabela;
- <code>frequency_simple</code>: Função para o cálculo de frequência simples;
- <code>function_acumulate</code>: Função para calcular a fruquência acumulada;
- <code>function_relative</code>: Função para cálculo de frequência relativas
- <code>function_acumulate_relative</code>: Função para cálculo de frequência acumulada relativas
- <code>visualize_table</code>: Função para visualizar a tabela
- <code>frequency_distribuition</code>: Função para realização de todos os cálculos necessários para gerar a tabela de distribuição.

### Medidas de frequência central (R)
- <code>x</code>: Função para encontrar a média aritmética simples;
- <code>md</code>: Função para encontrar a mediana;
- <code>mo</code>: Função para encontrar a moda.

### Probabilidade (R)

- <code>prob_simple</code>: Função para cálculo de probabilidade simples;
- <code>prob_sum</code>: Função para cálculo de probabilidade utilizando o teorema da soma;
- <code>prob_prod</code>: Função para cálculo de probabilidade utilizando o teorema de produto;
- <code>prob_solver</code>: Função para cálculo de probabilidade de ocorrência de certo evento, aplicando os teoremas de soma e produto.

### Correlação e regressão (Python)

- <code>Linear</code>: Classe com funcionalidades para realizar regressão linear;
- <code>Pearson</code>: Classe para cálculos da correlação de Pearson;
- <code>plot_disp</code>: Função para realizar o plot do diagrama de dispersão.

### Teste de hipótese (Python)
- <code>HypothesisTest</code>: Classe com funcionalidades para realizar testes de hipótese.

### Extras (Python)

Há ainda alguns extras para os alunos da Nanci

- Tabelas: Aqui há funções para trabalhar com as tabelas dos exercícios da Nanci
	- <code>table_five</code>: Gera tabelas dos exercícios da lista 5;
	- <code>nearest_neighbors</code>: Encontra o elemento mais próximo do inserido na tabela de distribuição normal ou tabela student. Recomenda-se o uso deste nos exercícios de teste de hipótese.

### Apresentação

Para ver a apresentação do projeto, acesse o diretório `notebooks` e digite:

<code>jupyter nbconvert Presentation.ipynb --to slides --post serve</code>

OBS: A nomenclatura foi definida seguindo alguns exercícios de aula, do curso de estatística aplicada da Fatec.

### Executando o projeto

Para executar os códigos `R`, basta ter instalado o pacote da linguagem `R` e executar os notebooks, para os códigos em Python, será necessário instalar alguns pacotes. Para isso utilize o comando abaixo:

`pip install -r requirements.txt`

Após fazer a instalação das bibliotecas necessárias, basta apenas executar `jupyter-notebook` e executar os notebooks.

### Outras implementações

Caso você prefira/precise existe também a implementação deste pacote de soluções em C/C++, o [nancia.h](https://github.com/M3nin0/nancian.h), ele ainda não possui todas as funcionalidades listadas aqui, mas pode te ajudar a resolver alguns exercícios :smile:

