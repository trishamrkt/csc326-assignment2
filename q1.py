from time import clock

def profile(func, *args):
    
    # Finds the time it takes to perform func
    def timer(*args):
        if PROFILE_FUNCTIONS: 
            # Name of original function - used as key in PROFILE_RESULTS dict
            func_name = func.__name__
            
            # Times the function 
            start = clock();
            func(*args);
            duration = clock() - start;
            
            # Updates PROFILE_RESULTS dict
            update_results(func_name, duration)
            
    return timer

def update_results(name, duration):
    avg_time = 0;
    num_calls = 0;
    
    # Create new entry for function 
    if name not in PROFILE_RESULTS:
        avg_time = duration
        num_calls = 1;
        PROFILE_RESULTS[name] = (avg_time, num_calls)
    
    # Update existing entries
    # Increments num_calls, recalculates avg runtime
    else: 
        num_calls = PROFILE_RESULTS[name][1] + 1;
        avg_time = duration/num_calls + (num_calls - 1)*PROFILE_RESULTS[name][0]/num_calls
        PROFILE_RESULTS[name] = (avg_time, num_calls)
    
    print PROFILE_RESULTS

@profile
def foo():
    for i in range(1000000):
        pass
    return; 

if __name__ == "__main__":
    PROFILE_FUNCTIONS = True;
    PROFILE_RESULTS = {}
    foo()
    foo()
    foo()