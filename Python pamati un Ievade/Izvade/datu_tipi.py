a = "5"
b = 5
c = 5.5
print(type(a))
print(type(b))
print(type(c))
print(a + a)

vards = input("Ievadi varoņa vārdu: ")
punkti = int(input("Ievadi bāzes punktus: "))
reizinatajs = float(input("Ievadi reizinātāju: "))
kopa = punkti * reizinatajs
print(vards, "ieguva", kopa, "punktus")

# kļūda radās desmitajā rindā.
# rakstot 1,5 arī bija ValueError, jo float funkcija pienem tikai punktu kā decimāldaļu atdalītāju, nevis komatu.
# tas kalpo kā atdalītājs, lai uzsāktu vairākus elementus sarakstos, funkciju argumentos vai izveidot datu struktūru, ko sauc par kortežu.