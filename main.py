import io
from random import randint as rand
def random_writes: # TODO
    with open('output.txt2','w') as file:
#        for i in range(1000000000):
        for i in range(1000**2):
            file.seek(rand(0,500000000,0)
            file.write('HOLA'*1000000)
def random_reads:
    with open('output.txt2','r') as file:
        for i in range(1000**2):
            file.seek(rand(0,500000000,0)
            file.read(int(1024**3))

def seq_writes:
    with open('output.txt2','w') as file:
        #for i in range(1000000000):
        for i in range(1000):
            file.write('HOLA'*1000000)
def seq_reads:
    with open('output.txt2','r') as file:
        for i in range(1000):
            file.seek(0,0)
            file.write('HOLA'*1000000)
            
#codigo para el iostat: iostat -x 1 
#ejecutar coddigo de python: python3 main.py
