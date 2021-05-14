import random,math
from matplotlib import pyplot as plt
from numpy import busday_count
class node():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return str(self.x)+','+str(self.y)    

class line():
    def  __init__(self,x1,x2,y1,y2):
        try:
            self.m=(y2-y1)/(x2-x1)
            self.c=y1-x1*(self.m)
        except:
            self.m='inf'
            self.c='nd'    
        self.p1=(x1,y1)
        self.p2=(x2,y2)
    
    def intsect(self,l2,xi,yi):
        pass
        
        
        
    def isnotcol(self,n1,n2):
        l2=line(n1.x,n2.x,n1.y,n2.y)      
        if self.m==l2.m:
            return 1
        elif self.m=='inf':
            self.xi=self.p1[0]
            self.yi=l2.m*self.xi+l2.c
        elif l2.m=='inf':
            self.xi=l2.p1[0]
            self.yi=self.m*self.xi+self.c  
        else:        
            self.xi=(l2.c-self.c)/(self.m-l2.m)
            self.yi=(self.m*l2.c-self.c*l2.m)
            #print(self.xi,self.yi)
        if self.xi>=min(self.p1[0],self.p2[0]) and self.xi<=max(self.p1[0],self.p2[0]):
           if self.xi>=min(l2.p1[0],l2.p2[0]) and self.xi<=max(l2.p1[0],l2.p2[0]):
                if self.yi>=min(self.p1[1],self.p2[1]) and self.yi<=max(self.p1[1],self.p2[1]):
                    if self.yi>=min(l2.p1[0],l2.p2[0]) and self.yi<=max(l2.p1[1],l2.p2[1]):
                        print(self.xi,self.yi,(self.m,self.c)) 
                        return 0
        
        return 1                
           
                   



def is_not_on_obs(node1,node2):
    global obslis
    for i in obslis:
        if i.isnotcol(node1,node2):
            continue
        else:
            #print(node1.x,node1.y,node2.x,node2.y)
            #print('hi',i.p1,i.p2)
            return 0
    return 1               
def dist(node1,p):
    return math.sqrt(((node1.x-p[0])**2)+((node1.y-p[1])**2))

def randpoint():
    x=random.randint(-1000,1000)
    y=random.randint(-1000,1000)
    return ((x,y))
       
def nearnode(p):
    global nodcol
    temp=float('inf')
    for i in nodcol:
        d=dist(i,p)
        if d<temp:
            temp=d
            np=i

    return ((np,temp))

def newnode(i,p):
    global delta
    #print('ttt',i,p)
    nod,d=i[0],i[1]
    x=((delta/(d-delta))*(p[0]-nod.x))+nod.x
    y=((delta/(d-delta))*(p[1]-nod.y))+nod.y
    #print(x,y)
    return ((round(x,0),round(y,0)))



if __name__=="__main__":
    nodcol,delta=[],5
    #gx,gy=map(int,input().split())
    plt.figure()

    #obstacle1
    j=40
    xlis,ylis=[],[]
    ylis=[i for i in range(-50,10)]
    xlis=[40]*len(ylis)
    plt.plot(xlis,ylis)
    ylis=[i for i in range(21,51)]
    xlis=[40]*len(ylis)
    plt.plot(xlis,ylis)
    
    #obstacle2
    xlis,ylis=[],[]
    j=-40
    
    ylis=[i for i in range(-50,-40)]
    xlis=[-40]*len(ylis)
    plt.plot(xlis,ylis)
    ylis=[i for i in range(-30,51)]
    xlis=[-40]*len(ylis)
    plt.plot(xlis,ylis)     

    xlis,ylis=[],[]
    #obstacle3        
    for i in [-50,50]:
        ylis=[]
        for j in range(-50,51):
            ylis.append(j)
        xlis=[i]*len(ylis)
        plt.plot(xlis,ylis)
        plt.plot(ylis,xlis)
    
    l1=line(-50,50,50,50)
    l2=line(-50,50,-50,-50)
    l3=line(40,40,-50,10)
    l4=line(40,40,20,50)
    l5=line(-40,-40,-50,-40)
    l6=line(-40,-40,-40,50)
    l7=line(50,50,50,-50)
    l8=line(-50,-50,50,-50)
    obslis=[]
    for i in [l1,l2,l3,l4,l5,l6,l7,l8]:
        obslis.append(i)
        print(i.m,i.c)
        
    
    beg=node(0,0)
    nodcol.append(beg)
    count,count1=0,0
    for i in range(int(input("number of nodes"))):
        
        delta=5
        p=randpoint()          
        n=nearnode(p)
        if n[1]==delta:
            delta=n[1]-1

        
        nn=newnode(n,p)
        ob=node(nn[0],nn[1])
        #print('ob',ob)
        #print(ob.x,ob.y)
        if not is_not_on_obs(ob,n[0]):
            #print('hi')
            #print(ob.x,ob.y)
            count+=1
            continue
        else :
            count1+=1
            nodcol.append(ob)
            plt.plot([(ob.x),(n[0].x)],[(ob.y),(n[0].y)])
            
        

                
        #print([(i.x,i.y) for i in nodcol])        
    #print(nodcol)
    xlis,ylis=[],[]
    for i in nodcol:
        xlis.append(i.x)
        ylis.append(i.y)
    plt.scatter(xlis,ylis)
    #plt.xlim([-gx,gx]) 
    #plt.ylim([-gy,gy])
    plt.show()
    print(count,len(nodcol),count1)
    print('done')
    a=node(0,60)
    b=node(0,-60)
    #print(l7.iscol(a,b))        
   