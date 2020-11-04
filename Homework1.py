name1 = input('Enter your name: ')
age1 = input('Enter your age: ')
gender1 = input('Enter your gender: ')

alldata1 = 'Hello! My name is ' + name1 + ". I'm " + age1 + " and I'm a " + gender1
print('1', alldata1)
alldata11 = '%s%s%s%s%s%s' % ('Hello! My name is ', name1, ". I'm ", age1, " and I'm a ", gender1)
print('2', alldata11)
alldata12 = "Hello! My name is {}. I'm {} and I'm a {}".format(name1, age1, gender1)
print('3', alldata12)

about_me_fstring = f"Hello! My name is {name1}. I'm {age1} and I'm a {gender1}"
print('4', about_me_fstring)

list_from_str = about_me_fstring.split(' ')
print('5', list_from_str)

print('6', type(list_from_str))

str_from_list = ' '.join(list_from_str)
print('7', str_from_list)

invert_about_me_fstring = about_me_fstring.swapcase()
print('8', invert_about_me_fstring)