# question 1

def hello_name(user_name):
    print('hello_' + user_name + '!')

hello_name('USERNAME')

# # question 2

def first_odds():
    for i in range(51):
        x = 2*i-1
        print(x)

# question 3

def max_num_in_a_list(a_list):
    return max(a_list)

print(max_num_in_a_list(a_list=[58, 12, 45, 45342]))

# question 4

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 400 == 0:
            return True
        elif a_year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

print(is_leap_year(801))

# question 5

def is_consecutive(a_list):
    sorted_a_list = sorted(a_list)
    x = len(sorted_a_list) - 1
    for i in range(x):
        if sorted_a_list[i] == sorted_a_list[i+1] - 1:
            continue
        elif sorted_a_list[i] != sorted_a_list[i+1] - 1:
            return False
    return True

print(is_consecutive(a_list = [2,3,4,5,6,7]))
print(is_consecutive(a_list = (1,2,4,5)))
print(is_consecutive(a_list = (1,3,5,7,2,4,6)))
print(is_consecutive(a_list = [1]))






