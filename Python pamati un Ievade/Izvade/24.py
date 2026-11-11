print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 3)
mantas = int(input("Cik mantu ir? "))
somas_ietilpiba = int(input("Cik mantu ietilpst somā? "))
pilnas = mantas // somas_ietilpiba
pari = mantas % somas_ietilpiba
print(f"Vajag {pilnas} somas un {pari} mantas paliks pāri.")
videji = mantas / somas_ietilpiba
print(f"Vidēji {videji:.1f} somas")