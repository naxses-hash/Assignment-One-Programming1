try:
    print("Please enter score1: ")
    s1 = float(input())
    print("Please enter score2: ")
    s2 = float(input())
    print("Please enter score3: ")
    s3 = float(input())
    if s1 >= 0 and s1 <= 100 and s2 >= 0 and s2 <= 100 and s3 >= 0 and s3 <= 100:
        average = (s1 + s2 + s3) / 3
        print("The average score is: " + str(average))
    else:
        print("Error: Invalid input. Please enter numerical values")
except ValueError:
    print("Error: Invalid input. Please enter numerical values")
