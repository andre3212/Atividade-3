n1 = int(input('nota 1: '))
n2 = int(input('nota 2: '))
n3 = int(input('nota 3: '))

media = (n1+n2+n3)/3

if n3>8:
    media = media+1
if media > 10:

    media = 10
print(media)
