# Write a Python function that takes a string input. This string represents code. 
# It may have any number of characters in it, and the characters may be anything. 
# For our purposes, we'll ignore anything that isn't one of the following: [, ], {, }, (, ). 
# Your function definition looks like this:

# def bracket_matcher(input):
# The return value is a boolean. You should return True if the brackets are properly matched and nested, 
# otherwise False.

# Test Cases:
# Think you got it figured out? Run through the test cases below to make sure!

# create a list of open brackets and closed brackets
open_brackets = ["[", "{", "("]
close_brackets = ["]", "}", ")"]

# create a function that checks the string for parentheses
def bracket_matcher(stri):
  # code goes here
  # create an empty array to store objects
  stack = []
  for i in stri:
    if i in open_brackets:
      stack.append(i)
    elif i in close_brackets:
      pos = close_brackets.index(i)
      if ((len(stack) > 0) and (open_brackets[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        return False
  if len(stack) == 0:
    return True
  else:
    return False

print(bracket_matcher('abc(123)'))
# returns True

print(bracket_matcher('a[b]c(123'))
# returns False -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns True

print(bracket_matcher('a[bc(12]3)'))
# returns False -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns True

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns False -- improperly nested

print(bracket_matcher('()'))
# returns True

print(bracket_matcher('[]]'))
# returns False - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns True -- no brackets = correctly matched