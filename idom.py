#read from txt file and store control flow graph
def read_cfg(file):
    entry = None
    n = None
    exit = None
    cfg = {}
    file = open(file,"r")
    lines = file.readlines()
    for line in lines:
        if(line[0]=='p'):
            line = line.strip()
            line_split = line.split(' ')
            n = line_split[1]
            entry = line_split[2]
            exit = line_split[3]
        if(line[0]=='e'):
            line = line.strip()
            line_split = line.split(' ')
            node = line_split[1]
            if node not in cfg:
                cfg[node] = []
            for i in range(2,len(line_split)):
                cfg[node].append(line_split[i])
    
    return n,entry,exit,cfg

#compute immediate dominator
def idom(n,entry,exit,cfg):
    dom = {}
    for node in range(1,n+1):
        dom[node] = []
        for dominator in range(1,n+1):
            dom[node].append(dominator)


n,entry,exit,cfg = read_cfg("./tests/cfg3.txt")
print(cfg)
