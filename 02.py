from math import factorial, exp


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def bernulli(n, k, p):
    combination = factorial(n) / (factorial(k) * factorial(n - k))
    return combination * (p**k) * (1 - p)**(n - k)


def puasson(m, n, p):
    lambd = p * n
    return (lambd**m) * exp(-lambd) / factorial(m)


# 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз,
# равна 0.8. Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

print(bernulli(100, 85, 0.8))

# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# а) Какова вероятность, что ни одна из них не перегорит в первый день?

print(puasson(0, 5000, 0.0004))

# б)Какова вероятность, что перегорят ровно две?

print(puasson(2, 5000, 0.0004))

# 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

print(bernulli(144, 70, 0.5))

# 4. В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# а) Какова вероятность того, что все мячи белые?

print((combinations(7, 2) / combinations(10, 2)) *
      (combinations(9, 2) / combinations(11, 2)))

# б) Какова вероятность того, что ровно два мяча белые?

print(((combinations(7, 2) / combinations(10, 2)) *
       (combinations(2, 2) / combinations(11, 2))) +
      ((combinations(3, 2) / combinations(10, 2)) *
       (combinations(9, 2) / combinations(11, 2))) +
      (((combinations(7, 1) * combinations(3, 1)) / combinations(10, 2)) *
       ((combinations(9, 1) * combinations(2, 1)) / combinations(11, 2))))

# в) Какова вероятность того, что хотя бы один мяч белый?

print(1 - ((combinations(2, 2) / combinations(10, 2)) *
           (combinations(3, 2) / combinations(11, 2))))
