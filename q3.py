def my_map(func, iterable):
    result_map = [];
    
    # Iterate through all the elements in iterable
    # Apply func to each element 
    for elem in iterable: 
        new_elem = func(elem)
        result_map.append(new_elem)
        
    return result_map 

def my_reduce(func, iterable):
    if len(iterable) == 1:
        return iterable[0]
    
    else: 
        prev = iterable[0]
        for elem in iterable:
            if iterable.index(elem) != 0:
                new_val = func(prev, elem)
                prev = new_val
        
    return new_val;

def my_filter(func, iterable):
    return [elem for elem in iterable if func(elem)]

if __name__ == "__main__":
    print my_map(lambda x: x**2, range(10))
    print my_reduce(lambda x,y: x*y, [1,2,3,4])
    print my_filter(lambda x: x > 10, [2,1,64,7,2,3,43,13])