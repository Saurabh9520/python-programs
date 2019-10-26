def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
              
            elif x == pivot:
                equal.append(x)
               
            elif x > pivot:
                greater.append(x)
                
        
        return sort(less)+equal+sort(greater) 
    else:  
        return array
    
   
new =[1,1,11,1,1]
print(sort(new))
