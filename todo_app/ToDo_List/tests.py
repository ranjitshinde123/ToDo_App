from django.test import TestCase
f=open(r"C:\Users\DELL\Downloads\records (1).txt",'a')
print(" pointer ",f.tell())
#print(" pointer {}".format(f.seek(1,1)))
if f.tell() == False:
    print("end of file")
b=f.readline()
v=b.split(" ")
c=f.readline().strip()
d=f.readline().strip()
e=f.readline().strip()
# print('_'.join(v[0:2]),'_'.join(v[2:4]),'_'.join(v[4:5]),'_'.join(v[5:7]),'_'.join(v[7:9]))
o='_'.join(v[0:2]),'_'.join(v[2:4]),'_'.join(v[4:5]),'_'.join(v[5:7]),'_'.join(v[7:9])
y=list(o)
print(c+d+" "+e)
g=f.readline().strip()
h=f.readline().strip()
i=f.readline().strip()
print(g+h+" "+i)

g1=f.readline().strip()
h1=f.readline().strip()
i1=f.readline().strip()
print(g1+h1+" "+i1)

g2=f.readline().strip()
h2=f.readline().strip()
i2=f.readline().strip()
print(g2+h2+" "+i2)

g3=f.readline().strip()
h3=f.readline().strip()
i3=f.readline().strip()
print(g3+h3+" "+i3)

g4=f.readline().strip()
h4=f.readline().strip()
i4=f.readline().strip()
print(g4+h4+" "+i4)

g5=f.readline().strip()
h5=f.readline().strip()
i5=f.readline().strip()
print(g5+h5+" "+i5)


g6=f.readline().strip()
h6=f.readline().strip()
i6=f.readline().strip()
print(g6+h6+" "+i6)

f1=open(r"C:\Users\DELL\Downloads\demo.txt",'w')
f1.write(y[0]+" "+y[1]+" "+y[2]+" "+y[3]+" "+"Dr/Cr"+" "+y[4])
f1.write(c+d+" "+e+"\n")
f1.write(g+h+" "+i+"\n")
f1.write(g1+h1+" "+i1+"\n")
f1.write(g2+h2+" "+i2+"\n")
f1.write(g3+h3+" "+i3+"\n")
f1.write(g4+h4+" "+i4+"\n")
f1.write(g5+h5+" "+i5+"\n")
f1.write(g6+h6+" "+i6+"\n")
f1.close()




