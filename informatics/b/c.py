V = int(input())
Axxx = V // 1000            # цифра на позиции тысяч
xBxx = V % 1000 // 100      # цифра на позиции сотен
xxBA = xBxx * 10 + Axxx     # зеркальное двузначное число из цифр сотен и тысяч
xxCD = V % 100              # младшая (правая) половина числа
symmetry = xxBA - xxCD      # если 0 - то исходное число симметрично
print(symmetry + 1)         # выведет 1 если symmetry = 0, иначе будет другое число