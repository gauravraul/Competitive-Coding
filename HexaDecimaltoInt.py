#combine the row seperated by commas
# and then convert the Hexadecimal numbers to Integer
data = [
['00', '00', '00', '00', '00', '00', '00', '00'],
['00', '00', '00', '80', 'db', '80', 'a2', '7f'],
['ae', '05', '00', '00', '05', '00'],
['40', 'c0', '50', '6c'],
]

#''.join(items) will join a items of a list
#int(<Hexadeciaml String>, 16) ... will convert Hexadecimal to Int

#using List compehensions
new_range  = [int(''.join(i),16) for i in data]   

print(new_range)

