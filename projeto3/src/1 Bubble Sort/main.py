# Bubble Sort
# Matrícula Infração Gravidade (1..5) Infrator

bd = []


def bubble_sort():
    bdaux = bd.copy()

    for j in range(len(bdaux)):
        for k in range(len(bdaux) - 1 - j):
            if bdaux[k][0] > bdaux[k + 1][0]:
                bdaux[k], bdaux[k + 1] = bdaux[k + 1], bdaux[k]

    return bdaux


while 1:
    entrada = input().split("\t")

    if entrada[0] == "TCHAU":
        break

    if entrada[0] == "DIM_BD":
        for i in range(int(entrada[1])):
            bd.append(input().split("\t"))
        print("BD_ATUALIZADA")

    elif entrada[0] == "CONSULTA_MATRICULA":
        naoencontrou = 1
        for registro in bd:
            if entrada[1] == registro[0]:
                print(registro[1], registro[2], registro[3])
                naoencontrou = 0
        if naoencontrou:
            print("REGISTOS NAO ENCONTRADOS")
        print("FIM")

    elif entrada[0] == "CONSULTA_CONDUTOR":
        naoencontrou = 1
        for registro in bubble_sort():
            if entrada[1] == registro[3]:
                print(registro[0], registro[1], registro[2])
                naoencontrou = 0
        if naoencontrou:
            print("REGISTOS NAO ENCONTRADOS")
        print("FIM")

    elif entrada[0] == "CONSULTA_BD":
        for registro in bubble_sort():
            print(registro[0], registro[1], registro[2], registro[3])

        print("FIM")
