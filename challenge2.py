class Student:
    def __init__(self,name,phy,chm,bio):
        self.name = name
        self.phy = phy
        self.chm = chm
        self.bio = bio
        
    def Total(self):
        return self.phy+self.chm+self.bio
    
    def percentage(self):
        return (Student.Total(self) / 300) * 100
    
std = Student("Tejashri",80,90,40)

print("Total is: ",std.Total())
print("Percentage is: ",std.percentage())