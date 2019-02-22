
lastId=0

class Employee:
    def __init__(self,name,salary):
        global lastId
        lastId+=1
        self._id=lastId
        self._name=''
        self._salary=0
        
        self.name=name
        self.salary=salary
        
        
    @property
    def valid(self):
        return self._id>0 and self._salary>0 and len(self._name)>0
    
    @property
    def id(self):
        return self._id if self.valid else None
        
    @property
    def name(self):
        return self._name if self.valid else None
    
    @name.setter
    def name(self,value):
        if ' ' in value:
            self._name=value
            
    @property
    def salary(self):
        return self._salary if self.valid else 0
    
    @salary.setter
    def salary(self,value):
        if value > self.salary:
            self._salary=value
            
    
    def work(self):
        if self.valid:
            print('{} works as employee {}'.format(self.name,self.id))
        else:
            print('update your details before work can be assigned')
            
    def info(self):
        return 'Employee {}\t{}\t{}'.format(self.id,self.salary,self.name) \
        if self.valid else '<Invalid Employee>'