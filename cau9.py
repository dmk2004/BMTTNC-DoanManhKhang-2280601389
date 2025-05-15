def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
    return False
number = int(input("nhập vào số cần kt:"))
if kiem_tra_so_nguyen_to(number):
    print(number,"là số nguyên tố")
else:
    print(number, "ko phải số nguyên tố")
    