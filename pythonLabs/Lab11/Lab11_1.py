import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
food = [14.4, 12.1, 16.9, 14.5, 15.6, 13]
utility = [6.9, 5.2, 6.9, 6.3, 6.7, 5.4]
car_maintenance = [5, 5.5, 5.1, 4.4, 3.4, 4.2]
loan_repayment = [3, 3, 3, 4, 3, 3]
other_expenses = [0.4, 2.6, 5.8, 0.8, 6.6, 7.5]

# Creating the bar graph
fig, ax1 = plt.subplots()

ax1.set_xlabel('Месяц')
ax1.set_ylabel('Тыс.руб')
ax1.bar(months, food, color='lightsteelblue', label='Продукты')
ax1.tick_params(axis='y')

# Creating the line graph
ax1.plot(months, utility, color='blue', label='Коммунальные платежи')
ax1.plot(months, car_maintenance, color='red', label='Обслуживание автомобиля')
ax1.plot(months, loan_repayment, color='yellow', label='Выплата кредитов')
ax1.plot(months, other_expenses, color='magenta', label='Прочие расходы')


fig.tight_layout()
plt.title('Динамика расходов за первое полугодие')
plt.legend()
plt.show()