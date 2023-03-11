#insert:rear=rear+1-- we add new person at end of queue
#delete:front = front+1  --FIFO
class CircularQueue():
    def __init__(self,size):#initializing the class
        self.size = size
        self.queue = [None for i in range(size)]# we can use queue as [None]*size
        self.front = self.rear = -1#if queue is empty the rear equal to front equal to -1
    def enqueue(self,data):# enque operation

        if((self.rear+1)%self.size==self.front):
            print("queue is front\n")
        elif (self.front==-1): #indicates empty queue
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data# always we insert elements at end(tail) position
        else:
            #for next position of rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if(self.front==-1):
           print("queue is empty")
        elif(self.front == self.rear):
            temp=self.queue[self.front]
            self.rear = -1
            self.front= -1
            return temp
        else:
            temp=self.queue[self.front]
            self.front = (self.front+1)%self.size
            return temp
    def display(self):
        #condition for empty queue
        if(self.front == -1):
            print("queue is empty")
        elif(self.rear>=self.front):
            print("elements in the circular queue:",end = " ")
            for i in range(self.front,self.rear+1):
                print(self.queue[1],end = " ")
                print()
        else:
            print("elements in cicular queue are:",end = " ")
            for i in range (self.front,self.size):
                 print(self.queue[i], end = " ")
            for i in range(0,self.rear+1):
                print(self.queue[i], end = " ")
            print()
        if((self.rear+1)%self.size==self.front):
            print("queue is full")
obj = CircularQueue(5)
obj.enqueue(14)
obj.enqueue(22)
obj.enqueue(13)
obj.enqueue(-6)
obj.display()
print("deleted value=",obj.dequeue())
print("deleted value=",obj.dequeue())
obj.display()
obj.enqueue(9)
obj.enqueue(20)
obj.enqueue(5)
obj.display()
obj.enqueue(100)

       
                     
                  
              
            
           
