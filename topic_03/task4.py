sp=[1,2,5,10]
while True:
    a=input('Введіть число ')
    if a=='q':
        break
    for i in sp:
        if int(a)>sp[len(sp)-1]:
            sp.append(int(a))
        elif int(a)<=i:
            sp.insert(sp.index(i),int(a))
            break
    print('Результат виконання ',sp)