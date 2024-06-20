import datetime

agora= datetime.datetime.now()

dia= agora.day
mes=agora.month
ano= agora.year
hora=agora.hour
minuto= agora.minute

data=f"data: {dia:0d}/{mes:0d}/{ano:0d}"
hora=f"hora: {hora:0d}:{minuto:0d}"

print(data)
print(hora)