def remove_leading(ip): # returns string
    ip = ip.split(".")
    for i in range(len(ip)):
        while ip[i].startswith("0") and len(ip[i]) > 1:
            ip[i] = ip[i][1:]
        
    return ".".join(ip)
    
print(remove_leading('255.024.01.01'))