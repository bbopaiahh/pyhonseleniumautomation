#object method
class shop:
    sname='chennai silks'
    address='hosur,krishnagiri(dt),tamilnadu(st)'
    contactno=9998765432
    
    def disp(self):
        print('name of the shop:',self.sname)
        print('addres of the shop:',self.address)
        print('contactno of shop:',self.contactno)
        print('name of the customer:',self.name)
        print('phoneno of the customer:',self.phoneno)

    def __init__(self,name,phoneno,card='no'):
        self.name=name
        self.phoneno=phoneno
    
obj1=shop('ram',9876543210)
obj2=shop('midhu',9876654321)
obj1.disp()
print()
obj2.disp()
    
