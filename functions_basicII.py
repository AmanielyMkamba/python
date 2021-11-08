# 1.Countdown pseudo_code
# create a function
# accept number as input
# return a list
# example: countdown(5) => [5,4,3,2,1,0]

def countdown(num):
    num_count = []
    for i in range(num, -1, -1):
        num_count.append(i)
    return num_count

# countdown(5)
# print(countdown(5))

# 2.Print and Return pseudo_code
# create a cunction
# input with list of two nubers
# print first value and return second
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list_nums):
    for i in (list_nums):
        print(list_nums[0])
        return(list_nums[1])

print(print_and_return([7,2]))

# 3.First Plus Length pseudo_code
# create a function
# accept/with list as input
# returns sum of first value + length of list
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list_nums):
    sum = 0
    for i in (list_nums):
        sum = list_nums[0] + len(list_nums)
    return sum

print(first_plus_length([1,2,3,4,5]))

# 4.Values Greater than Second pseudo_code
# create a function, that accept list
# create or return new list with values greater than 2nd value
# print how many values
# return new list
# if list has less than 2 elements retuern false
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(list_nums):
    new_list_nums = []
    for i in (list_nums):
        if len(list_nums) < 2:
            return False
    for i in (list_nums):
        if i > list_nums[1]:
            # print(i)
            new_list_nums.append(i)
    print(len(new_list_nums))
    return new_list_nums

print(values_greater_than_second([3]))
print(values_greater_than_second([5,2,3,2,1,4]))


# 4.This Length, That Value pseudo_code
# write a function, with two int as parameters(size, value)
# function return list lenghth equals size, and given values
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    new_length_and_value = []
    for i in range(size):
        new_length_and_value.append(value)
    return new_length_and_value

print(length_and_value(6,2))

