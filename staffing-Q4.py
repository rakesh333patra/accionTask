
class Staffing(object):
    
    def __init__(self,firstName,lastName,payRate,YearlyVac):
        self.firstname=firstName
        self.lastname=lastName
        self.payrate=payRate
        self.yearvac=YearlyVac
        
    def get_name(self):
        print self.lastname+","+self.firstname
    def get_pay_rate(self):
        print self.payrate
    def get_yearly_vacation(self):
        print self.yearvac
    
class Employee(Staffing):
    def __init__(self, firstName, lastName, payRate, YearlyVac):
        super(Employee, self).__init__(firstName, lastName, payRate, YearlyVac)
        
class Contractor(Staffing):
    def __init__(self, firstName, lastName, payRate, YearlyVac,agency):
        super(Contractor, self).__init__(firstName, lastName, payRate, YearlyVac=0)
        self.agency=agency
    def get_agency(self):
        print self.agency
        
class temporary(Contractor):
    def __init__(self, firstName, lastName, payRate, YearlyVac,agency):
        super(temporary, self).__init__(firstName, lastName, payRate, YearlyVac,agency)
        
   
        
        
if __name__=="__main__":
    firstName='rakesh'
    lastName='patra'
    payRate=34
    YearlyVac=20
    a1=temporary(firstName, lastName, payRate, YearlyVac,'accion')
    a1.get_name()
    a1.get_pay_rate()
    a1.get_yearly_vacation()
    a1.get_agency()