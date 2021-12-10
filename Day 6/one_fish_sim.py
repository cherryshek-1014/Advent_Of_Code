
Days = 80
initial_age = 1

count = 0
age = initial_age
for i in range(0, Days):
    if age != 0:
        age -= 1
    else:
        age = 6
        count += 1

    print('After Day '+str(i+1)+'___'+'Age:' +
          f'{age}'+'___'+'N= '+str(count))
