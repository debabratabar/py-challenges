class Node:

    def __init__(self,data ,next=None):
        self.data = data 
        self.next = next 

    
class SinglyLinkedList:

    def __init__(self,head = None):
        self.head = head

    def insertBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node




    def insertEnd(self,data):

        t1 = self.head 
        new_node = Node(data)



        while ( t1.next != None) :
            t1 =t1.next

        t1.next = new_node 


    def insertMid(self,data , pos ):
        t1 = self.head 
        # prev = self.head 
        new_node = Node(data)



        while ( t1.next != None) :
            if  t1.data == pos :
                new_node.next = t1.next
                t1.next = new_node  
                break             

            # prev = t1     
            t1 =t1.next
        
    

    def deleteNode(self,data):
        t1 = self.head 
        prev = self.head 

        if t1.data == data : 
            self.head = t1.next 
            return
        

        while ( t1.next != None) :
            # print(f"{prev.data} - {t1.data}")
            if  t1.data == data :
                prev.next = t1.next 
                return             
            else:
                prev = t1     
                t1 =t1.next

        if t1.data == data : 
            prev.next = None 
        


    def printLL(self):
        t1 = self.head

        while(t1.next!=None):
            print(f"{t1.data}-> ",end='')
            t1 = t1.next

        print(f"{t1.data}")






sll1 = SinglyLinkedList()
sll1.insertBegin(5)
sll1.insertBegin(4)
sll1.insertBegin(3)
sll1.insertBegin(2)
sll1.insertBegin(1)
sll1.insertEnd(6)
sll1.insertEnd(7)
sll1.insertBegin(0)
# sll1.insertMid(4,5)

sll1.deleteNode(5)


sll1.printLL()

        