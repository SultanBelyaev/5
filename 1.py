sistem = int(input())
number = int(input())
def perevod ( sistem,number ):
    proverka = False
    if number < 0 :
        proverka = True
        number *= -1
    a = ""
    while number > 0:
        a = str(number%sistem) + a
        number //= sistem
    if proverka:
        return"-" + a
    else:
        return a
while sistem != 2 and sistem != 8:
    print(" Могу переводить только во вторичную и восьмиричную систему :(")
    sistem = int(input("Введите заново:"))
a = perevod(sistem,number)
print(a)

