string_text = input('Enter string text: ')
line = 20 * 'X'
leng = len(string_text)

print(line)
print('X' + ' ' * int(9 - leng / 2 ) + string_text +' ' * int(9 - leng / 2 ) + 'X')
print(line)