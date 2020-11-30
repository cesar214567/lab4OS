import io
from random import randint as rand

name = 'output.txt'

def random_writes():
    to_write ='HOLA'*1000000000 
    f = open(name, 'w')
    for i in range(10):
        f.seek(rand(0, 5000000), 0)
        f.write(to_write)
    f.close()

def random_reads():
    f=open(name, 'r')
    for i in range(100**3):
        f.seek(rand(0, 5000), 0)
        f.read(int(1024**3))
    f.close()

def seq_writes():
    to_write ='HOLA'*1000000
    f=open(name, 'w')
    for i in range(1000**3):
        f.write(to_write)
    f.close()

def seq_reads():
    f=open(name, 'r')
    value = int(100**3)
    for i in range(1000):
        #f.seek(0, 0)
        f.read(value)
    f.close()

#seq_writes()
seq_reads()
#random_writes()
#random_reads()

# codigo para el iostat: iostat -x 1
# ejecutar coddigo de python: python3 main.py
