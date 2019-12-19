from lirc import RawConnection

conn = RawConnection()

def teclaMando():
       
    #get IR command
    #keypress format = (hexcode, repeat_num, command_key, remote_id)
    for i in range(10):
        try:
            keypress = conn.readline(.0001)
        except:
            keypress=""
                  
        if (keypress != "" and keypress != None):
                    
            data = keypress.split()
            sequence = data[1]
            command = data[2]
            
            #ignore command repeats
            if (sequence != "00"):
               return
            
            return(command)
