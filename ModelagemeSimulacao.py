import numpy as np
import matplotlib.pyplot as plt
import math

def movimentoCircular(a, v0, r, ti, tf, f, tipo):
    w0 = v0 / r
    s = []
    v = []
    w = []
    t = []
    alpha = []
    deltateta = []
    if tipo == "1":
        for i in range(tf):
            t.append(i)
            s.append(2 * math.pi * r)
            v.append(s[i] * f)
            w.append(2 * math.pi * f)
            deltateta.append(w[i] * t[i])
    if tipo == "2":
        for i in range(tf):
            t.append(i)
            
            w.append(w0 + alpha[i] * t[i])
            alpha.append(w[i]/t[i])
            v.append(v0 + a * t[i])
            deltateta.append(w0 * t[i] + (alpha[i] * pow(t[i], 2)/2))
            s.append(v[i]/t[i])
    return t, s, v, w, deltateta


def movimentoUniformementeAcelerado(aY, aX,y0, x0, v0y, v0x, t0, tf):
    vY = []
    vY.append(v0y)
    vX = []
    vX.append(v0x)
    sY = []
    sY.append(y0)
    sX = []
    sX.append(x0)

    t = []

    for i in range(tf):
        t.append(i)
        #definimos aqui o incremento dos vetores de velocidade
        #vY.append(v0y + aY * (i - t0))
        vY.append(vY[i-1] + aY * (i - (i-1)))
        #vX.append(v0x + aX * (i - t0))
        vX.append(vX[i-1] + aX * (i - (i-1)))
        #definimos aqui o incremento dos vetores de espaço
        #sY.append(y0 + v0y * (i - t0) - (1/2) * aY * pow((i - t0),2))
        sY.append(sY[i-1] + vY[i-1] * (i - (i-1)))
        #sX.append(x0 + v0x * (i - t0) + (1/2) * aX * pow((i - t0),2))
        sX.append(sX[i-1] + vX[i-1] * (i - (i-1)))
        #equação da tragetória


    return sX, sY,vX, vY, t

def main():
    print("##################### Escolha um Movimento ##################\n" )
    print("1 - Queda livre\n")
    print("2 - Movimento Oblíquo (projétil)\n ")
    print("3 - Movimento Circular\n")
    mov = input()
    print("Foi escolhido o ", mov)

    if(mov == "1"):
        print("########### Queda Livre ############")
        print("A queda livre é um movimento uniformemente acelerado em y e em x não há movimento\n (não há variação de espaço em relação ao tempo, portanto a velocidade e a aceleação em x são nulas)")
        print("A velocidade inicial em Y (v0y) é 0")
        x0 = float(input("Digite o ponto x em que a queda acontece:"))
        y0 = float(input("Digite o y0 (ponto inicial em y):"))
        aY = float(input("Digite o aY (aceleração em Y):"))
        aX = 0
        v0y = 0
        v0x = 0
        t0 = int(input("Digite o t0 (tempo inicial):"))
        tf = int(input("Digite o tf (tempo final):"))

        sX, sY,vX, vY, t = movimentoUniformementeAcelerado(aY, aX, y0, x0, v0y, v0x, t0, tf)
        print("Velocidade e Y: ")
        print(vY)
        print("Espaço em Y")
        print(sY)

        plt.plot(t, vY)
        plt.grid()
        plt.show()
    if(mov == "2"):
        print("###########  Projétil ############")
        print("O movimento oblíquo é uniformemente acelerado em y e em x o movimento é uniforme\n (não há variação da velocidade, portanto a aceleação em x é nula)")
        x0 = 0
        y0 = 0
        ang = input("Digite o ângulo, em graus, que o corpo é lançado")
        v = input("Digite a velocidade inicial com a qual o corpo é lançado")
        aY = float(input("Digite o aY (aceleração em Y):"))
        aX = 0
        v0y = math.sqrt(pow(v, 2)) * math.sin(ang)
        v0x = v * math.sqrt(pow(v, 2)) * math.cos(ang)
        t0 = int(input("Digite o t0 (tempo inicial):"))
        tf = int(input("Digite o tf (tempo final):"))

        sX, sY,vX, vY, t = movimentoUniformementeAcelerado(aY, aX, y0, x0, v0y, v0x, t0, tf)
        print("Velocidade e Y: ")
        print(vY)
        print("Espaço em Y")
        print(sY)

        plt.plot(t, vY)
        plt.grid()
        plt.show()
    if(mov == "3"):
        print("###########  Movimento Circular ############")
        print("O movimento circular pode ser uniforme(velocidade constante, portanto sem aceleração) ou acelerado (a velocidade varia a uma aceleração)")
        a = float(input("Digite a aceleração do corpo. Caso não haja, digite 0"))
        v0 = float(input("Digite qual é a velocidade inicial do corpo."))
        r = float(input("Digite qual é o raio da circunerência"))
        ti = int(input("Digite o tempo inicial"))
        tf = int(input("Digite qual é o tempo final do movimento"))
        f = float(input("Digite qual é a frequência do moviimento"))
        tipo = input("Digite o tipo de movimento: \n 1 - Uniforme \n 2 - Acelerado")
        t, s, v, w, deltateta = movimentoCircular(a, v0, r, ti, tf, f, tipo)
        
        plt.plot(t, w)
        plt.grid()
        plt.show()
    return(0)
main()
    


    

