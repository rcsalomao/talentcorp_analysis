# Análise de Dados: TalentCorp

Neste repositório consta a análise de dados do dataset referente à empresa fictícia TalentCorp, como exercício prático do curso de análise de dados do SCTEC.
Trata-se da análise e considerações à cerca das questões propostas no documento de instrução `./briefing/TalentCorp_ALUNO.docx`.

A primeira parte corresponde às rotinas de ingestão, tratamento e limpeza dos dados brutos, encontradas no arquivo `./src/data_ingestion.py` e posterior escrita dos dados limpos por meio das rotinas encontradas em `./src/data_writing.py`.

Por fim, as questões propostas pelo documento de instrução são respondidas pelas respectivas rotinas encontradas nos arquivos `./src/parte_A_qualidade_dados.py`, `./src/parte_B_KPI.py`, `./src/parte_C_OKR.py`, `./src/parte_D_analise_propostas.py`.

## Requisitos

Este repositório faz uso das seguintes bibliotecas:

- pandas
- numpy

Por favor, instale-as previamente.

## Uso

O ponto de entrada do algoritmo para análise é o arquivo `./main.py`.
Basta, portanto, executar o respectivo arquivo pelo interpretador à partir da pasta raiz do projeto.

## Resultados

A execução do algoritmo resulta na exposição das respostas do projeto no stdout do terminal, além do arquivo `./data/output/funcionarios_clean.csv` que representa o dataset processado e limpo em formato `csv`.

Segue adiante o texto resultante da análise:

<style>
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
</style>

```
=== RELATÓRIO DE LIMPEZA ===
Total de funcionários: 20
Emails inválidos: 4
CPFs que precisaram de regularização: 6
Datas convertidas de AAAA-MM-DD: 7
Datas convertidas de AAAA-MM-DD: 6
Telefones inválidos: 0
Telefones corrigidos: 2
              
>>> O arquivo de dataset limpo foi escrito com sucesso!
=== QUALIDADE DOS DADOS ===

>>> Questão 01: Quantos funcionários tinham e-mail inválido? Quais são eles?
Total de funcionários com email inválido: 4
Nome dos funcionários:
Carlos Eduardo Mendes
Roberto Alves
Beatriz Lima
Vanessa Oliveira

>>> Questão 02: Quantos CPFs precisaram de normalização? Liste os formatos encontrados.
Total de cpfs que foram corrigidos: 6
Formatos de cpfs incorretos encontrados:
98765432100
111-222-333/44
555666777-88
22233344455
444-555-666/77
666777888-99

>>> Questão 03: Quantos nomes tinham algum tipo de inconsistência? Quais eram os problemas mais comuns?
Total de nomes que foram corrigidos: 14
Total de nomes em maiúsculo:  7
Total de nomes em minúsculo:  6
Total de nomes com espaços em branco internamente:  3
Total de nomes com espaços em branco externamente:  2

=== ANÁLISE DOS KPIS ===

>>> Questão 04: Qual o salário médio por cargo?
O salário médio por cargo é descrito na seguinte tabela:
                        cargo  salario_medio
10              Gerente de TI   14500.000000
5     Desenvolvedor(a) Sênior   12000.000000
8          Gerente Financeiro   11000.000000
9               Gerente de RH   10500.000000
7           Gerente Comercial    9800.000000
4   Desenvolvedor(a) Pleno(a)    8350.000000
3            Desenvolvedor(a)    7200.000000
1         Analista Financeiro    5100.000000
2              Analista de RH    4333.333333
0          Analista Comercial    3800.000000
6               Estagiário(a)    1200.000000

>>> Questão 05: Qual o salário médio por departamento?
O salário médio por departamento é descrito na seguinte tabela:
  departamento  salario_medio
3           TI         8600.0
2           RH         5875.0
1   Financeiro         5500.0
0    Comercial         4480.0

>>> Questão 06: Qual departamento tem a maior folha salarial total?
A folha salarial total por departamento é descrita na seguinte tabela:
  departamento    total
3           TI  51600.0
1   Financeiro  27500.0
2           RH  23500.0
0    Comercial  22400.0

>>> Questão 07: Quantos funcionários por regime? Qual o percentual de cada um?
A quantidade de funcionários por regime é descrita na seguinte tabela:
    regime  total  percentual
0      CLT     13        0.65
1  Estágio      3        0.15
2       PJ      4        0.20

>>> Questão 08: Qual o funcionário com maior tempo de casa? (data de admissão mais antiga)
O tempo de permanência de cada funcionário é descrito na seguinte tabela:
                      nome         tempo_permanencia departamento
18        Vanessa Oliveira 4124 days 13:32:50.090048           RH
13     Diego Souza Martins 3550 days 13:32:50.090048   Financeiro
7   Thiago Oliveira Santos 3319 days 13:32:50.090048           TI
5      Pedro Augusto Nunes 3000 days 13:32:50.090048           TI
1    Carlos Eduardo Mendes 2503 days 13:32:50.090048    Comercial
3            Roberto Alves 2324 days 13:32:50.090048   Financeiro
11            Rafael Costa 2179 days 13:32:50.090048           TI
9          Marcos Teixeira 1922 days 13:32:50.090048   Financeiro
0          Ana Paula Souza 1908 days 13:32:50.090048           RH
16          Amanda Ribeiro 1634 days 13:32:50.090048           TI
2    Mariana Ferreira Lima 1588 days 13:32:50.090048           TI
19       Bruno Lima Santos 1530 days 13:32:50.090048   Financeiro
8            Lucia Menezes 1381 days 13:32:50.090048           RH
12          Camila Pereira 1298 days 13:32:50.090048    Comercial
14          Patricia Alves 1128 days 13:32:50.090048           RH
15          Lucas Ferreira 1108 days 13:32:50.090048    Comercial
4             Julia Santos 1086 days 13:32:50.090048    Comercial
6           Fernanda Rocha  994 days 13:32:50.090048    Comercial
10            Beatriz Lima  858 days 13:32:50.090048           TI
17         Henrique Castro  659 days 13:32:50.090048   Financeiro

>>> Questão 09: Quantos funcionários por departamento?
A quantidade de funcionários por departamento é descrita na seguinte tabela:
  departamento  total
3           TI      6
0    Comercial      5
1   Financeiro      5
2           RH      4

>>> Questão 10: Qual cargo tem mais funcionários?
A quantidade de funcionários por cargo é descrita na seguinte tabela:
                        cargo  total
0          Analista Comercial      3
1         Analista Financeiro      3
2              Analista de RH      3
6               Estagiário(a)      3
4   Desenvolvedor(a) Pleno(a)      2
3            Desenvolvedor(a)      1
5     Desenvolvedor(a) Sênior      1
7           Gerente Comercial      1
8          Gerente Financeiro      1
9               Gerente de RH      1
10              Gerente de TI      1

=== CONFRONTO COM OKRS ===

>>> Questão 11: Para cada KR acima, responda: a empresa está no caminho certo? Qual é o número atual vs a meta?

O1-OKR1: Zerar as inconsistências cadastrais até o fim do mês:
De acordo com o relatório de limpeza, foram encontradas diversas inconsistências cadastrais no dataset.
A maior parte das inconsistências estão presentes nos dados de 'nome', 'cpf' e 'data_admissao'.
Para devida correção, entende-se que seja necessário uma padronização e definição de protocolo uniforme para a inserção e registro de informações.
Neste sentido, pode-se fazer uso de treinamento dos funcionários responsáveis e/ou uso de plataformas e programas que já fazem a devida verificação no ponto de inserção.

O2-OKR1 : Atingir 70% dos funcionários em regime CLT:
O percentual atual de funcionários em regime CLT é de 65%.
Entendo que, com uma reestruturação, seja possível alcançar o valor alvo e, portanto, a empresa está bem encaminhada.
Considerando o outro objetivo de redução de funcionários de TI sob regime PJ (O2-OKR2), a efetivação de 2 destes funcionários para o regime CLT já bastaria para alcançar este objetivo.

O2-OKR2 : Reduzir PJs no TI de 4 para 2:
Atualmente são 4 funcionários de TI sob regime PJ.
Este OKR representa uma redução de 50% do regime de PJs no setor de TI, mas equivale a apenas 2 funcionários.
O importante é que a realização deste OKR também vai de encontro com o objetivo O2-OKR1, aumentando a proporção total de funcionários sob regime CLT.
O quão crítico este OKR é, vai depender do prazo restante para realizar a redução e viabilidade/facilidade na transição de regimes.

O3-OKR1 : Reduzir custo do Comercial em 15%:
Por meio do dataset é possível constatar que o departamento Comercial possui uma folha salarial total de R$ 22.400,00 correspondente à menor folha de todos os departamentos encontrados.
O setor Comercial é composto por 1 gestor, 3 analistas e mais 1 estagiário.
O valor da redução de custo de 15% desejada sobre a folha é de R$ 3.360,00.
Levando-se em consideração a folha de pagamento, uma das alternativas seria a redução de 1 posto de analista comercial.
Outra alternativa seria efetuar reestruturação no cargo de gerência promovendo esta redução, conjuntamente ou não com redução do posto de estagiário.
Entretanto, deve-se sempre atentar às necessidades reais da empresa sobre o setor do comercial.

O3-OKR2 : Nivelar salários dos Analistas Comerciais dentro de ±10%:
Os valores salariais para os analistas comerciais são de: [3800. 3900. 3700.].
Com o valor médio salarial de: 3800.0.
Portanto, a diferença percentual dos valores salariais para sua média é de: [ 0.    2.63 -2.63].
Considerando o valor alvo de ±10% para nivelação, entende-se que este OKR já está atendido.

>>> Questão 12: Qual KR você considera mais urgente de endereçar? Justifique com os dados.
Como já descrito, o objetivo O3-OKR2 já está contemplado.
Neste sentido, entendo que é mais interessante adereçar os OKRs mais próximos de serem completados de tal maneira que seriam os objetivos O2-OKR1 e O2-OKR2.
Com a conclusão do objetivo O2-OKR2, já se contempla automaticamente o objetivo O1-OKR1.
Na sequência, tendo em vista o curto prazo para a rodada de investimento, deve-se focar na questão de correção e consistência das informações cadastrais.
Esta exigiria treinamento dos funcionários responsáveis pela entrada dos dados e/ou uso de plataformas e metodologias de trabalho apropriadas que garantiriam a correta validação e inserção das futuras informações.
Por fim há o objetivo sobre redução de custos com o departamento Comercial.
As possíveis alternativas, não exaustivas, já foram descritas anteriormente, com a decisão final delegada à parte responsável levando em consideração as reais necessidades da empresa.

=== ANÁLISE E PROSPOSTAS ===

>>> Questão 13: Crie pelo menos 2 KPIs que você acha relevantes e que NÃO foram pedidos acima. Justifique cada um.
1º KPI: Quantidade e proporção de funcionários por nível:
Como se calcula: 'Quantidade de funcionários por nível' / 'Total de funcionários'
         nivel  total  percentual
2  Operacional     13        0.65
1    Liderança      4        0.20
0   Estagiário      3        0.15

2º KPI: Taxa média de inconsistências cadastrais:
Como se calcula: 'Somatório dos dados inconsistentes e inválidos' / 'Quantidade dos tipos de dados avaliados'
Valor para este dataset: 7.8

>>> Questão 14: Com base nos dados que você encontrou, proponha um novo OKR para o próximo trimestre. Use o formato: Objetivo + pelo menos 2 KRs mensuráveis.
"OKR: Melhoria da qualidade cadastral dos dados da empresa, por meio da redução da 'taxa média de inconsistências cadastraris'."
"Horizonte: Trimestral"
"KPI base: Minimização do 2º KPI (Taxa média de inconsistências cadastrais) apresentado anteriormente. Quanto mais próximo de 0, melhor.

>>> Questão 15: Se você fosse a Vanessa (Gerente de RH), qual seria sua prioridade nos próximos 30 dias? Justifique com dados.
Levando em considerarção as questões anteriores e o curto prazo de 30 dias para a apresentação do relatório e resultados, entendo que o amis interessante seria completar num primeiro momento os objetivos mais fáceis.
Neste primeiro momento creio que é plenamente possível realizar a execução do objetivo O1-OKR1 (zerar as inconsistências cadastrais) e iniciar os objetivos O2-OKR2 (reduzir PJs no TI de 4 para 2) e O2-OKR1 (atingir 70% dos funcionários em regime CLT).
Para o objetivo O1-OKR1, entendo que uma estratégia eficaz consiste em realizar sessões regulares de treinamento e orientação para os funcionários responsáveis pelo registro, além da definição de protocolos e métodos para a execução da tarefa, a fim de minimizar e eliminar o surgimento das inconsistências cadastrais.
Os objetivos O2-OKR1 e O2-OKR2, por sua natureza, são convergentes e portante a realização de um também implica na realização do outro.
A redução de PJs de 4 para 2 também provocará o aumento na proporção de funcionários CLT.
Creio que a dificuldade possa residir na negociação entre os respectivos funcionários e aí se encontra a incerteza sobre o prazo de execução destes objetivos.
Além destes 3 objetivos discutidos, há de se ter em mente o objetivo O3-OKR1 (redução de custo do Comercial em 15%) que envolve os respectivos funcionários e as partes responsáveis pela tomada de decisão sobre o tema e, portanto, entendo que este objetivo é o mais delicado e incerto quanto sua exequibilidade e prazo.
```
