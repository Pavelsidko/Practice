import matplotlib.pyplot as plt

# Данные из таблицы
categories = ["Продукты питания", "Коммунальные платежи", "Обслуживание автомобиля", "Выплата кредитов", "Прочие расходы"]
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"]

expenses = {
    "Продукты питания": [14.4, 12.1, 16.9, 14.5, 15.6, 13],
    "Коммунальные платежи": [6.9, 5.2, 6.9, 6.3, 6.7, 5.4],
    "Обслуживание автомобиля": [5, 5.5, 5.1, 4.4, 3.4, 4.2],
    "Выплата кредитов": [3, 3, 3, 4, 3, 3],
    "Прочие расходы": [0.4, 2.6, 5.8, 0.8, 6.6, 7.5]
}

# Построение круговых диаграмм для каждой категории
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
fig.suptitle('Круговые диаграммы расходов за первое полугодие', fontsize=16)

for i, (category, ax) in enumerate(zip(categories, axes.flatten())):
    total_expenses = sum(expenses[category])
    ax.pie(expenses[category], labels=months, autopct=lambda p: f'{p:.1f}%', startangle=90)
    ax.set_title(category)

# Отображение круговых диаграмм
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
