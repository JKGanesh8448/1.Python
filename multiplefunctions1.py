class multiplefunctions():
    def subfields():
        print("Subfields in AI are : ")
        lists=['Machine learning','Deep Learning','Natural Language processing','Time series analysis','Robotics','Data Science','Neural Networks ']
        for temp in lists:
            print(temp)
        
        
    def OddEven():
        num=int(input("Enter a number: "))
        if(num%2==1):
            print("The given number is odd")
        else:
            print("The given number is even")
            
    def agecategory():
        sex=input("Enter the Sex:")
        age=int(input("Enter the age: "))
        if(sex=='male'):
            if(age>=21):
                print("Eligible")
            else:
                print("Not Eligible")
        elif(sex=='female'):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")
            return
    
    def percentage():
        S1=int(input("Enter the Marks in English: "))
        S2=int(input("Enter the Marks in Tamil: "))
        S3=int(input("Enter the Marks in Maths: "))
        S4=int(input("Enter the Marks in Science: "))
        S5=int(input("Enter the Marks in Social: "))
        total=S1+S2+S3+S4+S5
        print("Your total Marks: ",total)
        percentage=total/500*100
        print("Percentage: ",percentage)
    
    def area_of_triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        area_of_triangle=Height*Breadth/2
        print("Area of a Triangle: ",area_of_triangle)
    def perimeter_of_triangle():
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        perimeter_of_triangle=Height1+Height2+Breadth
        print("Perimeter of a Triangle: ",perimeter_of_triangle)
        return
        
    def BMI():
        print("To calculate BMI of a person")
        name = input("Enter your name: ")
        height = int(input("Enter the height in cm: "))
        weight = int(input("Enter the weight in kgs: "))
        BMI = weight/(height/100)**2
        if BMI<18:
            print("Underweight")
        elif BMI<25:
            print("Healthy range")
        elif BMI<30:
            print("Overweight")
        elif BMI<35:
            print("Grade1 Obesity")
        elif BMI<40:
            print("Grade2 obesity")
        else:
            print("Grade3 orbit obesity")