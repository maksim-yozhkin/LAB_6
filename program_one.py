import random

list_elem = []
for i in range(48):
    list_elem.append(random.randint(-98, 98))
print("Початковий список: ")
print(list_elem)
max_elem = max(list_elem)
count_max_1 = list_elem.count(max_elem)
count_max_2 = random.choice([3,4])
count_max = count_max_2 - count_max_1
if(count_max > 0):
    list_ind_max = random.sample(range(len(list_elem)), count_max)
    for i in list_ind_max:
        list_elem[i] = max(list_elem)
list_nul = []
for i in list_elem:
    if i not in list_ind_max:
        list_nul.append(i)
list_ind_nul = random.sample(range(len(list_nul)),int(len(list_elem)*0.2))
for i in list_ind_nul:
    list_elem[i] = 0
print("\nОновлений список: ")
print(list_elem)
try:
    with open("data_list.txt", "w") as file_list:
        file_list.write(str(list_elem))
except Exception as e:
    print(f"При роботі з поточним файлом виникла помилка: {e}")