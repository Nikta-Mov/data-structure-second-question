import matplotlib.pyplot as plt
import numpy as np
import random
import string
import time

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

    def generate_random_names(size):
    names_list = []
    for _ in range(size):
        first_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        last_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        names_list.append({'first_name': first_name, 'last_name': last_name})
    return names_list

sizes = range(10, 1001, 10)  
times = []

for size in sizes:
    random_names = generate_random_names(size)
    start_time = time.time()
    selection_sort(random_names)
    end_time = time.time()
    times.append(end_time - start_time)

    plt.plot(sizes, times, marker='o')
plt.title("Selection Sort Execution Time")
plt.xlabel("Data Size")
plt.ylabel("Time in seconds")
plt.show(500)