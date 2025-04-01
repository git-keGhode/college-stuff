# import asyncio

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main() :
#    data = int(input("Enter Packet Data : "))
#    print("Sending DataPacket",data)
#    send_data = asyncio.create_task(
#       say_after(3,data))
   
#    receive_data = asyncio.create_task(
#       say_after(5,data))
#    print("Packet Is Recived Send Another Packet",data)
   
#    await send_data
#    await receive_data
# asyncio.run(main())

import asyncio

async def receiver(delay, data):
    await asyncio.sleep(delay)
    print("Receiver: Packet received.")
    print("ACK sent.\n")

async def tintout():
    await asyncio.sleep(3600)
    print("Not Recived in Specified Time Duration")

async def retransmit(data):
   
   #  try :
   #      async with asyncio.timeout(3):
   #          await receiver(data)
   #  except TimeoutError:
    print("Retransmitting Packet",data)  
    
async def main():
    packet_data = input("Enter Packet Data (space-separated numbers): ")

    packets = packet_data.split()

    for packet in packets:
        print("\nSending Packet:",packet)

        
        try:
            await asyncio.wait_for(tintout(packet), timeout=1.0)
        except TimeoutError:
            print('timeout!')

        await receiver(5, packet)
        print("Packet is received, sending next packet...\n")

    print("All packets recived")

asyncio.run(main())