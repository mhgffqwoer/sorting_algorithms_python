from matplotlib import pyplot as plt
from algoritms.built_in import *
from algoritms.bubble import *
from algoritms.heap import *
from algoritms.insertion import *
from algoritms.merge import *
from algoritms.quick import *
from algoritms.selection import *
from algoritms.test import *
from generator.generator import *


def run(command):
    if command=='bubble':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=bubble,array=arr1))
            di.append(test(func=bubble,array=arr2))
            ran.append(test(func=bubble,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Bubble \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='merge':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=merge,array=arr1))
            di.append(test(func=merge,array=arr2))
            ran.append(test(func=merge,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Merge \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='built_in':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,10001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=built_in,array=arr1))
            di.append(test(func=built_in,array=arr2))
            ran.append(test(func=built_in,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Built-in \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='quick':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=quick,array=arr1))
            di.append(test(func=quick,array=arr2))
            ran.append(test(func=quick,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Quick \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='heap':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=heap,array=arr1))
            di.append(test(func=heap,array=arr2))
            ran.append(test(func=heap,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Heap \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='insertion':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=insertion,array=arr1))
            di.append(test(func=insertion,array=arr2))
            ran.append(test(func=insertion,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Insertion \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='selection':
        x,rev,di,ran = [],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            arr1 = reverse(i)
            arr2 = direct(i)
            arr3 = random(i)
            rev.append(test(func=selection,array=arr1))
            di.append(test(func=selection,array=arr2))
            ran.append(test(func=selection,array=arr3))
        plt.figure(figsize=(10, 5))
        plt.plot(x,rev, label=r'$f_1(x)=reverse$')
        plt.plot(x,di, label=r'$f_2(x)=direct$')
        plt.plot(x,ran, label=r'$f_3(x)=random$')
        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$Selection \ Sort$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()

    if command=='all':
        x, bub, hea, ins, qui, sel, mer, bui = [],[],[],[],[],[],[],[]
        for i in range(0,5001,100):
            x.append(i)
            bub1 = random(i)
            hea1 = random(i)
            ins1 = random(i)
            qui1 = random(i)
            sel1 = random(i)
            mer1 = random(i)
            bui1 = random(i)
            bub.append(test(func=bubble,array=bub1))
            hea.append(test(func=heap,array=hea1))
            ins.append(test(func=insertion,array=ins1))
            qui.append(test(func=quick,array=qui1))
            sel.append(test(func=selection,array=sel1))
            mer.append(test(func=merge,array=mer1))
            bui.append(test(func=built_in,array=bui1))
        plt.figure(figsize=(10, 5))

        plt.plot(x,bub, label=r'$f_1(x)=bubble$')
        plt.plot(x,hea, label=r'$f_2(x)=heap$')
        plt.plot(x,ins, label=r'$f_3(x)=insertion$')
        plt.plot(x,qui, label=r'$f_4(x)=quick$')
        plt.plot(x,sel, label=r'$f_5(x)=selection$')
        plt.plot(x,mer, label=r'$f_6(x)=merge$')
        plt.plot(x,bui, label=r'$f_6(x)=built-in$')

        plt.xlabel(r'$x,\ (длинна \ массива)$')
        plt.ylabel(r'$f(x), (микросекунды)$')
        plt.title(r'$All \ algorithms$')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True)
        plt.show()