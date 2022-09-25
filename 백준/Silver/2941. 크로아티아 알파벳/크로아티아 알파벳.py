c_l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()

for i in c_l:
    if i in text:
        text = text.replace(i, '$')

print(len(text))
