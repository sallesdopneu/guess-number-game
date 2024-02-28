import random

def acertou():
    print('Parabéns! você acertou')
def jogo():

    tentas = 0
    num_sec = random.randint(1,100)
    maxtry = 10
    try_ = 0
    while try_ != maxtry:
        tentas = (maxtry - try_)
        print('Escolha um número de 1 a 100, você tem %.f chances ' %(tentas))
        resp = int(input())
        
        if (num_sec - resp) >= 10:
            print('é bem maior')
            try_ += 1

        elif resp < num_sec:
            print("é maior")
            try_ += 1

        if (resp - num_sec) >= 10:
            print('é bem menor')
            try_ += 1

        elif resp > num_sec:
            print('é menor')
            try_ += 1




        if resp == num_sec:
            acertou()
            break
    if try_ == maxtry:
        print("acabaram as tentativas")

jogo()
