def test(a=40,b=30,c=20,d=34):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test()

def vik(a=20,b=1,d=45,c=40):
    print("A:",a,"B:",b,"C:",c,"D:",d)

vik(b=40,d=50)

def A(a,b,c,*d,**e):
    print("A:",a,"B:",b,"C:",c,"D:",d,"E:",e)
A(1,2,3,4,5,6,8,9,x=10,z=15,)
