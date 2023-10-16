def gas_station_journey(gas, cost):
    if sum(gas) - sum(cost) < 0:
        return -1
        
    n = len(gas)
    re = -1
    for idx in range(len(gas)):
        i = idx
        station = 0
        curr_gas = 0
        while True:
            curr_gas = curr_gas + gas[i] - cost[i]
            if curr_gas < 0:
                break
            if station == n:
                re = i
                break
            
            station += 1
            i = (i + 1) % len(gas)
    return re

#####
def gas_station_journey(gas, cost):
   
    if sum(cost) > sum(gas):  
        return -1             

    current_gas, starting_index = 0, 0

    for i in range(len(gas)):  
       
        current_gas = current_gas + (gas[i] - cost[i])
        
        if current_gas < 0:
            current_gas = 0
            starting_index = i + 1

    return starting_index