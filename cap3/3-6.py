# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger 
# dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list

# Starting with guest list from Exercise 3-5
guestList = ['Jhow', 'Daniel', 'Vitor', 'Gabriel', 'Tatinho', 'Lucas']

# Print message about bigger table
print("Good news, everyone! I found a bigger dinner table!")

# Add three new guests to the list
guestList.insert(0, 'Amanda')
guestList.insert(4, 'Julia')
guestList.append('Fernanda')

# Print new set of invitation messages
for guest in guestList:
    print("Dear " + guest + ", you are invited to my dinner party!")
