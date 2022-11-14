# liczby, które mają 9 jedynek w zapisie binarnym
numbers = [1023]*10
for i in range(10):
    numbers[i] -= 2**i

# wyrównywanie numerów butelek
tab = [0]*1023
sum = 0
for i in range(1023):
    if i in numbers:
        sum += 1
    tab[i] -= sum


def butelki(num , out = 0):
    sum = 0
    list = []

    # przechodzenie po osobach i butelkach
    for i in range(10):
        for j in range(1, 1006):

            # omijanie liczb (łącznie jest ich 5 mniejszych od 1006), które mają 9 jedynek w zapisie binarnym
            if j in numbers:
                continue

            # sprawdzanie czy na i-tym miejscu zapisu binarnego jest jedynka
            if int(j / (2 ** i)) % 2 == 1:
                if j == num:
                    sum += 1
                list += [j+tab[j]]

        # wypisywanie kto pije z których butelek
        if out:
            print("Osoba ", i+1, " pije z butelek o numerach: ", list)
        list = []
    return sum


max_res = 0

# przypisanie butelek
butelki(1, out = 1)

for i in range(1,1006):
    max_res = max(butelki(i),max_res)

# maksymalna liczba umierających osób
print(max_res)
