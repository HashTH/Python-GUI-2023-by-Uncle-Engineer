class Hotel:
    #constructor
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch

    #method
    def introduce(self):
        print(f'Hotel : {self.name} | Branch : {self.branch}')
    
    def changeBranch(self,new_branch):
        print(f'from : {self.branch}')
        self.branch = new_branch
        print(f'to : {self.branch}')
    
    def changeName(self, new_name):
        print(f'from : {self.name}') 
        self.name = new_name
        print(f'to : {self.name}')
    
    def delete(self):
        print(f'Delete {self.name} Successfully')
        del self

#Instance
Holi = Hotel('Holiday Inn','Pattaya')
Mari = Hotel('Bangkok Marriott Hotel','Sukhumvit')

print('...........Show Hotel.............')
Holi.introduce()
Mari.introduce()
print('.........Change Hotel Name........')
Holi.changeName('Hilton Hotels & Resorts')
print('........Change Hotel Branch.......')
Holi.changeBranch('Hua Hin')
print('.......Delete Marriott Hotel......')
Mari.delete()
print('...........Update Hotel...........')
Holi.introduce()
print('..................................')