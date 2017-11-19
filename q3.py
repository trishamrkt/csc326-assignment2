def my_map(func, iterable):
    result_map = [];
    
    # Iterate through all the elements in iterable
    # Apply func to each element 
    for elem in iterable: 
        new_elem = func(elem)
        result_map.append(new_elem)
        
    return result_map 

def my_reduce(func, iterable, initializer=None):
    return 

def my_filter():
    return 

if __name__ == "__main__":
    print my_map(lambda x: x**2, range(10))