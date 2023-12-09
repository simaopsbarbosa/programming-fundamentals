def transitive_closure(r:set):
    comp = lambda r: {(x[1],y[1]) for x in r for y in r if x[1] == y[0]}
    def rec(r): 
        newr = comp(r)
        if not newr - r: return r
        return r | rec(r | newr)
    return rec(r)
 	

print(sorted(list( transitive_closure({(1,2), (2,3), (3,4)} ))))