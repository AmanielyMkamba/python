
for i in range(0,150):
    print(i)

for v in range(5,1000,5):
    print(v)

for count in range(1,100):
    if count % 5 == 0:
        print("Coding")
        count += 1
    else:
        print("Coding Dojo")

odd_sum = 0
for odd_count in range(0,500000):
    if odd_count % 2 == 1:
        #print(odd_count)
        odd_sum += odd_count
        print(odd_sum)

for pos_num in range(2018,0,-4):
    print(pos_num)

low_num = 1
high_num = 10
mult = 3

for i in range(low_num, high_num):
    if i % mult == 0:
        print(i)