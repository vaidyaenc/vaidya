
import sys
import threading

def main(name,args):
    t=threading.current_thread()
    print(t)
    print(t.name)
    

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])