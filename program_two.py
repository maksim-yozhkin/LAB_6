import matplotlib.pyplot as plt

def create_diagram(list_elem: list):
    list_ind = []
    for i in range(len(list_elem)):
        list_ind.append(i)
    list_color = []
    for i in range(len(list_elem)):
        if list_elem[i] == max(list_elem):
            list_color.append("red")
            plt.text(list_elem[i], i, str(list_elem[i]), color = "red")
        elif list_elem[i] < 0:
            list_color.append("blue")
        else:
            list_color.append("black")
    plt.barh(list_ind,list_elem, color = list_color)
    plt.title("Статистика по елементам списку")
    plt.xlabel("Значення елементів")
    plt.ylabel("Індекси елементів")
    plt.show()

try:
    with open("data_list.txt", "r") as file_list:
        list_elem = file_list.read()
        list_elem = eval(list_elem)
        print(list_elem)
except Exception as e:
    print(f"При роботі з файлом виникла помилка: {e}")
create_diagram(list_elem)
count_elem = 0
start_val = input("Введіть початкове граничне значення => ")
end_val = input("Введіть кінцеве граничне значення => ")
for i in range(len(list_elem)):
    if int(start_val) <= list_elem[i] <= int(end_val):
        count_elem += 1
list_max = []
for i in range(len(list_elem)):
    if list_elem[i] == max(list_elem):
        list_max.append(i)
end_ind = list_max[-1]
val_end_ind = list_elem[end_ind]
sum_elem = 0
for i in range(len(list_elem)):
    if i > end_ind:
        sum_elem += list_elem[i]
print(f"Кількість елементів в інтервалі [{start_val},{end_val}] становить {count_elem} елементів.")
print(f"Сума елементів списку, які розташовані після останнього елементу з максимальним значенням становить {sum_elem}")
list_nul = []
list_other = []
update_list = []
for i in range(len(list_elem)):
    if list_elem[i] == 0:
        list_nul.append(list_elem[i])
for i in range(len(list_elem)):
    if list_elem[i] != 0:
        list_other.append(list_elem[i])
list_other.sort(reverse = True)
update_list = list_nul + list_other
print("Змінений масив з нулями на початку та з відсортованими елементами після них за збиванням:")
print(update_list)
create_diagram(update_list)