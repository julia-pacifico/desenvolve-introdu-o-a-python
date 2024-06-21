import csv

caminho_arquivo = 'spotify-2023.csv'

musicas_populares = []

with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    next(leitor_csv)

    musicas_por_ano = {}

    for linha in leitor_csv:
        try:
            track_name = linha[0].strip()
            artists_name = linha[1].strip()
            artist_count = int(linha[2].strip())
            released_year = int(linha[3].strip())
            streams = int(linha[8].strip())

            if '"' in artists_name or '(' in track_name:
                continue
            
            if 2012 <= released_year <= 2022:
                if released_year not in musicas_por_ano or streams > musicas_por_ano[released_year][3]:
                    musicas_por_ano[released_year] = [track_name, artists_name, released_year, streams]
        
        except Exception as e:
            print(f"Erro ao processar linha: {linha}")
            print(e)

    for ano in range(2012, 2023):
        if ano in musicas_por_ano:
            musicas_populares.append(musicas_por_ano[ano])

print("Músicas mais populares de cada ano (2012-2022):")
for musica in musicas_populares:
    print(musica)