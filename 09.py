import matplotlib.pyplot as plt
import numpy as np

# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть,
# zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(ks)
# с интерцептом
b1 = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) - np.mean(zp) ** 2)
b0 = np.mean(ks) - b1 * np.mean(zp)
y_pred = b0 + b1 * zp
# без интерцепта
zp = zp.reshape((-1, 1))
ks = ks.reshape((-1, 1))
b2 = np.dot(np.linalg.inv(np.dot(zp.T, zp)), np.dot(zp.T, ks))
y_pred1 = b2 * zp

plt.scatter(zp, ks)
plt.plot(zp, y_pred, 'b', label='с intercept')
plt.plot(zp, y_pred1, 'r', label='без interсept')
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг', rotation=90)
plt.legend()
plt.show()


# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

def mse_(b1, y=ks, X=zp, n=10):
    return np.sum((b1 * X - y) ** 2) / n


alpha = 1e-6
b1 = 0.1
print('Задание 2')
for i in range(1000):
    fp = (1 / n) * np.sum(2 * (b1 * zp - ks) * zp)
    b1 -= alpha * fp
    if i % 100 == 0:
        print(f'Итерация: {i}, b1: {b1}, mse: {mse_(b1)}')
print("Коэффициент линейной регрессии 5.8898")

# 3. Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно
# производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого
# во время одной итерации).

def mse_1(b0, b1, y=ks, X=zp, n=10):
    return np.sum((b0 + b1 * X - y) ** 2) / n


alpha = 5e-5
b0 = 0.1
b1 = 0.1
print('Задание 3')
for i in range(1000000):
   # y_pred3 = b0 + b1 * zp
    b0 -= alpha * (2 / n) * np.sum((b0 + b1 * zp - ks))
    b1 -= alpha * (2 / n) * np.sum((b0 + b1 * zp - ks) * zp)
    if i % 100000 == 0:
        print(f"Итерация: {i}, b1: {b1}, b0: {b0}, mse: {mse_(b0, b1)}")
print("Коэффициент линейной регрессии 2.6205, интерцепт 444.1773")