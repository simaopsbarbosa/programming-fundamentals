def interleave(f1,f2):
    res = []
    
    file1_list = open(f1, "r").readlines()
    file2_list = open(f2, "r").readlines()
    
    for i in range(min(len(file1_list), len(file2_list))):
        res.append(file1_list[i])
        res.append(file2_list[i])

    return "".join(res)
