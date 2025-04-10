from typing import List

class Solution:
    # Determines the starting gas station index that allows traveling around the circuit once.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # Total gas available
        total_gas = 0    
        # Total cost required
        total_cost = 0    
        # Current tank balance
        current_tank = 0  
        # Potential starting station
        start_station = 0 
        
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            current_tank += gas[i] - cost[i]
            
            # If current_tank is negative, we can't start at the current start_station
            if current_tank < 0:
                # Move start to next station
                start_station = i + 1  
                # Reset tank
                current_tank = 0       
        
        # If total gas is enough to cover total cost, return the start station
        return start_station if total_gas >= total_cost else -1

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50, "="))
gas1 = [1, 2, 3, 4, 5]
cost1 = [2, 3, 4, 5, 1]
print("Example 1:")
print("Input gas1:", gas1)
sol1 = sol.canCompleteCircuit(gas1, cost1)
print("Output:", sol1)
print("=".center(50, "="))

# Example 2
gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print("Example 2:")
print("Input gas2:", gas2)
sol2 = sol.canCompleteCircuit(gas2, cost2)
print("Output:", sol2)
print("=".center(50, "="))