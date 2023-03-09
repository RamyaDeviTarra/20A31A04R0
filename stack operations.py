# stack last in first out
stack = []
def push():
    element = int(input("enter the element:"))
    stack.append(element)#append  method used for add/push/insert new element 
    print(stack)
def pop_element():
    if not stack:
        print(" stack is empty")
    else:
        e = stack.pop()
        print("remove element")
        print(stack)
while True:
    print("select the opetion 1.push 2.pop 3.quit")#push-insert,pop-delete,peek-top element
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
         break
    else:
        print("enter the correct value")
    
