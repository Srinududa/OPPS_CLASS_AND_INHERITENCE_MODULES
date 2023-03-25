# CLASS module
# --to assaign values to properties we need to use __init__    
#class == BLUE PRINT and #from blue print to real creation of PROCESS is Called INSTANCE

class Car:
    def __init__(self, color, speed, acceleration, tyre_friction):   # properties = attributes
        self.Color=color
        self.Speed=speed
        self.Acceleration=acceleration
        self.Tyre_riction=tyre_friction
    def default_test(self):                                           #actions = methods
        print(self)
Obj=Car("Red", 250, 10, 3)                                             #THIS IS CALLED === INSTANCING                                     
Obj.default_test()


result==== <__main__.Car object at 0x000002455A4BF3D0>


class Mobile:
    def __init__(self, model, camera):
        self.model=model
        self.camera=camera
    def make_call(self,number):
        print("calling..{}",number)
Obj=Mobile("Realme 5 Pro", "48MP")
Obj.make_call(960123455)


result===>>> calling..{} 960123455





class Car:
    def __init__(self, color, speed, acceleration, tyre_friction):  #<<<<<< # properties = attributes
        self.Color=color
        self.Speed=speed
        self.Acceleration=acceleration
        self.Tyre_riction=tyre_friction
    def default_test(self,model_name):          # <<<<<<<#actions = methods
        print(model_name)
Obj=Car("Red", 250, 10, 3)       #<<<<<< #THIS IS CALLED === INSTANCING        
Obj.default_test("SUZUKI Z")           #<<<<<this is method calling


result===>>> SUZUKI Z




class Water_tin:
    lit=25
    def output(self):
        print(self.lit)
Obj=Water_tin()
Obj.output()

result===>>> 25


class Car:
    color="Red"
    speed=250
    acceleration=10
    tyre_friction=3
    def Color(self):
        print(self.color)
    def Speed(self):
        print(self.speed)
    def Acceleration(self):
        print(self.acceleration)
    def Tyre_friction(self):
        print(self.tyre_friction)
Obj=Car()
Obj.Color()
Obj.Speed()
Obj.Acceleration()
Obj.Tyre_friction()



#Result >>>
#Red
#250
#10
#3





#CONSTRUCTORS MODULE-1

class Laptop:
    def __init__(self, company, ram, rom,):
        self.Company=company
        self.Ram=(ram)
        self.Rom=(rom)
    def price(self,money):
        print(money)
Obj=Laptop("HP","4gb", "512mb")
Obj.price(48500)

results>>>> 48500



#CONSTRUCTORS MODULE-2

class Laptop:
    def __init__(self, company, ram, rom,):
        self.Company=company
        self.Ram=(ram)
        self.Rom=(rom)
    def features(self):
        print(self.Company,self.Ram,self.Rom)
Obj=Laptop("HP","4gb", "512mb")
Obj.features()

results>>>> HP 4gb 512mb



# inheritance

#class names from parent class to child class


#>>>>>> 1. SINGLE INHERITENCE

class Bike:
    def color(self):
        print('Green')
class Model(Bike):
    def recent(self):
        print('2023')
feature=Model()
feature.color()
feature.recent()

results>>>> 
Green
2023



# inheritance

#class name from two parent classes into one child class

#>>>>>> 2. MULTIPLE INHERITENCE   

class Prof:
    def sir_name(self):
        print("BVR Mohar Rao")
class Teacher:
    def teacher_name(self):
        print("Tulasi")
class student_under(Prof,Teacher):
    def student_name(self):
        print("Jockey")
school=student_under()
school.sir_name ()
school.teacher_name()
school.student_name()

result>>>> 
BVR Mohar Rao
Tulasi
Jockey





# inheritance

#class names from one Grand parent into one parent class  into child class by passing method

#>>>>>> 3. MULTI LEVEL INHERITENCE   

class Car:
    def wheels(self):
        print("4")
class Auto(Car):
    def Wheels(self):
        print("3")
class Bike(Auto):
    def wheel(self):
        print("2")
tyres=Bike()
tyres.wheels()
tyres.Wheels()
tyres.wheel()

result>>>> 
4
3
2



# inheritance

#class names from one  parent into TWO child classes by passing method

#>>>>>> 3. Hierarchy  INHERITENCE  


class Boss:
    def salary(self):
        print("4 cr per year")
class Emplyee_one(Boss):
    def income(self):
        print("20 Lks per year'")
class Emplyee_two(Boss):
    def money(self):
        print("10 Lks per year")

Yearlyone=Emplyee_one()
Yearlytwo=Emplyee_two()

Yearlyone.salary() # Output: 4 cr per year
Yearlyone.income() # Output: 20 Lks per year

Yearlytwo.salary() # Output: 4 cr per year
Yearlytwo.money() # Output: 10 Lks per year




