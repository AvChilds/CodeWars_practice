#create a function so that array [1,2,3,4] --> 1*2*3*4 = 24


def grow (arr):
    ans = 1
    for num in arr:
        ans *= num
    return ans

num_list = [1,2,3,4]
print (grow(num_list))