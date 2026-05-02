class Student:
    def getdata(self,fname,lname):
        print("getdata called")
        self.f=fname
        self.l=lname
    def putdata(self):
        print("first name:",self.f)
        print("last name:",self.l)
s1=Student()
s1.getdata("vikas","kannojiya")
s1.putdata()
                                
