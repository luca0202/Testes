# 3) Análise do faturamento diário
import json

# Suponha que o arquivo 'faturamento.json' contém os dados do faturamento diário
with open("json_teste_3.json", "r") as file:
    dados = json.load(file)

faturamento = [d["valor"] for d in dados if d["valor"] > 0]
menor = min(faturamento)
maior = max(faturamento)
média = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for f in faturamento if f > média)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")