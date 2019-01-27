#class method 1
class shop:
    sname='chennai silks'
    address='gandhi nagar,hosur,krishnagiri(dt),tamilnadu(st)'
    contactno=9998765432

    def __init__(self,name,phoneno,card='no'):
        self.name=name
        self.phoneno=phoneno
    
    def disp(self):
        print('name of the shop:',self.sname)
        print('addres of the shop:',self.address)
        print('contactno of shop:',self.contactno)
        print('name of the customer:',self.name)
        print('phoneno of the customer:',self.phoneno)

    @classmethod
    def modify(cls):
        shop.sname='ARSS'
        shop.address='jivan nagar,hosur,tamilnadu'
        shop.contactno=9678543219
shop.modify()  
obj1=shop('ram',9876543210)
obj2=shop('midhu',9876654321)
obj1.disp()
print()
obj2.disp()
    
