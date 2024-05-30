immutable_var=(1,"cucumber",3,"cart",5)
print(immutable_var)
#Присвоили переменной immutable_var элементы разных типов данных
#immutable_var[1]="apple"
#print(immutable_var[1])
#Попытались заменить элемент "cucumber" на элеменнт "apple", но так как -
# - переменная immutable_var относится к типу 'tuple'.Элементы в нгутри типа 'tuple' не возможно заменить таким присвоением

mutable_list=["Pizza","Dakiri",23]
print(mutable_list)
#Присвоили переменной mutable_list тип список и различные элементы
mutable_list[0]="Paste"
mutable_list[1]="Negroni"
mutable_list[2]=1997
print(mutable_list)
#Заменили все элементы списка в переменной mutable_list