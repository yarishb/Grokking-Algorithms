# Creating graphs that 
# are representing cost of way to some points

# This graph shows price to get from start to a and b
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# This graph shows price to get from a to finish
graph["a"] = {}
graph["a"]["fin"] = 1

# This graph shows price to get from b to a and to finish
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}
#------------------------------------------------

# This graph shows costs to get into some point
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#---------------------------------------------------

# This graph shows parents of some points
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# This array is represinting the way
processed = []

# This function finds lowest cost node
def find_lowest_cost_node(costs):
     # starting points
     lowest_cost = float("inf")
     lowest_cost_node = None
     
     # for each node in costs
     for node in costs:
          # stores current cost of current node 
          cost = costs[node]
          # if cost is less then starting point and node is not processed yet
          if cost < lowest_cost and node not in processed:
               # starting cost becomes current node's cost
               lowest_cost = cost
               # starting node becomes current node with lowest cost
               lowest_cost_node = node
     # returns node with lowest cost
     return lowest_cost_node

# Find the lowest cost of node
node = find_lowest_cost_node(costs)

# While there are nodes
while node is not None:
     # storing the cost of getting to the current node
     cost = costs[node]
     # storing all the neighbors of this node
     neighbors = graph[node]
     # go threw each neighbor
     for neighbor in neighbors.keys():
          # storing cost of getting to this neighbor threw the node
          new_cost = cost + neighbors[neighbor]
          # if price is cheaper
          if costs[neighbor] > new_cost:
               # cost becomes the new cost
               costs[neighbor] = new_cost
               # parent becomes new parent
               parents[neighbor] = node
     # append new node to the list of nodes
     processed.append(node)
     node = find_lowest_cost_node(costs)


print("Cost from the starting node to each nodes")
print(costs)