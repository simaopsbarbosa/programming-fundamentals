def mail_merge(names, mail_template):
    res = []
    
    nameList = open(names, "r").readlines()
    template = open(mail_template, "r").read()
    
    for name in nameList:
        res.append(template.replace("<name>", name.replace("\n", "")))
    
    return res