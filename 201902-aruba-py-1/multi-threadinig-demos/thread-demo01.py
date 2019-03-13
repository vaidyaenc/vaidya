import thread
import time

#print(dir(thread))
#print(help(thread.start_new_thread))


def count_down(id,max):
    
    print('thread {} started'.format(id))
    while max>0:
        print('thread {} counts {}'.format(id,max))
        time.sleep(1)
        max-=1

    print('thread {} ends '.format(id))


def main():
    thread.start_new_thread(count_down,(1,20))    
    thread.start_new_thread(count_down,(2,15))
    raw_input('hit enter to exit')
   

if __name__=='__main__':
    main()



        
