my_list = [1, 2, 3, 4]


def print_data(data):
    print(f"inside the function: {id(data)}")
    for data in data:
        print(data)

print(f"outside the function: {id(my_list)}")

print_data(my_list)