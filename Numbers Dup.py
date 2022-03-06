Num_One = int(input('Enter First Number: '))
Num_Two = int(input('Enter Second Number: '))
Num_Three = int(input('Enter Third Number: '))
Num_Four = int(input('Enter Fourth Number: '))
Num_Five = int(input('Enter Fifth Number: '))
Dup = [Num_One, Num_Two, Num_Three, Num_Four, Num_Five]
duplicate = 0

for i in range(0, len(Dup)):
    for h in range(i + 1, len(Dup)):
        if Dup[i] == Dup[h]:
            duplicate += 1

if duplicate == 0:
    print("ALL UNIQUE")
else:
    print("DUPLICATE")