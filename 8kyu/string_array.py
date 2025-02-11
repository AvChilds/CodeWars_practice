""""
Description:
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]
"""

def string_to_array (s):
    array = list(s.split(" "))
    return array

print (string_to_array("you are my sunshine"))