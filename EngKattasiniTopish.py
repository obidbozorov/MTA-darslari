# # Eng katta elementni topish
# def eng_katta_element(A):
#     if not A:
#         return None
#     max_element = A[0]
#     for element in A:
#         if element > max_element:
#             max_element = element
#     return max_element

# # Foydalanish
# massiv = [3, 17, 2,8,12, 9, 1]
# print("Eng katta element:", eng_katta_element(massiv))  
# massiv = [3, 17, 2, 8, 12, 9, 1]
# olib_tashlanadigan = [2, 8, 9]
# for x in olib_tashlanadigan:
#     massiv.remove(x)
# print(massiv)  
# Tartib muhim bo'lmasa — O(1)
# massiv = [3, 17, 2, 8, 12, 9, 1]
# i = 2  # Misol uchun, 2-indexdagi elementni olib tashlash
# massiv[i] = massiv[-1]
# massiv.pop()
# print(massiv)  # Natija: [3, 17, 1, 8, 12, 9]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print("Linked List:", head.data)  # 10 -> 20 -> 30 -> None
cur = head
while cur is not None:
    print(cur.data, end=' -> ')
    cur = cur.next

print('None')  # 10 -> 20 -> 30 -> None
