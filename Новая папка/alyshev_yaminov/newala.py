# Задание 1
import json 
with open("data.json", "r") as json_fille:
    data = json.load(json_fille)
    print(data)

# Задание 2
book = { 
    "tittle" : "War and Peace",
    "author" : "Lev Tolstoy",
    "year_iznadnie" : 1867
}
with open("book.json","w",encoding="UTF-8") as json_fille:
    json.dump(book,json_fille,indent=2)

# Задание 3
with open('user_data.json', 'r') as fille:
    us1x = json.load(fille)
new_user = {
    "username": "user1",
    "email" : "user1@gmail.com"
}
us1x['users'].append(new_user)
with open('user_data.json', 'w') as fille:
    json.dump(us1x,fille,indent=4)

# Задание 4
import json
with open('products.json', 'r') as prodt:
    prd = json.load(prodt)
for  product in prd['products']:
    if product['price'] > 100:
        print(product['name'])

# Задание 5
import json
with open('school.json','r') as schkila:
    sch = json.load(schkila)
max_students = 0
class_max_stud = ""
for class_name,class_data in sch['classes'].items():
    num_stud = len(class_data['students'])
    print(f"В классе {class_name} -  {num_stud}-е учеников")
if num_stud > max_students:
    max_students = num_stud
    class_max_stud = class_name
print(f"Класс в котором больше всего учеников: {class_max_stud} ,а именно {max_students}")