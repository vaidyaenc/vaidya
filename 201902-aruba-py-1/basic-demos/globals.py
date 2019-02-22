


def my_range(min,max):
    # min max overwritten in this function 
    # but not outside
    result=[]
    count=min
    while count<max:
        result.append(count)
        count+=1
    return result

def find_range(seq):
    #overwritten here
    print= (min(seq),max(seq)) #print overwritten in local
    print('done')
    return print

def create_range():

    min=int(input('min?'))
    max=int(input('max?'))
    return my_range(min,max)

# run the program
input='hi' # global override
repeat='y'
while repeat=='y':
    values=create_range()
    range=find_range(values)
    print(range)    #overwritten within find_range that has already been called
    repeat=input('repeat') #overwritten globally








    