import sys



if __name__=='__main__':

    if len(sys.argv)<2:
        read_str=input if sys.version_info.major>=3 else raw_input
        topic=read_str('help on ? ')
    else:
        topic=sys.argv[1]
    
    help(topic) 

    import threading


    help(threading.Thread.isDaemon)


