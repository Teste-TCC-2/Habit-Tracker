import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta


# Lista de tarefas (nome, início, fim)
tasks = [
    ("Configurar ambiente", "2026-03-16", "2026-03-23"),
    ("Desenvolvimento do banco de dados", "2026-03-23", "2026-04-03"),
    ("Desenvolvimento da API", "2026-04-06", "2026-04-24"),
    ("Desenvolvimento do front-end", "2026-04-06", "2026-05-08"),
    ("Testes iniciais e correção de bugs", "2026-05-08", "2026-05-19"),
    ("Deploy", "2026-05-19", "2026-05-26"),
    ("Testes e validação", "2026-05-18", "2026-05-29"),
]

# Evento único
milestones = [
    ("Entrega do TCC 2", "2026-06-15")
]

# Converter datas
for i, (task, start, end) in enumerate(tasks):
    tasks[i] = (task, datetime.fromisoformat(start), datetime.fromisoformat(end))
milestones = [(m[0], datetime.fromisoformat(m[1])) for m in milestones]

# Dicionário de meses em português
meses_pt = {
    1: "jan", 2: "fev", 3: "mar", 4: "abr",
    5: "mai", 6: "jun", 7: "jul", 8: "ago",
    9: "set", 10: "out", 11: "nov", 12: "dez"
}

# Criar gráfico
fig, ax = plt.subplots(figsize=(11, 6))

# Texto ao lado de cada barra — personalize esta lista com o texto que desejar
# Deve conter um item para cada tarefa (mesma ordem de `tasks`)
# bar_texts = [
#     "Sprint 1",
#     "Sprint 1",
#     "Sprint 1",
#     "Sprint 2",
#     "Sprint 2",
#     "Sprint 3",
#     "Sprint 3",
# ]

# Plotar tarefas
for i, (task, start, end) in enumerate(tasks):
    ax.barh(i, end - start, left=start, height=0.4, align="center", color="skyblue")

    # Colocar texto específico ao lado direito de cada barra
    # Ajuste timedelta(days=2) para deslocar mais/menos horizontalmente
    x = end + timedelta(days=2)
    label = ""
    ax.text(x, i, label, va="center", ha="left", fontsize=9, color="black")

# Plotar milestone
for name, date in milestones:
    ax.plot(date, len(tasks), "ro", markersize=10)
    ax.text(date, len(tasks)+0.2, name, ha="center", color="red")

# Ajustes do eixo
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([t[0] for t in tasks])
ax.invert_yaxis()  # Primeira tarefa em cima

# Mostrar apenas meses no eixo X (abreviações em português)
from datetime import timedelta

# Determinar intervalo mínimo/máximo para o eixo X
min_date = min(start for (_, start, _) in tasks)
max_date = max(end for (_, _, end) in tasks)
if milestones:
    max_m = max(m[1] for m in milestones)
    if max_m > max_date:
        max_date = max_m

# Locators/formatters mensais
months = mdates.MonthLocator(interval=1)
ax.xaxis.set_major_locator(months)

def format_month(x, pos=None):
    d = mdates.num2date(x)
    return f"{meses_pt[d.month]}"

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_month))

for date in months.tick_values(min_date, max_date):
    ax.axvline(date, color="lightgray", linestyle="--", linewidth=0.7, alpha=0.7, zorder=0)
    d = mdates.num2date(date)
    ax.text(date, -1, f"{d.month}", ha="center", va="top", fontsize=9, color="gray")

plt.xticks(rotation=45)
plt.title("Cronograma do TCC 2")
plt.tight_layout()
plt.savefig("cronograma_tcc.png", dpi=300)
plt.show()
