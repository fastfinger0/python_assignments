input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

frequency_count = {}

for element in input_list:
    frequency_count[element] = frequency_count.get(element, 0) + 1

print(f"Frequency count: {frequency_count}") 