


input_file = "inputs/input_d1.txt"
l1 = []
l2 = []
with open(input_file, 'r') as f:
    for line in f:
        t1, t2 = line.split()
        l1.append(int(t1))
        l2.append(int(t2))
l1.sort()
l2.sort()
dist = 0
for t1, t2 in zip(l1, l2):
    dist += ((t2-t1)**2)**.5

print("Part 1:", dist)


p1 = 0 
p2 = 0
sim_score = 0
while p1 < len(l1) and p2 < len(l2):
    p12=p1
    while p12 < len(l1) and l1[p1]==l1[p12]:
        p12+=1
    while p2 < len(l2) and l2[p2]<l1[p1]:
        p2+=1
    p22 = p2
    while p22 < len(l2) and l2[p22]==l1[p1]:
        p22+=1
    count_l1 = p12-p1
    count_l2 = p22-p2
    count_t = l1[p1]
    sim_score += count_t * count_l2 * count_l1
    p1 = p12
    p2 = p22

    

print("Part 2:", sim_score)