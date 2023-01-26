import random
def A1():
    print("1/A:")
    szam=random.randint(1,50)
    print("     generált szám:{}".format(szam))
    return szam
def B1(szam):
    print("1/B:")
    if not (szam%5==0 and szam%3)==0:
        if szam%5==0:
         print("        a szám osztható öttel")
        elif szam%3==0:
            print("     A szám hárommal  osztható!")
    if szam % 5 == 0 and szam % 3 == 0:
        print("A szám öttel és hárommal is osztható!")
    else:
        print("     egyikkel sem oszthato")