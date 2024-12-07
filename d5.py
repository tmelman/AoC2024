import re
from typing import List
import numpy as np
input_file="inputs/input_d5.txt"

with open(input_file, 'r') as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    if lines[i]=="": div = i; break

checks = lines[:i]
reports = lines[i+1:]

def check_report(r):
    r_not_allowed = list(map(lambda x: f'{x[1]}|{x[0]}', zip(r[:-1],r[1:])))
    return len(set(r_not_allowed)-set(checks))==len(r_not_allowed)

def reorder(r):
    neworder = []
    all_pairs = [(a,b) for a in r for b in r if a!=b and a>b]
    possible = set(map(lambda x: f'{x[0]}|{x[1]}', all_pairs)).union(set(map(lambda x: f'{x[1]}|{x[0]}', all_pairs)))
    subset_checks = possible.intersection(set(checks))
    subset_starts = [c.split('|')[0] for c in subset_checks]
    counts = {ri: 0 for ri in r}
    counts = {ri: subset_starts.count(ri) for ri in r}
    counts = {v:k for k,v in counts.items()}
    neworder = [counts[len(counts)-i-1] for i in range(len(counts))]
    return neworder

total = 0
for r in reports:
    rsplit = r.split(',')
    if check_report(rsplit):
        total += int(rsplit[int(len(rsplit)/2)])

    

print(f"part 1: {total}")
total = 0
for r in reports:
    rsplit = r.split(',')
    if not check_report(rsplit):
       neworder = reorder(rsplit)
       total += int(neworder[int(len(neworder)/2)])
print(f"part 2: {total}")