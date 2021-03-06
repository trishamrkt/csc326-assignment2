"""
    This function finds the maximum product 
    of 5 consecutive integers in the input 
    list 'l' using FUNCTIONAL PROGRAMMING
    (ie no if/else statements, or while loops)
"""
def find_product(L):
    num_iterations = len(L) - 5
    
    # Creates lists of 5
    lists = map(lambda (i, x): L[i: i+5], enumerate(L))[:num_iterations+1]
    
    # Finds the product of each list in lists
    products = map(lambda  arr: reduce(lambda x,y: x*y, arr), lists)
    
    # Sorts products in descending order and returns max 
    sorted_products = sorted(products, reverse=True)
    
    # Get greatest value and its index
    mx = sorted_products[0]
    index = products.index(mx)
    
    return (index, mx);


if __name__ == "__main__":
    # Expected output: (4, 15120)
    print find_product([1,2,3,4,5,6,7,8,9])