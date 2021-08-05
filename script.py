from sympy import *
import time
import numpy as np

x = Symbol('x')

expr = expand(input('Digite aqui a expressao: '))
time.sleep(3)

numa = float(input('Digite aqui o intervalo A: '))
intervaloa = expr.subs(x, numa)

numb = float(input('Digite aqui o intervalo B: '))
intervalob = expr.subs(x, numb)

if intervaloa * intervalob < 0:
    print('Primeiro passo OK! ')
    time.sleep(4)
    print('Agora iremos testar a derivada!')
    time.sleep(4)

    derivada = expr.diff(x) #Derivada da equação que o usuario digitou
    derivada1 = derivada.subs(x, numa) #Substituindo o intervalo a na equação da derivada
    derivada2 = derivada.subs(x, numb) #Substituindo o intervalo b na equação da derivada

    if derivada1 and derivada2 < 0 or derivada1 and derivada2 > 0:
        print('O intervalo é Válido!')
        time.sleep(3)
        print('Agora iremos calcular as raizes de acordo com os intervalos {} e {}'.format(numa, numb))     
        xn = (numa + numb)/2
        int = int(input("Digite quantas interações Você deseja: "))
        for i in range (int):
            xn = xn - np.float(expr.evalf(subs= {x:xn})) / np.float(derivada.evalf(subs= {x:xn}))
            if xn < 0:
                xn = xn * -1
                print(f'A {i+1} Interação xn é {xn:.6} e f(xn) is {np.float(expr.evalf(subs= {x:xn})):.2}')
            else:
                print(f'A {i+1} Interação xn é {xn:.6} e f(xn) is {np.float(expr.evalf(subs= {x:xn})):.2}')
else:
    print("Intervalo inválido")            



#2 * x**3 + 3 * x**2 - 2
#0.01 e 1