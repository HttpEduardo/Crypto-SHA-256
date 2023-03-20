import hashlib
from tqdm import tqdm

def encrypt_string(input_string):
    # Converte a string de entrada em bytes
    input_bytes = input_string.encode('utf-8')

    # Cria um objeto de hash SHA-256
    sha256_hash = hashlib.sha256()

    # Define o tamanho do bloco de dados para criptografia
    block_size = 1024

    # Inicializa a barra de progresso
    progress_bar = tqdm(total=len(input_bytes), unit='B', unit_scale=True)

    # Itera sobre a string de entrada enquanto criptografa os dados
    for i in range(0, len(input_bytes), block_size):
        # Atualiza a barra de progresso
        progress_bar.update(block_size)

        # Seleciona o bloco atual de dados
        block = input_bytes[i:i+block_size]

        # Adiciona o bloco de dados ao objeto de hash
        sha256_hash.update(block)

    # Finaliza a barra de progresso
    progress_bar.close()

    # Retorna a string criptografada
    return sha256_hash.hexdigest()

# Exemplo de uso da função de criptografia
input_string = 'Hello, world!'
encrypted_string = encrypt_string(input_string)
print(f'Input string: {input_string}')
print(f'Encrypted string: {encrypted_string}')
