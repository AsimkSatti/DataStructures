"""
Asim Satti
HW5 Part 2 : list shuffle
Linkedlist 

"""

class DoublyLinkedList:
    
    class _Node:
        
        __slots__ = 'data', 'next', 'prior'
        def __init__(self, data=None, next=None, prior=None):
            """
            Field names as they are not being treated as private.
            """
            self.data = data
            self.next = next
            self.prior = prior


    class Iterator:
        """
        Used for tracking positions. Returned by __iter__.
        Passed to add_after.
        """
        def __init__(self, node, dll):
            self.position = node
            self.dll = dll
        def __next__(self):
            self.position = self.position.next
            if self.position == dll._trailer: raise StopIteration
            return self.position.data

    def __init__(self):
        """
        __init__: mark the list as empty.  Maintaining the size and a tail
        reference are conveniences.
        """
        self._header = self._Node()
        self._trailer = self._Node()
    
        self._header.next = self._trailer
        self._trailer.prior = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return self.Iterator(self._header, self)

    def add_back(self, item):
        """
        push: insert the item at the head of the list.
        """
        old_last = self._trailer.prior
        new_node = self._Node(item, self._trailer, old_last)
        self._trailer.prior = new_node
        old_last.next = new_node
        self._size += 1


    def listshuffle(self):
      
        half=(self._size)//2
        curr=self._header
        iterat=0
        iterat2=half
        numele=0
        lst=[]
        lst2=[]
        final=[]
        finalnum=0
    

        
        while(iterat!=half+1): #saving data from the first half of linklist to python list
            
            curr=curr.next
            numele+=1
            lst.append(curr.data)
            iterat+=1
            

        while(iterat2!=self._size):  #saving data from the second half of list to another python list
       
            lst2.append(curr.data)
            curr=curr.next
            iterat2+=1
            

        if(self._size%2==0):
            for elements in range(half):            #adds alternating elements into an array if size is even
                final.append(lst2[elements])
                final.append(lst[elements])
                
        else:                                       #adds alternating elements into an array if size is odd
            instance=0
            cap=0
            while(cap!=self._size):
                final.append(lst2[instance])
                cap+=1
                if(cap!=self._size):
                    final.append(lst[instance])
                    cap+=1
                instance+=1
           
        finalList=DoublyLinkedList()     #creates a DoublyLinked List
        for nodes in range(self._size):
         
            finalList.add_back(final[nodes])    #adds nodes with data attributes from final array

        for item in finalList:      #Displays new doublylinked list that is shuffled
            if(item is None):
                return 
            print(item, end=' ')
        





    def display(self):
        # Displays linkedlist
        curr=self._header
        while(curr is not None):
            print(curr.data, end=" ")
            curr=curr.next
    




        
if __name__ == '__main__':
    """

    Part 2
    
    """
    print("Part 2: \n\n")
    
   # Creates a doubly linked list and adds nodes 10 nodes in total

    print("Even lengthed List: ")    #Test if there are an even number of nodes
    
    dll = DoublyLinkedList()
    dll.add_back(1)
    dll.add_back(2)
    dll.add_back(3)
    dll.add_back(4)
    dll.add_back(5)
    dll.add_back(6)
    dll.add_back(7)
    dll.add_back(8)
    dll.add_back(9)
    dll.add_back(10)
    
    for item in dll:
        print(item, end=' ')    #1 2 3 4 5 6 7 8 9 10
    print("\n===========")
    print("ListShuffle: \n")
    
    dll.listshuffle()           # 1 6 2 7 3 8 4 9 5 10



    print("\n \n\n")


    

    print("Odd lengthed List: ")    #Test if there are an odd number of nodes
    #Creates a doubly linkedlist adds nodes (9 in total)
    dll2 = DoublyLinkedList()   
    dll2.add_back(1)
    dll2.add_back(2)
    dll2.add_back(3)
    dll2.add_back(4)
    dll2.add_back(5)
    dll2.add_back(6)
    dll2.add_back(7)
    dll2.add_back(9)
    dll2.add_back(10)

    dll2.display()               #1 2 3 4 5 6 7 9 10
    print("\n=============")
    print("ListShuffle: \n")
    dll2.listshuffle()            # 1 6 2 7 3 9 4 10 5
    
    
    
