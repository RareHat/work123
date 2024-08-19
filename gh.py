import json

#terrariabasskibidiplanteras
with open("bd.json", 'r', encoding="utf-8") as file:
    data = json.load(file)
    print(data)

name = input("Введіть імя учня")





s = 0
count = 0

for element in data:
    if name == element["імя"]




        s += element['оцінка']
        count += 1

print(s/count)









