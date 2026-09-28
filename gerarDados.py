import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

pastaDados = Path('dados')
pastaDados.mkdir(exist_ok=True)

# Listas utilizadas para gerar os dados
unidades = [
    "Guaíba",
    "Porto Alegre",
    "Canoas",
    "Gravataí",
    "Alvorada"
]

tiposManutencao = [
    "Preventiva",
    "Corretiva",
    "Preditiva"
]

prioridades = [
    "Baixa",
    "Média",
    "Alta",
    "Crítica"
]

statusChamado = [
    "Concluído",
    "Em andamento",
    "Pendente"
]

categoriasProblema = [
    "Elétrica",
    "Mecânica",
    "Hidráulica",
    "Eletrônica",
    "Estrutural"
]

tecnicos = [
    "Técnico 01",
    "Técnico 02",
    "Técnico 03",
    "Técnico 04",
    "Técnico 05"
]

registros = []

dataInicial = datetime(2026, 1, 1)

for numero in range(1, 501):
    dataAbertura = dataInicial + timedelta (
        days=random.randint(0, 262)
    )

    tipo = random.choice(tiposManutencao)
    prioridade = random.choice(prioridades)
    status = random.choice(statusChamado)

    tempoAtendimento = round(random.uniform(0.5, 12), 2)
    tempoResolucao = round(
        tempoAtendimento + random.uniform(1, 48), 2
    )

    custo = round(random.uniform(100, 3000), 2)

    registro = {
        'idChamado': numero,
        'dataAbertura': dataAbertura.strftime('%Y-%m-%d'),
        'unidade': random.choice(unidades),
        'equipamento': f'Equioamento {random.randint(1, 100):03d}',
        'tipoManutencao': tipo,
        'prioridade': prioridade,
        'status': status,
        'tempoAtendimentoHoras': tempoAtendimento,
        'tempoResolucaoHoras': tempoResolucao,
        'tecnico': random.choice(tecnicos),
        'categoriaProblema': random.choice(categoriasProblema),
        'custo': custo
    }

    registros.append(registro)

df = pd.DataFrame(registros)

caminhoArquivo = pastaDados / 'chamadosManutencao.csv' 

df.to_csv(caminhoArquivo, index=False, encoding='utf-8-sig')

print(f"Base criada com sucesso: {caminhoArquivo}")
print(f"Quantidade de registros: {len(df)}")
print("\nPrimeiros registros:")
print(df.head())