def verificar_transcricao(transcricao):
    # Verificar se a transcrição começa com "O"
    if transcricao.startswith("O"):
        return '?'

    # Verificar se houve empate
    if 'X' not in transcricao and 'O' not in transcricao:
        return '*'

    # Verificar se houve vitória de algum jogador
    if 'XX' in transcricao:
        return 'Alice'
    if 'OO' in transcricao:
        return 'Bob'

    # Se não for nenhum dos casos acima, a transcrição é inconsistente
    return '?'

# Entrada de exemplo
transcricao = input().strip()

# Verificar a consistência da transcrição e determinar o resultado
resultado = verificar_transcricao(transcricao)
print(resultado)
