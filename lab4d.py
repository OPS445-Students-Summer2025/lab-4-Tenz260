#!/usr/bin/env python3
# lab4d.py

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(text):
# SO here it accepts a string and returns its first five characters.
    return text[:5]

def last_seven(text):
# It accepts a string and returns its last seven characters.
    return text[-7:]

def middle_number(number):
# Turns the number into text and returns the 2nd and 3rd characters.
    s = str(number)
    return s[1:3]

def first_three_last_three(s1, s2):
# Takes the first 3 letters of s1 and last 3 letters of s2, then adds them.
   return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
