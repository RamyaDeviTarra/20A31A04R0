# single LL deletion at begining
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def __init__(self):
        self.head=None
    def delete_beg(self):
      temp=self.head
      self.head=temp.next
      temp.next=None
    def display(self):
      if self.head is None:
            print('list is empty')
      else:
            temp=self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp=temp.next
obj=SLL()
n1=Node(1)
obj.head=n1
n2=Node(2)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print(" ")
obj.delete_beg()
obj.display()
