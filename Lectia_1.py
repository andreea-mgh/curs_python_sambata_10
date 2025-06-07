# tipuri de operatii

a = 12
b = 5

##print('a+b =', a+b)
##print('a-b =', a-b)
##print('a*b =', a*b)
##
##print('a/b =', a/b)
##print('a//b =', a//b)
##print('a%b =', a%b)

# conditii

##print(a == b)
##print(a != b, not a == b)
##print(a >= b)

if a > b:
    print('biscuiti')
else:
    print('placinte')

print('gata')

lista_cool = [ 'rosu', 'galben', 'albastru', 'mov', 'verde' ]

for i in lista_cool:
    print(i)








def patrat(w=2, h=2, char='#'):
    for i in range(h):
        print(char * w)

def patrat_frumos(w=1, h=1):
    print('+' + w*'-' + '+')
    for i in range(h):
        print('|' + w*' ' + '|')
    print('+' + w*'-' + '+')
    



patrat(char = '*')

patrat_frumos(3, 5)



numere = [3, 6, 12, 13, 'andrei', 'ion']

print(numere[2]) # al treilea element
print(numere[0]) # primul
print(numere[-1]) # ultimul
print(numere[-3]) # al treilea de la coada 

print(numere[0:4]) # toate elementele de la primul la al patrulea
