print('Добрый день! Введите данные для расчета.')
user_name = input('Введите имя:')
user_age = int(input('Введите возраст:'))


user_weight = float(input('Введите вес в килограммах:'))
user_height = float(input('Введите рост в метрах:'))

bmi = round(user_weight / (user_height ** 2), 1)

water_per_kg = 30
water_ml = user_weight * water_per_kg
water_needed = water_ml / 1000


print(f'Привет !, {user_name}, {user_age}, лет')
print(f'Индекс массы тела: {bmi}')
print(f'Норма воды в день: {water_needed}лМак')
print("Расчет окончен. Будьте здоровы!")
