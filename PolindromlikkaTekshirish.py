# Massivni palindrom ekanligini tekshirish
def massivni_polindromlikka_tekshirish(massiv):
    n = len(massiv)
    for i in range(n // 2):
        if massiv[i] != massiv[n - 1 - i]:
            return False
    return True

A = [1, 2, 3, 2, 1]
elementsoni=int(input("Massiv elementlar sonini kiriting: "))
for i in range(elementsoni):
    element=int(input(f"Massivning {i+1}-elementini kiriting: "))
    A.append(element)
    
if massivni_polindromlikka_tekshirish(A):
    print("Massiv palindrom")
else:
    print("Massiv palindrom emas")
