from typing import List
input_file = "inputs/input_d2.txt"
reports: List[int] = []
with open(input_file, 'r') as f:
    for line in f:
        reports.append([int(n) for n in line.split()])

def safe(report: List[int]):
    dists = []
    for r1, r2 in zip(report[:len(report)-1], report[1:]):
        dists.append(r1-r2)
    if dists[0]<0: dists = [d*-1 for d in dists]

    for d in dists: 
        if d not in [1,2,3]: return 0
    return 1

n_safe = 0
for r in reports: n_safe += safe(r)

print("Part 1: ", n_safe)


def safe_dampener(report: List[int]):
    safe_d = safe(report)
    if safe_d==0:
        reports_d = [report[:idx]+report[idx+1:] for idx in range(len(report))]
        for r in reports_d:
            if safe(r)==1: 
                return 1
    return 0

for r in reports: 
    n_safe += safe_dampener(r)
print("Part 2: ", n_safe)
