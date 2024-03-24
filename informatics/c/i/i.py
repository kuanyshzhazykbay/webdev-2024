import math

a = int(input())
cnt = 0
sqrt_a = int(math.sqrt(a))
for i in range(1, sqrt_a + 1):
    if a % i == 0:
        cnt += 2  # Учитываем как i, так и a/i
if sqrt_a * sqrt_a == a:
    cnt -= 1  # Уменьшаем счётчик на 1, если a является квадратом целого числа
print(cnt)

