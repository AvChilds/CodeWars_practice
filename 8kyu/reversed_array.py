"""Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]"""
#solution: create a list of integers.
# convert n to a str, apply map() to every item of the list and returns a map obj which is an iterator
# use reversed() function to reverse list

def digitize(n):
    num_list = list(map(int,str(n)))
    reverse_array =  list(reversed(num_list))
    print (reverse_array)
    return reverse_array

digitize(23546)

#solution 2
def digitize2(n):
    reversed_list = [int(x) for x in str(n)[::-1]]
    print (reversed_list)
    return reversed_list

digitize2(12354)


