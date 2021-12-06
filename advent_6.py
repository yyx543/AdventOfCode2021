inp = '''2,3,1,3,4,4,1,5,2,3,1,1,4,5,5,3,5,5,4,1,2,1,1,1,1,1,1,4,1,1,1,4,1,3,1,4,1,1,4,1,3,4,5,1,1,5,3,4,3,4,1,5,1,3,1,1,1,3,5,3,2,3,1,5,2,2,1,1,4,1,1,2,2,2,2,3,2,1,2,5,4,1,1,1,5,5,3,1,3,2,2,2,5,1,5,2,4,1,1,3,3,5,2,3,1,2,1,5,1,4,3,5,2,1,5,3,4,4,5,3,1,2,4,3,4,1,3,1,1,2,5,4,3,5,3,2,1,4,1,4,4,2,3,1,1,2,1,1,3,3,3,1,1,2,2,1,1,1,5,1,5,1,4,5,1,5,2,4,3,1,1,3,2,2,1,4,3,1,1,1,3,3,3,4,5,2,3,3,1,3,1,4,1,1,1,2,5,1,4,1,2,4,5,4,1,5,1,5,5,1,5,5,2,5,5,1,4,5,1,1,3,2,5,5,5,4,3,2,5,4,1,1,2,4,4,1,1,1,3,2,1,1,2,1,2,2,3,4,5,4,1,4,5,1,1,5,5,1,4,1,4,4,1,5,3,1,4,3,5,3,1,3,1,4,2,4,5,1,4,1,2,4,1,2,5,1,1,5,1,1,3,1,1,2,3,4,2,4,3,1'''
lst = inp.split(",")
map_object = map(int, lst)

int_lst = list(map_object)

new_count = [0,0]
count = [0,0,0,0,0,0,0]

for idx in range(len(int_lst)):
    count[int_lst[idx]] += 1
day = 0
birth = 0
for i in range(256):
    tdy = count[day] + new_count[birth]
    new_count[birth] = count[day]
    count[day] = tdy
    if day == 6:
        day = 0
    else:
        day += 1
    if birth == 0:
        birth = 1
    else:
        birth = 0
    
    if i == 79:
        fish_count = 0
        for i in count:
            fish_count += i
        for i in new_count:
            fish_count += i
        print(f"Part 1: {fish_count}")
        
fish_count = 0
for i in count:
    fish_count += i
for i in new_count:
    fish_count += i
print(f"Part 2: {fish_count}")