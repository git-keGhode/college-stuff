import time

def sender(data):
    for char in data:
        print("Sending the ",char)
        ack=reciver(char)
        
        if ack:
            print("Acknowledgemnt recived")
        else:
            print("Timeout")
        


def reciver(char):
    time.sleep(3)
    print("Reciver got",char)
    return True

# data=input("Enter the message-")
data=[1100,1110,1111,11001]
sender(data)