kantiteNot=0 

while (kantiteNot < 2):
    kantiteNot= int (input ("Antre kantite not ou vle f mwayen lan: "))


print("Ou pral k fe mwayen not pou  ", kantiteNot , " matye ")

notes =[] 


s=0
print("Antre not")
for i in range(kantiteNot):
        note = float(input())
        notes.append(note)
        s = s + note
        moy=s/kantiteNot
print("mwayen lan se ", moy)


if moy >=90:
    result = "A"
elif moy>= 80 and moy<90 :
    result = "B"
elif  moy>= 70 and moy<80:
    result = "C"
elif  moy>= 60 and moy<70:
    result = "D"
else:
    result = "F"

print("Klasifikasyon: ",result)

