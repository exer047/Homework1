a = float(input('Enter a:'))
b = float(input('Enter b:'))
f = float(input('Enter f:'))

result = (a + b - f / a) + (f * a * a) - (a + f**2)
# в задании не было закончена функция поэтому я в конце добавил f**2

print('Result:' + str(result))
