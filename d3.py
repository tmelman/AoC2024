import re
input_file = "inputs/input_d3.txt"

with open(input_file, 'r') as f:
    instructions = f.readlines()

instructions = "".join(instructions)

def get_multiples(input_string):
    # Define the regex pattern for "mul(...)" with two integers separated by a comma
    pattern = r"mul\((\d+),(\d+)\)"
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    # Sum the product of the integers in each match
    total_sum = sum(int(a) * int(b) for a, b in matches)
    
    return total_sum

print('Part 1:', get_multiples(instructions))

def remove_disables(instructions):
    instructions = re.sub(r'don\'t\(\).*?do\(\)','',instructions,flags=re.DOTALL)
    instructions = re.sub(r'don\'t\(\).*?$','',instructions,flags=re.DOTALL)
    return instructions
f=re.findall(r'don\'t\(\).*do\(\)',instructions)
print('Part 2:', get_multiples(remove_disables(instructions)))
