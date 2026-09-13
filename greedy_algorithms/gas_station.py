# Question:
# There are n gas stations along a circular route, where gas[i] is the amount of gas at station i,
# and cost[i] is the cost to travel from station i to station i+1.
# Find the starting gas station's index if you can travel around the circuit once.
# If no solution exists, return -1.

def can_complete_circuit(gas, cost):
    total_gas = total_cost = 0
    tank = start = 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start if total_gas >= total_cost else -1
