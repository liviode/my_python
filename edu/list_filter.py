my_list = [123, 'artus', 'zürich', 22.476]

print('my_list', my_list)

filtered_list = [e for e in my_list if e != 123]

print('...after filtering')

print(my_list)

print(filtered_list)
