#condition_is_true if condition else condition_is_false
is_fat = True
state = "fat" if is_fat else "not fat"
print(state)
#Output: falt

age = 10
is_old = 'true' if age>10 else 'false'
print(is_old)
#Output: false

#(if_test_is_false, if_test_is_true)[test]
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
# Output: Ali is fat
