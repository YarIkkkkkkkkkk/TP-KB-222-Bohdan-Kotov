def corin(a,b,c):
    D=int(b)**2-4*int(a)*int(c)
    if D>0:
        x1=(-int(b)+D**0.5)/2*int(a)
        x2=(-int(b)-D**0.5)/2*int(a)
        return(x1,x2)
    elif D<0:return('None')
    else:return((-int(b)+D**0.5)/2*int(a))
a,b,c=input('Введіть a b та c ').split()
print(corin(a,b,c))