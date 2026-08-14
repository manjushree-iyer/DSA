# Control Statements

# Question: Take input of age and print output print eligible or not eligible for the drivers licsence

age = int(input())

if(age >= 18):
    test_result = input()
    if test_result == "Pass":
        print("Eligible for thedrivers licsence")
    else:
        print("Not eligible for thedrivers licsence")
else:
    print("Eligible for thedrivers licsence")

# Ternary Operator

age = int(input())
result = "Eligible" if age >= 18 else "Not eligible"
print(result)


# Question: Grade students on the basis of their marks

marks = int(input())

if marks >= 90 and marks <= 100:
    print("Grade = O")
elif marks >= 80 and marks <= 90:
    print("Grade = A")
elif marks >= 70 and marks <= 80:
    print("Grade = A")
elif marks >= 60 and marks <= 70:
    print("Grade = B")
elif marks >= 50 and marks <= 60:
    print("Grade = B")
elif marks >= 40 and marks <= 50:
    print("Grade = C")
else:
    print("Grade = F")

# Question: Print the degree of hotness or coldness wrt the given temperature

temp = int(input())

if temp <= 50 and temp >= 30:
    print("Hot")
elif temp <=29 and temp >= 10:
    print("Cold")
elif temp <=9:
    print(temp, "Extremely cold")
else:
    print("Enter a valid temperature")

