import random

def acertou():
    print('acertou')
def jogo():


    num_sec = random.randint(1,10)
    maxtry = 5
    try_ = 0
    tentas = maxtry - try_
    while try_ != maxtry:

        resp = int(input('Escolha um número de 1 a 10 '))

        if resp < num_sec:
            print("é maior")
            try_ += 1

        if resp > num_sec:
            print('é menor')
            try_ += 1

        if resp == num_sec:
            print('acertou')
            break
    if try_ == maxtry:
        print("acabaram as tentativas")

jogo()
