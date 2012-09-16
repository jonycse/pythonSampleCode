'''
Eval evaluate expression, not statement
'''

v=5
print v
v=eval("v+5")
print v
#eval("print v") # It will not work
