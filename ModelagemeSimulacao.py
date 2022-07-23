import numpy as np
import matplotlib.pyplot as plt
import math


def movimentoCircular(a, alpha, v0, r, t0, tf, f, tipo):
    m = 0.1 #kg
    k = 10 #kN/m
    a = 2
    b = 3
    Ab = 0
    fi0 = 0
    v = []
    w = []
    t = []
    if tipo == "1":
        w = math.sqrt(k/m)
        Ab = math.sqrt(pow(a,2) + pow(b,2))
        f = (1/2*math.pi)*w
        T = 1/f

        fi = []
        t = []
        x = []
        v = []
        a = []
        for i in range (t0, tf*100):
            t.append(i/100)
            fi.append(w*t[i] + fi0)
            x.append(Ab * math.cos(fi[i]))
            v.append(-1 * Ab*w*math.sin(fi[i]))
            a.append(-1 * Ab*pow(w,2)*math.cos(fi[i]))

        s = ([x,v,t])
        #return s
        return x,v,t

def movimentoUniformementeAcelerado(aY, aX, y0, x0, v0y, v0x, t0):
    vY = []
    # vY.append(v0y)
    vX = []
    # vX.append(v0x)
    sY = []
    # sY.append(y0)
    sX = []
    # sX.append(x0)
    t = []
    # t.append(t0)
    i = -1
    a = []
    while(True):
        i = i + 1
        print(i)
        t.append(i/1000)
        sY.append(y0 + v0y * (t[i] - t0) - (1 / 2) * aY * pow((t[i] - t0), 2))
        # sY.append(sY[i-1] + vY[i-1] * (i - (i-1)))
        print(sY[i])
        if(sY[i] < 0):
            t.pop(i)
            sY.pop(i)
            break
        sX.append(x0 + v0x * (t[i] - t0) + (1 / 2) * aX * pow((t[i] - t0), 2))
        # sX.append(sX[i-1] + vX[i-1] * (i - (i-1)))
        # definimos aqui o incremento dos vetores de velocidade
        vY.append(v0y + aY * (t[i] - t0))
        # vY.append(vY[i-1] + aY * (i - (i-1)))
        vX.append(v0x + aX * (t[i] - t0))
        # vX.append(vX[i-1] + aX * (i - (i-1)))
        # definimos aqui o incremento dos vetores de espaço
        # equação da tragetória
        a.append(aY)
    return sX, sY, vX, vY, t, a


def main():
    print("##################### Escolha um Movimento ##################\n")
    print("1 - Queda livre\n")
    print("2 - Movimento Oblíquo (projétil)\n ")
    print("3 - Movimento Circular\n")
    print("4 - Pêndulo\n")
    mov = input()
    print("Foi escolhido o ", mov)

    if (mov == "1"):
        print("########### Queda Livre ############")
        print(
            "A queda livre é um movimento uniformemente variado em y e em x não há movimento\n (não há variação de espaço em relação ao tempo, portanto a velocidade e a aceleação em x são nulas)")
        print("A velocidade inicial em Y (v0y) é 0")
        x0 = float(input("Digite o ponto x em que a queda acontece:"))
        y0 = float(input("Digite o y0 (ponto inicial em y):"))
        aY = float(input("Digite o aY (aceleração em Y):"))
        aX = 0
        v0y = 0
        v0x = 0
        t0 = int(input("Digite o t0 (tempo inicial):"))

        sX, sY, vX, vY, t, aY= movimentoUniformementeAcelerado(aY, aX, y0, x0, v0y, v0x, t0)
        print("Velocidade e Y: ")
        print(vY)
        print("tempo")
        print(t)
        print("Espaço em Y")
        print(sY)
        plt.xlabel("Tempo(s)")
        plt.ylabel("Velocidade(m/s)")
        plt.plot(t, vY)
        plt.grid()
        plt.show()
        plt.xlabel("Tempo(s)")
        plt.ylabel("Espaço(m)")
        plt.plot(t, sY)
        plt.grid()
        plt.show()
        plt.plot(t,sY)
        plt.plot(t,vY)
        plt.plot(t,aY)

        plt.legend(["Espaço", "Velocidade", "Aceleração"])
        plt.xlabel("Tempo(s)")
        plt.show()
    if (mov == "2"):
        print("###########  Projétil ############")
        print(
            "O movimento oblíquo é uniformemente acelerado em y e em x o movimento é uniforme\n (não há variação da velocidade, portanto a aceleação em x é nula)")
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

        sX, sY, vX, vY, t = movimentoUniformementeAcelerado(aY, aX, y0, x0, v0y, v0x, t0, tf)
        print("Velocidade e Y: ")
        print(vY)
        print("Espaço em Y")
        print(sY)

        plt.plot(t, vY)
        plt.grid()
        plt.show()
    if (mov == "3"):
        print("###########  Movimento Circular ############")
        print(
            "O movimento circular pode ser uniforme(velocidade constante, portanto sem aceleração) ou acelerado (a velocidade varia a uma aceleração)")
        a = float(input("Digite a aceleração do corpo. Caso não haja, digite 0"))
        v0 = float(input("Digite qual é a velocidade inicial do corpo."))
        r = float(input("Digite qual é o raio da circunerência"))
        t0 = int(input("Digite o tempo inicial"))
        tf = float(input("Digite qual é o tempo final do movimento"))
        f = float(input("Digite qual é a frequência do moviimento"))
        tipo = input("Digite o tipo de movimento: \n 1 - Uniforme \n 2 - Acelerado")

        #t0 = 0
        #tf = 50
        m = 3700 #kg
        k = pow((math.pi*2)/tf-t0, 2)*m #kN/m
        a = 2
        b = 3
        fi0 = 0

        w = math.sqrt(k/m)
        A = math.sqrt(pow(a,2) + pow(b,2))
        f = (1/2*math.pi)*w
        T = 1/f
        tfI = int(tf*100)
    
        fi = []
        t = []
        x = []
        v = []
        a = []
        for i in range (t0, tfI):
            t.append(i/100)
            fi.append(w*t[i] + fi0)
            x.append(A * math.cos(fi[i]))
            v.append(-1 * A*w*math.sin(fi[i]))
            a.append(-1 * A*pow(w,2)*math.cos(fi[i]))


        s = ([x,v,t])
        print("frequência: ", f)
        print("Período:", T)

        print(t)
        print(x)
        print(v)
        print(a)
        print(fi)
        plt.plot(t,x)
        plt.plot(t,v)
        plt.plot(t,a)

        plt.legend(["Espaço", "Velocidade", "Aceleração"])
        plt.xlabel("Tempo(s)")
        plt.show()
        plt.ylabel("Espaço(rad)")
        plt.xlabel("Tempo(s)")
    
        plt.plot(t,x)
        plt.show()
        plt.ylabel("Velocidade(rad/s)")
        plt.xlabel("Tempo(s)")
        plt.plot(t,v)
        plt.show()
        plt.plot(t,a)
        plt.ylabel("Aceleração(rad/s²)")
        plt.xlabel("Tempo(s)")
        plt.show()
        #velocidade em relação ao espaço
        plt.plot(s[0], s[1])


    return (0)


main()





