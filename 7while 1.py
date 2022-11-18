#Шарапова Ангира 21 ис 21
#Задание 1. Задача «Количество слов». Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.

a=input()
print(a.count(" ") +1)

#

print(input().count(' ')+1)

#

s=input().split()
i=1
while i<len(s):
    i+=1
print(i)

#

print(len(input().split))

#

a = input()
i = 0
k = 0
while i < len(a):
    if a[i] == ' ':
        k += 1
    elif a[i] == ' ' and a[i - 1] == ' ':
        k += 1
    i += 1
print(k)
