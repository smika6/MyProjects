
#this function inputs/decorates another function and roughly estimates the time it takes to complete. (timit would be more accurate.)
def time_function(original_function):

    import time
    
    def time_func(*args, **kwargs):

        t1 = time.time()
        
        results = original_function(*args, **kwargs)

        t2 = time.time()

        print(f'\nStart time:\t{t1}' + 
                f'\nEnd Time:\t{t2}' + 
                f'\nTime to Execute {original_function.__name__}:\t{t2-t1}\n')

        return results

    return time_func