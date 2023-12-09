def find_treasure(pos, steps):
    # stopping condition
    if len(steps) == 0:
        return pos
    
    # tuples are immutable so convert into list
    pos = list(pos)
    
    # update using the last element of "steps"
    if steps[-1] == "up":
        pos[1] += 1
    if steps[-1] == "down":
        pos[1] -= 1
    if steps[-1] == "left":
        pos[0] -= 1
    if steps[-1] == "right":
        pos[0] += 1
    
    # convert back into tuple
    pos = tuple(pos)    
    
    # remove the last element of "steps"
    steps.pop()
    
    return find_treasure(pos, steps)
        
    
    
print(find_treasure((0, 0), ['up', 'up', 'left', 'right', 'up', 'up']))
print(find_treasure((0, 4), ['up', 'up', 'left', 'left', 'up', 'up']))
    