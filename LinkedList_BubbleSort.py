"""

Asim Satti
BubbleSort
Linkedlist

"""

#Part 1

class linkedlist:
    #Singly LinkedList
    
    
    class Node:
        def __init__(self,data,next=None):
            self.data=data
            self.next=next
            
    def __init__(self,head=None):
        #Every list has a head prior and length
        self.head=None
        self.prior=None
        self.len=0
            
    def add(self,data):
        # adds nodes to the back of the list
        new_node=self.Node(data)
        if(self.head is None):
            self.head=new_node
        else:
            curr=self.head
            while(curr.next is not None):
                self.prior=curr
                curr=curr.next
            curr.next=new_node
        self.len+=1
            
    def remove(self,data):
        # removes nodes given data
        if(self.head.data==data):
            self.head=self.head.next
        else:
            curr=self.head
            while(curr.next.data!=data):
                curr=curr.next
            if(curr.next.data!=data):
                    print("you suck")
            else:
                    temp=curr.next
                    curr.next=curr.next.next
                    temp=None

                    
    def bubblesortV1(self):
        #Switches data attributes of nodes if next node is larger
        
        for nodes in range(0,self.len+1):        #for every node in list
            curr=self.head                       #redifine head if needed
            while(curr.next is not None):        #Each loop checks one node
                if(curr.data>curr.next.data):   
            
                    temp=curr.data               #Switches data with next node
                    curr.data=curr.next.data
                    curr.next.data=temp
                curr=curr.next              #move to next node

            
    def bubblesortV2(self):
        #Switches nodes if the next nodes data is larger
        
        curr=self.head
        for nodes in range(0,self.len+1):               #For every node in list
            curr=self.head
            while(curr.next is not None):                #Each loop checks one node
                if(curr.data>curr.next.data):
                    
                    if(curr is self.head):
                        self.head=self.head.next            #Checks if need to move head 
                        curr.next=self.head.next
                        self.head.next=curr
                    else:
                        temp=curr.next.next
                        self.prior.next=curr.next         #reconnects the linkedlist
                        curr.next.next=curr
                        curr.next=temp
                        
                        
                      
                curr=curr.next


        
    def display(self):
        #Displays every nodes data
        curr=self.head
        while(curr is not None):
            print(curr.data)
            curr=curr.next




def main():
    
    """

    PART 1
    
    """
    print("Part 1: \n\n")
    
    #Creating a linkedlist adding nodes to back
    print("Original Linked List: ")
    LL=linkedlist()
    LL.add(1)
    LL.add(2)
    LL.add(3)
    LL.add(4)
    LL.add(5)
    LL.remove(1)                  #removing / adding nodes nodes
    LL.remove(5)
    LL.add(18)
    LL.add(9)
    LL.add(7)
    
    LL.display()                # Displaying original Linked list:   2 3 4 18 9 7
    print("\n")
    
    print("BubbleSort Version 1: ")
    LL.bubblesortV1()           # Switches data with BubbleSortV1
    LL.display()                # Displays modified linked list:  2 3 4 7 9 18


    
    print('\n')
    print('\n')
    
    #Creates a new LinkedList
    print("Orginal Linked List: ")  
    BL=linkedlist()
    BL.add(10)
    BL.add(7)
    BL.add(5)
    BL.add(48)
    
    BL.display()           #Dsiplays orignal linkedlist: 10 7 5 48

    print('\n')
    
    print("BubbleSort Version 2: ")
    BL.bubblesortV2()           #Switches nodes with BubbleSortV2
    BL.display()                 # Displays modified linkedlist: 5 7 10 48

    print("\n")

    
    # Testing worst possible case if last number is smalles
    print("Worst Case :")
    N=linkedlist()
    N.add(30)
    N.add(20)
    N.add(10)
    N.add(1)
    N.display()             # displays Original linkedList: 30 20 10 1
    print("\n")
    print("BubbleSortV1: ")
    N.bubblesortV1()        # Switches data with BubblesortV1
    N.display()             #Displays modifified linkedlist: 1  10 20 30
    


   
    


    

main()
