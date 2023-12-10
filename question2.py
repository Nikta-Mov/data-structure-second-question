def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j]['first_name'] < data[min_index]['first_name']:
                min_index = j
            elif data[j]['first_name'] == data[min_index]['first_name']:
                if data[j]['last_name'] < data[min_index]['last_name']:
                    min_index = j
                
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    
    return data

names = [
    {'first_name': 'Nikta', 'last_name': 'Movahednia'},
    {'first_name': 'Maryam', 'last_name': 'Shirazi'},
    {'first_name': 'Maryam', 'last_name': 'Zahedi'},
    {'first_name': 'Hossein', 'last_name': 'Mohammadi'},
    {'first_name': 'Zahra', 'last_name': 'Ahmadi'},
    {'first_name': 'Reza', 'last_name': 'Dadgar'},
]

sorted_names = selection_sort(names)

for name in sorted_names:
    print(f"{name['first_name']} {name['last_name']}")