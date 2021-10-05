# exercise type conversion
birth_year = input('what year were you born? ')
age = 2021 - int(birth_year)
print(f'you are {age}')

# exercise password checker
username = input('username: ')
password = input('password: ')
password_length = len(password)
encrypted_password = password_length*'*'
print(f'Hi {username}, your password {encrypted_password} is {password_length} letters long')
