f=open("Caracter.txt","w")
c=str(input("Introduceti un sir: "))
f.write(c)
f.close()

f=open("Caracter.txt","r")
cr=f.read()
print("Sirul dvs.:", cr)
f.close()

v=[]
for i in range(0,len(cr)):
    if str(cr[i])=='o' or str(cr[i])=='a' or str(cr[i])=='e' or str(cr[i])=='i' or str(cr[i])=='u' or str(cr[i])=='O' or str(cr[i])=='A' or str(cr[i])=='E' or cr[i]=='I' or cr[i]=='U':
        v.extend(cr[i])

nr=str(len(v))      
f=open("vocale.txt","w")
f.write(str(v))
f.write('\n')
f.write('Numarul de vocale din sir: ')
f.write(nr)
f.close()

f=open("vocale.txt","r")
z=f.read()
print("Vocalele din sir sunt:", z)
f.close()


