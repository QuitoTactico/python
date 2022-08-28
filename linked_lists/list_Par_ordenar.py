class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def juntar(n1:Node,n2:Node):
    if(n1.next!=None):
        n1.next = juntar(n1.next,n2)
        return n1
    else: 
        n1.next = n2
        return n1
#------------------------ cut -----------------------------#

def largo(head: Node, i: int):
    if(head==None):return i
    return largo(head.next,i+1)
def imprimir(head : Node) -> None:
    while(head != None):
        print(head.val)
        head = head.next
def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(55)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    m1 = Node(1)
    m2 = Node(2)
    m3 = Node(3)
    m4 = Node(999)
    m5 = Node(6234)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    m4.next = m5
    '''n6 = Node(6)
    n7 = Node(7)
    n5.next = n6
    n6.next = n7'''
    print(largo(n1,0),"(Largo)")
    imprimir(n1)
    print("---")

#------------------------- cambiar -------------------------#
    n = juntar(n1,m1)
    imprimir(n)
main()