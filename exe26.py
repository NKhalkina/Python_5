'''Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии'''
a=int(input('Введите число А: '))
b=int(input('Введите степень В: '))
def degree(a,b):
    if b==0:
        return 1
    return (a*degree(a,b-1))
temp=degree(a,b)
print(temp)
