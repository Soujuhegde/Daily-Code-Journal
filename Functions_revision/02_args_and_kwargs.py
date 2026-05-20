#using *args 
# *args -> multiple values
def total(*numbers):

    print(sum(numbers))

total(1, 2, 3, 4)

#using **kwargs
# **kwargs -> key value arguments
def student_details(**data):

    print(data)

student_details(name="Soujanya", age=21)