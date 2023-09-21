def diskrininant(a,b,c):
    return int(b)**2-4*int(a)*int(c)
a,b,c=input('Введіть a b та c ').split()
print(diskrininant(a,b,c))
