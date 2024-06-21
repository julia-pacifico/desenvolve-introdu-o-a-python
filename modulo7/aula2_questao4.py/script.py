import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'\d', senha):
        return False
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]', senha):
        return False
    
    return True