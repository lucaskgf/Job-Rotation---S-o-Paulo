#lucaskgf

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;



import json

faturamento_diario = [1000.00, 1500.00, 800.00, 0.00, 1200.00, 0.00, 2000.00, 900.00, 1100.00, 1300.00, 1400.00, 600.00, 0.00, 1700.00, 1800.00, 900.00, 0.00, 1400.00, 1200.00, 1100.00, 900.00, 1000.00, 800.00, 1500.00, 1700.00, 2000.00, 1200.00, 1400.00, 1600.00]

menor_valor = min(faturamento_diario)

maior_valor = max(faturamento_diario)

dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = len([valor for valor in faturamento_diario if valor > media_mensal])

dados_mensais = {}
for dia, valor in enumerate(faturamento_diario, start=1):
    dados_mensais[f'Dia {dia}'] = valor

resultados = {
    'menor_valor': menor_valor,
    'maior_valor': maior_valor,
    'dias_acima_da_media': dias_acima_da_media,
    'dados_mensais': dados_mensais
}


with open('resultados.json', 'w') as arquivo_json:
    json.dump(resultados, arquivo_json)