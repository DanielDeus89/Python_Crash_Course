# 2-3. Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”

name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'daniel'
last_name = 'deus'

full_name = (f'Hi, {first_name} {last_name}')

print(full_name.title())

name = 'daniel'
print(f'Hello {name.title()}')