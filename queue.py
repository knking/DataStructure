queue=[]

def pus_queue(element):
    queue.append(element)

def pop_queue():
    if len(queue) ==0:
        print('queue is empty ')
    else:
        return queue.pop(0)

def display_queue():
    for i in range(len(queue)-1,-1,-1):
        print(queue[i],end=" ")
    print()

pus_queue(10)
pus_queue(20)
pus_queue(30)
pus_queue(40)
pus_queue(50)
display_queue()
pop_queue()
display_queue()
pus_queue(100)
display_queue()