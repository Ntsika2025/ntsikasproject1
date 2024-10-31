class stash:
    
    def __init__(self):
        self.fisrtTerm = 0
        self.difference = 0
        self.numberOfDays = 0


    def stash_revenue(self, a, d, n):
        self.fisrtTerm = a
        self.difference = d
        self.numberOfDays = n


        sum1 = float(self.numberOfDays/2)
        sum2 = float(2*self.fisrtTerm +(self.numberOfDays -1)*self.difference)

        sum = round(sum1*sum2, 2)

        return sum
    

class simpleInterest:

    def __init__(self):
        self.principalAmount =0
        self.interest = 0
        self.period = 0

    def SI_revenue(self, pa, ir, p):
        self.principalAmount = pa
        self.interest = ir
        self.period = p   
        accumulation = float(self.principalAmount*pow((1 + self.interest/100), self.period))

        return round(accumulation, 2)  






test1 = stash()
test2 = simpleInterest()
print("Hello, this program calculates simple interent investiment in monthly time intervals and also calculates "
      "the stash of money from 10c 20c 30c and so on, and this 10c increment happens each day" 
      " for example 10c today and tomorrow 20c and 30c day after....\nSo choose the on the options below:\n")


def simple_iterest(user):
    if user ==1:
        print("Simple Interest, \nEnter the following")
        prA = float(input("Principal amount:"))
        interest = int(input("Interest e.g 12 for 12%:"))
        
        time = int(input("Months:"))
        return f'R{test2.SI_revenue(prA, interest, time)} after {test2.period} months'
        
def stashing(user):
    if user == 2:
        print("Stashing Money, \nEnter the following")
        Sa = int(input("Stash amount e.g 10 for 10c")) 
        csa = float(Sa/100)   
        prd = int(input("Days e.g 1 for day 1:"))
        return f"R{test1.stash_revenue(csa, csa, prd)} after {test1.numberOfDays} days"


user = int(input("Press 1 or 2 for option\n1.Simpmle Interest\n2.Stashing Money\n3.Exit\n"))

while user is not 3:
    if user == 1:
        print(simple_iterest(user))
        break

    elif user == 2:
        print(stashing(user))
        break
    
    else:
        raise ValueError("Input is invalid, sorry try again")
    
        








