import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



# Lista de tarefas (nome, início, fim)
tasks = [
    ("Análise contextual e decisão inicial", "2024-08-26", "2024-09-09"),
    ("Perfil motivacional e personalização", "2024-09-02", "2024-09-30"),
    ("Ideação criativa e co-design", "2024-10-01", "2024-10-14"),
    ("Prototipagem iterativa", "2024-10-15", "2024-11-05"),
    ("Elaboração do TCC no Overleaf", "2024-10-01", "2024-11-25"),
]

# Evento único
milestones = [
    ("Entrega do TCC 1", "2024-12-01")
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

# Plotar tarefas
for i, (task, start, end) in enumerate(tasks):
    ax.barh(i, end - start, left=start, height=0.4, align="center", color="skyblue")

    # Texto centralizado dentro da barra (datas de início e fim)
    mid_point = start + (end - start) / 2
    date_range = f"{start.day} {meses_pt[start.month]} – {end.day} {meses_pt[end.month]}"
    ax.text(mid_point, i, date_range, ha="center", va="center", fontsize=8, color="black")

# Plotar milestone
for name, date in milestones:
    ax.plot(date, len(tasks), "ro", markersize=10)
    ax.text(date, len(tasks)+0.2, name, ha="center", color="red")

# Ajustes do eixo
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([t[0] for t in tasks])
ax.invert_yaxis()  # Primeira tarefa em cima

# 🔹 Linhas suaves no início de cada mês
months = mdates.MonthLocator()
ax.xaxis.set_minor_locator(months)
for date in months.tick_values(tasks[0][1], milestones[0][1]):
    ax.axvline(date, color="lightgray", linestyle="--", linewidth=0.7, alpha=0.7, zorder=0)

# Formatter manual para português
def format_date(x, pos=None):
    d = mdates.num2date(x)
    return f"{d.day} {meses_pt[d.month]}"

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_date))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

plt.xticks(rotation=45)
plt.title("Cronograma do TCC")
plt.tight_layout()
plt.savefig("cronograma_tcc.png", dpi=300)
plt.show()
