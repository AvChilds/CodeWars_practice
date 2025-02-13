#Write a function which converts the input string to uppercase.

def make_upper_case(s):
      upper_string = s.upper()
      print(upper_string)

make_upper_case("hello")

def make_upper_case2(string):
    word =""
    for letter in string:
        letter = letter.capitalize()
        word = word + letter
    print(word)
make_upper_case2("hello")


    # Code here