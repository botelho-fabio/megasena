import random
cartelas = list(range(0, 100))
for i in range(0, 100):
    cartela = random.randint(1, 50063860)
    cartelas[i] = cartela
print(cartelas)
jogo = 0
for a in range(0, 60):
    for b in range(a+1, 60):
        for c in range(b+1, 60):
            for d in range(c+1, 60):
                for e in range(d+1, 60):
                    for f in range(e+1, 60):
                        jogo = jogo+1
                        for x in range(0, 100):
                            if (jogo == cartelas[x]):
                                print(str(jogo) + ' ' + str(a+1) + ' ' + str(b+1) + ' ' +
                                      str(c+1) + ' ' + str(d+1) + ' ' + str(e+1) + ' ' + str(f+1))
                                break
