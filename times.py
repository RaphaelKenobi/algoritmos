def ordena(a1):
    a1.sort(reverse=True)
    return a1

def main():
    candidatos, num_times = [int(i) for i in input().split()]
    alunos = []
    count = 0

    while count < candidatos:
        nomes, skill = input().split()
        alunos.append((nomes, int(skill)))
        count += 1

    alunos.sort(key=lambda x: x[1], reverse=True)

    times = [[] for i in range(num_times)]
    count = 0
    aux = 1

    while count < candidatos:
        aluno = alunos[count]
        times[count % num_times].append(aluno[0])
        count += 1

    while aux <= num_times:
        print(f"Time {aux}")
        times[aux - 1].sort()

        for jogador in times[aux - 1]:
            print(jogador)
        print("")
        aux += 1

main()