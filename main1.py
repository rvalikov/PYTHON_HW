# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

str=input("Введите трехзначное число: ")
if int(str)>99 and int(str)<999:
    
    print(str)
    print(type(str))
    sum=int(str[0])+int(str[1])+int(str[2])
    print(sum)
else:
    print(f"Ваше число {str} не трехзначное")
    




