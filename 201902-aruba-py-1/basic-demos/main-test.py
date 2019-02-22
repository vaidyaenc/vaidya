def find_range(seq):
    #overwritten here
    print= (min(seq),max(seq)) #print overwritten in local
    #print('done') #print is a tuple here. not a function
    return print 

def create_range():

    min=int(input('min?'))  #input is the global input function
    max=int(input('max?'))
    return range(min,max)

# run the program
def main():
    input='hi' # local override
    repeat='y'
    while repeat=='y':
        values=create_range()
        range=find_range(values)
        print(range)    
        repeat=input('repeat') #overriden locally

main()