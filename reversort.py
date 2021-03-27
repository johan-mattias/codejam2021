cases = int(input())
#print(cases)
for i in range(cases):
    _ = int(input())
    list_in = list(map(int,input().split(' ')))
    #print(list_in)
    
    cost = 0
    for out_index in range(len(list_in)):
        #print('out', out_index)
        min_index = out_index
        for index in range(out_index, len(list_in)):
            if list_in[index] < list_in[min_index]:
                min_index = index
        #print("min", list_in[min_index], min_index)
        list_in_temp = list_in[out_index:min_index+1]
        cost += len(list_in_temp)
        list_in = list_in[:out_index] + list_in_temp[::-1] + list_in[min_index+1:]
        #print('temp', list_in)
    #print('cost',cost-1)
    #print(list_in)
    print("Case #"+ str(i+1)+ ": "+ str(cost-1))