def test(a=40,b=30,c=20,d=34):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test() # default agrument

def vik(a=20,b=1,d=45,c=40):
    print("A:",a,"B:",b,"C:",c,"D:",d)

vik(b=40,d=50) # key value pair argument#

def A(a,b,c,*d,**e):#arbitrary agrument *d mein tuple mein data store karna ho to use karte hai
    #or **e tab use karte tab hume data dictnory mein  store karna ho to. 
    print("A:",a,"B:",b,"C:",c,"D:",d,"E:",e) 

A(1,2,3,4,5,6,8,9,x=10,z=15,)
