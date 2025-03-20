#Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade (s1,s2,s3):
    average =  (s1 + s2 + s3) / 3
    if 90 <= average <=100:
        return "A"

    elif  80<= average < 90:
        return "B"

    elif 70 <= average < 80:
        return "C"

    elif 60 <= average  < 70:
        return "D"

    else:
        return "F"


print (get_grade(42, 55, 60))


def sum_total(num):
    res = 0
    for i in range (1, num+1):
        res += i
    return res

print (sum_total(10))







