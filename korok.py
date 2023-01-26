def beker():
    lista=[]
    print("II/A, B, C:")
    i = 0
    while i<5:
        kor=int(input("adja meg a kort: "))
        if kor<=120 and kor >=0:
            lista.append(kor)
            i=i+1
    print("{}:{}:{}:{}:{}".format(lista[0],lista[1],lista[2],lista[3],lista[4]))
    return lista
def elso_idos(lista):
    i = 0
    nincs=True
    elso_idos_indexe=0
    while i<len(lista) and nincs :
        if lista[i]>70:
            elso_idos_indexe=i
            nincs=False
    return elso_idos_indexe
def konzolra_ir(elso_idos_indexe):
    szoveg =("	Első idős ember korának helye a listában:	Első idős ember korának helye a listában: {}".format(elso_idos_indexe))
    print(szoveg)
    return szoveg
def fajl_ir(szoveg):
    f=open("oreg.txt","w",encoding="UTF-8")
    f.write(szoveg)
    f.close()

