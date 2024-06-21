import csv

# Funções de utilidade
def carregar_usuarios():
    usuarios = []
    with open('usuarios.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios.append(row)
    return usuarios

def carregar_produtos():
    produtos = []
    with open('produtos.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append(row)
    return produtos

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        fieldnames = ['id', 'nome', 'usuario', 'senha', 'permissao']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)

def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='') as file:
        fieldnames = ['id', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Funções CRUD para usuários
def criar_usuario(usuarios):
    id = str(len(usuarios) + 1)
    nome = input("Nome: ")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    permissao = input("Permissão (gerente/vendedor): ")
    usuarios.append({'id': id, 'nome': nome, 'usuario': usuario, 'senha': senha, 'permissao': permissao})
    salvar_usuarios(usuarios)
    print("Usuário criado com sucesso!")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def atualizar_usuario(usuarios):
    id = input("ID do usuário a ser atualizado: ")
    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = input(f"Novo nome (atual: {usuario['nome']}): ") or usuario['nome']
            usuario['usuario'] = input(f"Novo usuário (atual: {usuario['usuario']}): ") or usuario['usuario']
            usuario['senha'] = input(f"Nova senha (atual: {usuario['senha']}): ") or usuario['senha']
            usuario['permissao'] = input(f"Nova permissão (atual: {usuario['permissao']}): ") or usuario['permissao']
            salvar_usuarios(usuarios)
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado!")

def deletar_usuario(usuarios):
    id = input("ID do usuário a ser deletado: ")
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            print("Usuário deletado com sucesso!")
            return
    print("Usuário não encontrado!")

# Funções CRUD para produtos
def criar_produto(produtos):
    id = str(len(produtos) + 1)
    nome = input("Nome do produto: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")
    produtos.append({'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos(produtos)
    print("Produto criado com sucesso!")

def listar_produtos(produtos):
    for produto in produtos:
        print(produto)

def atualizar_produto(produtos):
    id = input("ID do produto a ser atualizado: ")
    for produto in produtos:
        if produto['id'] == id:
            produto['nome'] = input(f"Novo nome (atual: {produto['nome']}): ") or produto['nome']
            produto['preco'] = input(f"Novo preço (atual: {produto['preco']}): ") or produto['preco']
            produto['quantidade'] = input(f"Nova quantidade (atual: {produto['quantidade']}): ") or produto['quantidade']
            salvar_produtos(produtos)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado!")

def deletar_produto(produtos):
    id = input("ID do produto a ser deletado: ")
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            salvar_produtos(produtos)
            print("Produto deletado com sucesso!")
            return
    print("Produto não encontrado!")

def buscar_produto(produtos):
    nome = input("Nome do produto a ser buscado: ")
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print(produto)
            return
    print("Produto não encontrado!")

def listar_produtos_ordenados_por_nome(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(produto)

def listar_produtos_ordenados_por_preco(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    for produto in produtos_ordenados:
        print(produto)

# Controle de acesso
def login(usuarios):
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user['usuario'] == usuario and user['senha'] == senha:
            return user
    print("Usuário ou senha incorretos!")
    return None

# Menu interativo
def menu_gerente(usuarios, produtos):
    while True:
        print("\nMenu Gerente")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Criar Produto")
        print("6. Listar Produtos")
        print("7. Atualizar Produto")
        print("8. Deletar Produto")
        print("9. Buscar Produto")
        print("10. Listar Produtos por Nome")
        print("11. Listar Produtos por Preço")
        print("12. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criar_usuario(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
        elif opcao == '4':
            deletar_usuario(usuarios)
        elif opcao == '5':
            criar_produto(produtos)
        elif opcao == '6':
            listar_produtos(produtos)
        elif opcao == '7':
            atualizar_produto(produtos)
        elif opcao == '8':
            deletar_produto(produtos)
        elif opcao == '9':
            buscar_produto(produtos)
        elif opcao == '10':
            listar_produtos_ordenados_por_nome(produtos)
        elif opcao == '11':
            listar_produtos_ordenados_por_preco(produtos)
        elif opcao == '12':
            break
        else:
            print("Opção inválida!")

def menu_vendedor(produtos):
    while True:
        print("\nMenu Vendedor")
        print("1. Listar Produtos")
        print("2. Buscar Produto")
        print("3. Listar Produtos por Nome")
        print("4. Listar Produtos por Preço")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            listar_produtos(produtos)
        elif opcao == '2':
            buscar_produto(produtos)
        elif opcao == '3':
            listar_produtos_ordenados_por_nome(produtos)
        elif opcao == '4':
            listar_produtos_ordenados_por_preco(produtos)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    user = login(usuarios)
    if user:
        if user['permissao'] == 'gerente':
            menu_gerente(usuarios, produtos)
        elif user['permissao'] == 'vendedor':
            menu_vendedor(produtos)

if __name__ == "__main__":
    main()
