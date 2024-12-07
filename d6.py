import re
import numpy as np
import time
input_file = "inputs/input_d6.txt"
with open(input_file, 'r') as f:
    lines = f.read().splitlines()

class Map:
    # head:Node = None
    dir:int=0
    map:np.array = None
    loc:list = None
    cycle_count:int = 0 
    rotmap = {'^':'>','>':'v','v':'<','<':'^'}
    def __init__(self, input_arr, dir=0):
        self.map=input_arr
        self.dir=0
        for i in range(len(input_arr)):
            for j in range(len(input_arr[0])):
                if input_arr[i][j] in ['^','>','<','v']:
                    self.loc=[i,j]
                    break

    def _walk_forward(self):
        cur_loc_sym = self._get_sym()
        newloc = self._get_next_square()
        # self._set_sym('X')
        self.loc = newloc
        self._set_sym(cur_loc_sym)
    def _get_next_square(self):
        cur_loc_sym = self.map[self.loc[0]][self.loc[1]]
        if   cur_loc_sym == '^': next_loc = [self.loc[0]-1, self.loc[1]]
        elif cur_loc_sym == '>': next_loc = [self.loc[0], self.loc[1]+1]
        elif cur_loc_sym == 'v': next_loc = [self.loc[0]+1, self.loc[1]]
        elif cur_loc_sym == '<': next_loc = [self.loc[0], self.loc[1]-1]
        return next_loc
    def _get_right_square(self):
        cur_loc_sym = self.map[self.loc[0]][self.loc[1]]
        if   cur_loc_sym == '^': next_loc = [self.loc[0], self.loc[1]+1]
        elif cur_loc_sym == '>': next_loc = [self.loc[0]+1, self.loc[1]]
        elif cur_loc_sym == 'v': next_loc = [self.loc[0], self.loc[1]-1]
        elif cur_loc_sym == '<': next_loc = [self.loc[0]-1, self.loc[1]]
        return next_loc
    def _check_right_syms(self):
        cur_loc_sym = self.map[self.loc[0]][self.loc[1]]
        if   cur_loc_sym == '^': 
            next_locs = self.map[self.loc[0]][self.loc[1]+1:] #[self.loc[0], [self.loc[1]+1]
        elif cur_loc_sym == '>': #next_loc = [self.loc[0]+1, self.loc[1]]
            next_locs = ''.join([self.map[i][self.loc[1]] for i in range(self.loc[0],len(self.map))])
        elif cur_loc_sym == 'v': #next_loc = [self.loc[0], self.loc[1]-1]
            next_locs = self.map[self.loc[0]][:self.loc[1]][::-1]
        elif cur_loc_sym == '<': #next_loc = [self.loc[0]-1, self.loc[1]]
            next_locs = ''.join([self.map[i][self.loc[1]] for i in range(0,self.loc[0])])[::-1]
        if "#" in next_locs:
            next_locs= next_locs.split('#')[0]+"#"
        if self.rotmap[self.rotmap[cur_loc_sym]]+'#' in next_locs:
            return True
        for l in next_locs: #next_locs:#.split('#')[0]: 
            if self.rotmap[cur_loc_sym] ==l: #in [l, "#"]:
                # print(self)
                print("Current:", cur_loc_sym, "; next:", next_locs, '; cycle')
                return True
        # print("Current:", cur_loc_sym, "; next:", next_locs) #.split('#')[0])
        return False
    def _set_sym(self,sym):
        loc = self.loc
        self.map[loc[0]] = self.map[loc[0]][:loc[1]]+sym+self.map[loc[0]][loc[1]+1:]
    def _get_sym(self,loc=None):
        if loc is None: loc = self.loc
        return self.map[loc[0]][loc[1]]
    def _rot90(self):
        self._set_sym(self.rotmap[self._get_sym()])
    def _blocked(self):
        next_square = self._get_next_square()
        return self._get_sym(next_square)=="#" 
    def step_check_cycles(self):
        # if self.rotmap[self._get_sym()] == self._get_sym(self._get_right_square())
        try:
            if self._get_sym(self._get_next_square()) == self._get_sym():
                return True
            self.step()
        except: return False
    def step(self):
        # if self._check_right_syms(): self.cycle_count+=1; #print(self) 
        # if self.rotmap[self._get_sym()] == self._get_sym(self._get_right_square()): return False #self.cycle_count+=1; #print(self)
        # else: print()
        if self._blocked(): self._rot90()
        else: self._walk_forward()
        # return True
    def can_step(self):
        newloc = self._get_next_square()
        if newloc[0] < 0 or newloc[0]>=len(self.map): return False
        if newloc[1] < 0 or newloc[1]>=len(self.map[0]): return False
        return True
    def eval(self):
        count = 0
        for row in self.map:
            # count += len(re.findall('X',row))
            count += len(re.findall('^',row))
            count += len(re.findall('>',row))
            count += len(re.findall('v',row))
            count += len(re.findall('<',row))
        return count+1
    def eval_cycles(self):
        return self.cycle_count
    
    def __str__(self):
        return '\n'.join(self.map)+'\n\n'
        
guardmap = Map(lines)
# print(map)
while guardmap.can_step(): 
    guardmap.step(); 
    # print(guardmap); 
    # time.sleep(.05)
    # input('Press Enter to continue')
# print(guardmap)
print('part 1:', guardmap.eval())
total = 0
for i in range(len(lines)):
    print(f"{i} of {len(lines)} rows")
    for j in range(len(lines[0])):
        if guardmap._get_sym([i,j]) in ['^','>','v','<']:
            newlines = lines
            newlines[i] = newlines[i][:j]+'#'+newlines[i][j+1:]
            new_map = Map(newlines)
            while(new_map.step_check_cycles()): total +=1
        
print('part 2:',total) # guardmap.eval_cycles())