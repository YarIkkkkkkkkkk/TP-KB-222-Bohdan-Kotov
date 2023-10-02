sp=[5,15,16,2023]
sp1=[1,1,1,1,5]

sp.extend(sp1)
print(sp)
sp.append(666)
print(sp)
sp.insert(0, 2023)
print(sp)
sp.remove(2023)
print(sp)
sp1.clear()
print(sp1)
sp.sort()
print(sp)
sp.reverse()
print(sp)
sp1=sp.copy()
print(sp1)