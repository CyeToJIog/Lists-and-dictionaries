#Работа со списками
my_list = ["apple" , "banan" , "apricot" , "kiwi" , "strawberry"]
print("Список: ",(my_list))
print("Первый и последний элементы списка: ",(my_list [0], my_list[4]))
print("С третьего до пятого элемент: ",my_list [2:5])
my_list[2] = "mango"
print("Измененный список: ",my_list)
#Работа со словорями
my_dict = {"apple": "яблоко", "banan": "банан"}
print("Словарь: ",my_dict)
print("Заданный ключ: ",my_dict["banan"])
my_dict["banan"] = "желтый"
print("Измененный словарь: ",my_dict)
