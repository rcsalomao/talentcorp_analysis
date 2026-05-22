import pandas as pd
import numpy as np


def questao_11(df: pd.DataFrame):
    print(">>> Questão 11:")
    print("""
O1-OKR1: Zerar as inconsistências cadastrais até o fim do mês:
De acordo com o relatório de limpeza, foram encontradas diversas inconsistências cadastrais no dataset.
A maior parte das inconsistências estão presentes nos dados de 'nome', 'cpf' e 'data_admissao'.
Para devida correção, entende-se que seja necessário uma padronização e definição de protocolo uniforme para a inserção e registro de informações.
Neste sentido, pode-se fazer uso de treinamento dos funcionários responsáveis e/ou uso de plataformas e programas que já fazem a devida verificação no ponto de inserção.""")
    print("""
O2-OKR1 : Atingir 70% dos funcionários em regime CLT:
O percentual atual de funcionários em regime CLT é de 65%.
Entendo que, com uma reestruturação, seja possível alcançar o valor alvo e, portanto, a empresa está bem encaminhada.
Considerando o outro objetivo de redução de funcionários de TI sob regime PJ (O2-OKR2), a efetivação de 2 destes funcionários para o regime CLT já bastaria para alcançar este objetivo.""")
    print("""
O2-OKR2 : Reduzir PJs no TI de 4 para 2:
Atualmente são 4 funcionários de TI sob regime PJ.
Este OKR representa uma redução de 50% do regime de PJs no setor de TI, mas equivale a apenas 2 funcionários.
O importante é que a realização deste OKR também vai de encontro com o objetivo O2-OKR1, aumentando a proporção total de funcionários sob regime CLT.
O quão crítico este OKR é, vai depender do prazo restante para realizar a redução e viabilidade/facilidade na transição de regimes.""")
    print("""
O3-OKR1 : Reduzir custo do Comercial em 15%:
Por meio do dataset é possível constatar que o departamento Comercial possui uma folha salarial total de R$ 22.400,00 correspondente à menor folha de todos os departamentos encontrados.
O setor Comercial é composto por 1 gestor, 3 analistas e mais 1 estagiário.
O valor da redução de custo de 15% desejada sobre a folha é de R$ 3.360,00.
Levando-se em consideração a folha de pagamento, uma das alternativas seria a redução de 1 posto de analista comercial.
Outra alternativa seria efetuar reestruturação no cargo de gerência promovendo esta redução, conjuntamente ou não com redução do posto de estagiário.
Entretanto, deve-se sempre atentar às necessidades reais da empresa sobre o setor do comercial.""")
    salarios_comercial = df.query("cargo == 'Analista Comercial'")["salario_num"].values
    salarios_comercial_mean = salarios_comercial.mean()
    print(f"""
O3-OKR2 : Nivelar salários dos Analistas Comerciais dentro de ±10%:
Os valores salariais para os analistas comerciais são de: {salarios_comercial}.
Com o valor médio salarial de: {salarios_comercial_mean}.
Portanto, a diferença percentual dos valores salariais para sua média é de: {np.round((salarios_comercial - salarios_comercial_mean) / salarios_comercial_mean * 100, 2)}.
Considerando o valor alvo de ±10% para nivelação, entende-se que este OKR já está atendido.""")
    print()


def questao_12(df: pd.DataFrame):
    print(">>> Questão 12:")
    print("""\
Como já descrito, o objetivo O3-OKR2 já está contemplado.
Neste sentido, entendo que é mais interessante adereçar os OKRs mais próximos de serem completados de tal maneira que seriam os objetivos O2-OKR1 e O2-OKR2.
Com a conclusão do objetivo O2-OKR2, já se contempla automaticamente o objetivo O1-OKR1.
Na sequência, tendo em vista o curto prazo para a rodada de investimento, deve-se focar na questão de correção e consistência das informações cadastrais.
Esta exigiria treinamento dos funcionários responsáveis pela entrada dos dados e/ou uso de plataformas e metodologias de trabalho apropriadas que garantiriam a correta validação e inserção das futuras informações.
Por fim há o objetivo sobre redução de custos com o departamento Comercial.
As possíveis alternativas, não exaustivas, já foram descritas anteriormente, com a decisão final delegada à parte responsável levando em consideração as reais necessidades da empresa.""")
    print()
