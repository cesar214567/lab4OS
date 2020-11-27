import io
from random import randint as rand

name = 'output.txt2'

def random_writes():
    f = open(name, 'w')
    for i in range(1000**2):
        f.seek(rand(0, 500000000, 0))
        f.write('HOLA'*1000000)
    f.close()

def random_reads():
    f=open(name, 'r')
    for i in range(1000**2):
        f.seek(rand(0, 500000000, 0))
        f.read(int(1024**3))
    f.close()

def seq_writes():
    f=open(name, 'w')
    for i in range(1000):
        f.write('HOLA'*1000000)
    f.close()

def seq_reads():
    f=open(name, 'r')
    for i in range(1000):
        f.seek(0, 0)
        f.write('HOLA'*1000000)
    f.close()

# codigo para el iostat: iostat -x 1
# ejecutar coddigo de python: python3 main.py
