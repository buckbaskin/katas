first_line = True

datas = []

for line in open('./football.dat', 'r'):
    print(filter(bool, line.replace('-', ' ').split(' ')))
    if first_line:
        categories = filter(bool, line.replace('-', ' ').split(' '))
        first_line = False
        continue
    if len(tuple(filter(bool, line.replace('-', ' ').split(' ')))) >= 3:
        datas.append(tuple(filter(bool, line.replace('-', ' ').split(' '))))

team = 1
for_ = 6
against = 7

min_delta = 100000
min_team = '-1'

for line in datas:
    delta = (int(line[for_]) - int(line[against]))
    if delta < min_delta:
        min_delta = delta
        min_team = line[team]
print('%s ... only %f' % (min_team, min_delta,))

