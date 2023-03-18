num_days = int(input('Num days--> '))
days_list = []

for i in range(num_days):
    day = int(input('Day--> '))
days_list.append(day)

max_len = 0
temp_count = 0
for temp in days_list:
    if temp > 0:
        temp_count += 1
else:
    if temp_count > max_len:
        max_len = temp_count
    temp_count = 0

print(max_len)
