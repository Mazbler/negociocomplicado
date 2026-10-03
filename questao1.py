import os

valor: int = 0
dir: str = ""
arq: str = ""

def mult(vlr, tabuada):
    res = vlr * tabuada
    return res

def grava(c, resultado):
    global dir, arq

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    linha = str(resultado) + "\n"

    if os.path.exists(dir) and os.path.isdir(dir):
        if os.path.exists(os.path.join(dir, arq)):
            if c > 0:
                tipo = "a"
            else:
                tipo = "w"
        else:
            tipo = "w"

        file = os.path.join(dir, arq)

        with open(file, tipo, encoding="utf-8") as f:
            f.write(linha)

def main():
    global valor

    contador = 0
    result = 0

    valor = int(input("digite um valor entre 1 e 10:"))

    while valor < 1 or valor > 10:
        valor = int(input("valor inválido amigo"))

    for contador in range (10):
        result = mult(valor, contador + 1)
        grava(contador, result)

dir = "/tmp/exercicios/"
arq = "exercicio34.txt"

os.makedirs(dir, exist_ok=True)
os.chmod(dir, 0o744)

if __name__ == "__main__":
    main()
