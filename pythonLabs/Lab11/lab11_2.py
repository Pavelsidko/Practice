import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
food = [14.4, 12.1, 16.9, 14.5, 15.6, 13]
utility = [6.9, 5.2, 6.9, 6.3, 6.7, 5.4]
car_maintenance = [5, 5.5, 5.1, 4.4, 3.4, 4.2]
loan_repayment = [3, 3, 3, 4, 3, 3]
other_expenses = [0.4, 2.6, 5.8, 0.8, 6.6, 7.5]

fig, ax = plt.subplots()
plt.title('Динамика расходов')
ax.set_xlabel('тыс.руб')


ax.barh(months, food, color='lightskyblue', label='Питание')

ax.barh(months, utility, left=food, color='lightgreen', label='Коммунальные платежи')

ax.barh(months, car_maintenance, left=[food[i] + utility[i] for i in range(len(months))], color='salmon', label='Обслуживание авто')

ax.barh(months, loan_repayment, left=[food[i] + utility[i] + car_maintenance[i] for i in range(len(months))], color='khaki', label='Кредиты')

ax.barh(months, other_expenses, left=[food[i] + utility[i] + car_maintenance[i] + loan_repayment[i] for i in range(len(months))], color='pink', label='Прочие расходы')

plt.legend()
plt.show()
