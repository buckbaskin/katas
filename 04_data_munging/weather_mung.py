first_line = True

datas = []

for line in open('./weather.dat', 'r'):
    # print(filter(bool, line.split(' ')))
    if first_line:
        categories = filter(bool, line.replace('*', ' ').split(' '))
        first_line = False
        continue
    if len(tuple(filter(bool, line.replace('*', ' ').split(' ')))) >= 3:
        datas.append(tuple(filter(bool, line.replace('*', ' ').split(' '))))

day = 0
max_temp = 1
min_temp = 2

min_delta = 100000
min_day = -1

for line in datas:
    delta = abs(float(line[max_temp]) - float(line[min_temp]))
    if delta < min_delta:
        min_delta = delta
        min_day = float(line[day])
print('%d ... only %f' % (min_day, min_delta,))

