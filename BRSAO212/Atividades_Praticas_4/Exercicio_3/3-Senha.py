#3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
#a - deve ter pelo menos 8 caracteres.
#b - deve conter pelo menos um número.

def verificar_senha(senha):
    if len(senha) < 8:
        return "Senha fraca: deve ter pelo menos 8 caracteres."
    if not any(char.isdigit() for char in senha):
        return "Senha fraca: deve conter pelo menos um número."
    return "Senha forte: atende aos critérios de segurança."

senha_usuario = input("Digite a senha para verificação: ")
resultado = verificar_senha(senha_usuario)
print(resultado)
