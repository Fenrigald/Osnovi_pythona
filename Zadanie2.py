my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_list = my_list[::-1]

for i in my_list:
    if my_list[my_list.index(i)].isdigit() == True and my_list[my_list.index(i)].startswith('"') == False:
        my_list.insert(my_list.index(i)+1, '"')
    elif my_list[my_list.index(i)].isdigit() == False and my_list[my_list.index(i)].startswith('+') == True:
        my_list.insert(my_list.index(i) + 1, '"')

my_list = my_list[::-1]

for i in my_list:
    if my_list[my_list.index(i)].isdigit() == True and my_list[my_list.index(i)].startswith('"') == False:
        my_list.insert(my_list.index(i)+1, '"')
        if len(i) == 1:
            my_list[my_list.index(i)] = '0' + i
    elif my_list[my_list.index(i)].isdigit() == False and my_list[my_list.index(i)].startswith('+') == True:
        my_list.insert(my_list.index(i) + 1, '"')

message= ' '.join(my_list)
print(message)