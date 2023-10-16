def two_city_scheduling(costs):
  n = len(costs)
  cost_difference = [[x - y, [x, y]] for x, y in costs]
  cost_difference.sort()
  print(cost_difference)
  i = 0
  result = 0
  while i < (n // 2):
    _, cost = cost_difference[i]
    result += cost[0]
    i += 1
  
  print(result)

  while i < n:
    _, cost = cost_difference[i]
    result += cost[1]
    i += 1

  return result


#########
def two_city_scheduling(costs):
    num_costs = len(costs)
    cost_difference_list = [[x - y, [x, y]] for x, y in costs]
    cost_difference_list.sort()

    i = 0
    result = 0

    # Add costs of the first half
    while i < num_costs:
        cost1, cost2 = cost_difference_list[i][1]
        if i < num_costs // 2:
            result += cost1
        else:
            result += cost2
        i += 1

    return result