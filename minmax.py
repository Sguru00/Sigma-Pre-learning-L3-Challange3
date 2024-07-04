def max_min(arr):
    min = arr[0]
    max = arr[0]
    temp_arr =[]
    for i in arr:
     if i > max:
        max = i
     if i < min:
        min= i
    temp_arr.append(min)
    temp_arr.append(max)
    return(temp_arr)

print(max_min([2,4,1,0,2,-1]))
  


  

