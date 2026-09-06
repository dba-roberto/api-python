from pwdlib import PasswordHash

PASSWORD_HASHER = PasswordHash.recommended()

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta, comparando a senha em texto puro
    informado pelo usuário.
    """
    return PASSWORD_HASHER.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera o hash da senha
    """
    return PASSWORD_HASHER.hash(senha)