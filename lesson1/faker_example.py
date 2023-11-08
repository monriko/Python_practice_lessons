from faker import Faker     #импортируем Faker

fake = Faker()              #создаем объект класса Faker

print(fake.name())            #выводим на экран сгенерированное имя
print(fake.email())           #выводим на экран сгенерированный email
