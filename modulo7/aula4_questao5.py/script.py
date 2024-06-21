import csv

livros = [
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 223},
    {"Título": "Harry Potter e a Câmara Secreta", "Autor": "J.K. Rowling", "Ano de publicação": 1998, "Número de páginas": 251},
    {"Título": "Harry Potter e o Prisioneiro de Azkaban", "Autor": "J.K. Rowling", "Ano de publicação": 1999, "Número de páginas": 317},
    {"Título": "Harry Potter e o Cálice de Fogo", "Autor": "J.K. Rowling", "Ano de publicação": 2000, "Número de páginas": 462},
    {"Título": "Harry Potter e a Ordem da Fênix", "Autor": "J.K. Rowling", "Ano de publicação": 2003, "Número de páginas": 766},
    {"Título": "Harry Potter e o Enigma do Príncipe", "Autor": "J.K. Rowling", "Ano de publicação": 2005, "Número de páginas": 607},
    {"Título": "Harry Potter e as Relíquias da Morte", "Autor": "J.K. Rowling", "Ano de publicação": 2007, "Número de páginas": 607},
    {"Título": "Dom Quixote", "Autor": "Miguel de Cervantes", "Ano de publicação": 1605, "Número de páginas": 863},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "Crime e Castigo", "Autor": "Fiódor Dostoiévski", "Ano de publicação": 1866, "Número de páginas": 551},
    {"Título": "Orgulho e Preconceito", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 432},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 471},
]

nome_arquivo = "meus_livros.csv"

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    for livro in livros:
        titulo = livro["Título"]
        autor = livro["Autor"]
        ano = livro["Ano de publicação"]
        paginas = livro["Número de páginas"]
        linha = f"{titulo},{autor},{ano},{paginas}\n"
        arquivo.write(linha)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")