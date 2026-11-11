vards = input("Vārds: ")
hp = int(input("Dzīvības punkti: "))
jauda = float(input("Uzbrukuma jauda: "))
bojajums = hp * jauda
print(vards)
print(hp)
print(bojajums)
#ValueError: invalid literal for int() with base 10: '' pēc tam, kad ievadīju tukšu vērtību
#ValueError: could not convert string to float: 'abc' pēc tam, kad ievadīju burtus
#Tā ievade ir bīstamāka, kura rada ValueError: could not convert string to float: 'abc' pēc tam, kad ievadīju burtus, jo tā var radīt problēmas, ja lietotājs ievada nepareizu datu tipu.