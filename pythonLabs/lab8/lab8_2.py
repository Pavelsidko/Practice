class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}"

    def evaluate(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    @property
    def has_real_roots(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        return discriminant >= 0

    def multiply_by_scalar(self, scalar):
        return QuadraticPolynomial(self.a * scalar, self.b * scalar, self.c * scalar)


# Создаем объект многочлена
p = QuadraticPolynomial(2, -3, 1)
# Выводим описание многочлена на экран
print(p) # 2x^2 - 3x + 1
# Вычисляем значение многочлена для аргумента x=1
print(p.evaluate(1)) # 0
# Проверяем, имеет ли многочлен действительные корни
print(p.has_real_roots) # True
# Умножаем многочлен на скаляр 2
q = p.multiply_by_scalar(2)
print(q) # 4x^2 - 6x + 2



# Создаем список из 3 объектов класса
polynomials = [QuadraticPolynomial(1, 2, 1), QuadraticPolynomial(2, -3, 1), QuadraticPolynomial(3, 0, 1)]

# Сохраняем данные в текстовый файл
with open("polynomials.txt", "w") as f:
    for p in polynomials:
        f.write(f"{p.a},{p.b},{p.c}\n")

# Добавляем в конец файла данные еще 2 объектов
with open("polynomials.txt", "a") as f:
    f.write("4,-4,1\n")
    f.write("-5,1,-3\n")

# Чтение данных из файла с помощью readline()
with open("polynomials.txt", "r") as f:
    line = f.readline()
    while line:
        a, b, c = map(int, line.strip().split(","))
        p = QuadraticPolynomial(a, b, c)
        print("readline " + str(p))
        line = f.readline()

# Чтение данных из файла с помощью read()
with open("polynomials.txt", "r") as f:
    data = f.read()
    lines = data.split("\n")
    for line in lines:
        if line:
            a, b, c = map(int, line.strip().split(","))
            p = QuadraticPolynomial(a, b, c)
            print("read " + str(p))

# Чтение данных из файла с помощью readlines()
with open("polynomials.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        a, b, c = map(int, line.strip().split(","))
        p = QuadraticPolynomial(a, b, c)
        print("readlines " + str(p))


import pickle

# Сохранение списка объектов в бинарный файл
with open("polynomials.pickle", "wb") as f:
    pickle.dump(polynomials, f)

# Чтение данных из бинарного файла
with open("polynomials.pickle", "rb") as f:
    data = pickle.load(f)
    for p in data:
        print("from binary " + str(p))

# Сохранение каждого объекта по отдельности в новый файл
for i, p in enumerate(polynomials):
    with open(f"polynomial_{i}.pickle", "wb") as f:
        pickle.dump(p, f)

# Чтение данных из неизвестного количества файлов
import os

files = os.listdir()
for filename in files:
    if filename.startswith("polynomial_") and filename.endswith(".pickle"):
        with open(filename, "rb") as f:
            p = pickle.load(f)
            print("from pickle " + str(p))


import shelve

# Сохранение данных в бинарный файл-хранилище
with shelve.open("polynomials_db") as db:
    for i, p in enumerate(polynomials):
        db[str(i)] = p

# Получение данных из бинарного файл-хранилища
with shelve.open("polynomials_db") as db:
    for key in db:
        print("from db " + str(db[key]))

# Обновление данных в бинарном файл-хранилище
with shelve.open("polynomials_db") as db:
    db["0"] = QuadraticPolynomial(2, 1, 1)

# Удаление данных из бинарного файл-хранилища
with shelve.open("polynomials_db") as db:
    del db["1"]