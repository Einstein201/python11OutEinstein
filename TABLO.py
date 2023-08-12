nonb=0



while (nonb < 1 or nonb>10):
    nonb= int (input ("Antre nonb lan: "))


print("Tablo miltiplikasyon pou", nonb, ":")

for i in range(1, 11):
        rezilta = nonb * i
        print(nonb, "x", i, "=", rezilta)
    

rejenere = input("eske w vle  jenere yon lòt tablo? (W/N): ")


#if rejenere.upper() != "W":
     ##   break

   