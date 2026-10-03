import os

nome: str = ""

nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0

dir: str = ""
arq: str = ""

def med(n1, n2, n3, n4):
    media: float = 0.0

    media = (n1 + n2 + n3 + n4) / 4
    return media

def escrevearq(caminho, arquivo, linha_arq):
    file: str = ""
    tipo: str = ""
    enc: str = ""

    if os.path.exists(caminho) and os.path.isdir(caminho):

        file = os.path.join(caminho, arquivo)

        if os.path.exists(file):
            tipo = "a"
        else:
            tipo = "w"

        enc = "utf-8"

        with open(file, tipo, encoding=enc) as f:
            f.write(linha_arq)

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha: str = ""

    linha = (
        str(nm) + ";" +
        str(nt1) + ";" +
        str(nt2) + ";" +
        str(nt3) + ";" +
        str(nt4) + ";" +
        str(vlr_med) + "\n"
    )

    escrevearq(dir, arq, linha)

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input("digite o nome do aluno: ")

    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    nota3 = float(input("digite a terceira nota: "))
    nota4 = float(input("digite a quarta nota: "))

    valor_media = med(nota1, nota2, nota3, nota4)

    print("media:", valor_media)

    if valor_media >= 6.0:
        print("aprovado")
    elif valor_media >= 3.0:
        print("exame")
    else:
        print("retido")

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    contador = 0

    for contador in range(5):
        entrada()

dir = "/tmp/exercicios/"
arq = "exercicio21.txt"

os.makedirs(dir, exist_ok=True)
os.chmod(dir, 0o744)

if __name__ == "__main__":
    main()