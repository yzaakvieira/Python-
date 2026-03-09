from time import time

# número total de segundos desde o Unix epoch
now = int(time())  # removendo a parte decimal

# segundos em um dia
seconds_per_day = 86400

# 1️⃣ Número de dias desde 1º de janeiro de 1970
days = now // seconds_per_day

# 2️⃣ Segundos restantes após remover os dias completos
remaining_seconds = now % seconds_per_day

# 3️⃣ Horas
hours = remaining_seconds // 3600

# 4️⃣ Minutos
remaining_seconds = remaining_seconds % 3600
minutes = remaining_seconds // 60

# 5️⃣ Segundos
seconds = remaining_seconds % 60

print("Dias desde 1/1/1970:", days)
print("Horário atual (UTC):", f"{hours:02d}:{minutes:02d}:{seconds:02d}")

# Na f-string foi usada uma formatação de strings
# A formatação de strings segue o seguinte formato:
#         valor : formatação | valor - uma variável ou uma expressão | : separa o valor da formatação | formatação - regras de como exibir o valor
# As regras de formatação, seguem esse padrão: [preenchimento][alinhamento][largura][.precisão][tipo]
# No nosso exemplo usamos o preenchimento, a largura mínimo, e o tipo
# Por que mudar o tipo pode ser importante? Observe no exemplo sugerido
print("\n")
print("Horário atual em binário (UTC):", f"{hours:02b}:{minutes:02b}:{seconds:02b}")

# Ou seja se eu mudo o tipo, eu mudo completamente a formatação do meu dado, para não ficar muito grande o texto, não pretendo me extender sobre os outros padrões, mas saiba que isso existe, e é muito interessante de ser usado. Só pra ressaltar também poderia ter usado o .format - funcionaria da mesma forma.