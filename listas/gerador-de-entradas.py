import argparse
import random
import collections
import os

# rodar esse arquivo com os parâmetros correspondentes - ex: python3 gerador.py -i entrada.txt -a string_a -b 1 -c 10 100
parser = argparse.ArgumentParser(description='descrição do que o código faz')

parser.add_argument(
        '-i', 
        '--input-file', 
        metavar = '\b',
        help = """Nome do arquivo de entrada que o programa vai gerar""",
        type = str
        )
parser.add_argument(
        '-a', 
        '--parametro-a', 
        metavar = '\b',
        help = """string. escrever significado do parâmetro aqui""",
        type = str,
        )
parser.add_argument(
        '-b',   
        '--parametro_b',
        metavar = '\b',
        help = """inteiro. escrever significado do parâmetro aqui""",
        type = int,
        )
parser.add_argument(
        '-c',   
        '--parametro_c',
        metavar = '\b',
        help = """Dois inteiros. escrever significado dos parâmetros aqui""",
        type = int,
        nargs = '+'
        )       

args = parser.parse_args()

# para acessar os parametros usar args.nome_que_vc_deu_ao_parametro
k = args.parametro_a

# inicializando buffer como string
# esse é o objeto que vai ter o conteúdo do arquivo de entrada no iudex, o arquivo em si é o 'input_file' retornado no final.
input_buffer = ""

# aqui, vai implementar a lógica da entrada que você quer gerar. esse código é só um exemplo e cria um documento vazio.

# abre o arquivo que vai conter as entradas do problema 
# (não precisa ser o nome de um arquivo existente no seu computador, o script cria um automaticamente)
input_file = open(args.input_file, 'w')

# transcreve o buffer pra o documento
input_file.write(input_buffer)

# fecha o documento
input_file.close()
