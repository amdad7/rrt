class node():
    def __init__(self,x,y):
        self.x=x
        self.y=y
def is_not_on_obs(node1,node2):
    global obscol
    try:
        ex1=(node2.y-node1.y)/(node2.x-node1.x)
    except:
        ex1='inf'    
    for i in obscol:
        try:
            ex2=(i[1]-node1.y)/(i[0]-node1.x)
        except:
            ex2='inf' 
        print(ex1,ex2)       
        if ex1==ex2:
            return 0
    return 1
obscol=[(1,1),(2,3),(4,5),(2,0)]
def test():
    n1=node(1,0)
    n2=node(4,0)
    print(is_not_on_obs(n1,n2))         
    
test() 