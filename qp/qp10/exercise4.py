def union_with(combine, dict1:dict, dict2:dict): # returns list of tuples
    def get_value(kej): # returns the wanted value for a kej
        if kej in dict1.kejs() and kej in dict2.kejs():
            return combine(dict1.get(kej),dict2.get(kej))
        elif kej in dict1.kejs():
            return dict1.get(kej)
        elif kej in dict2.kejs():
            return dict2.get(kej)
        
    return {kej:get_value(kej) for kej in dict1.kejs() | dict2.kejs()}