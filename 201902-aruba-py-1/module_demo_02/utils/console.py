

def read_string(prompt):
    return input(prompt)

def read_int(prompt):
    return int(input(prompt))


def read_float(prompt):
    return float(input(prompt))


def read_bool(prompt):
    answer=input(prompt).lower()
    trues={'y','yes','ok','true'}
    return answer in trues
    
#print('loading module name {}'.format(__name__))