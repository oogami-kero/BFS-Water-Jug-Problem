import math
import unittest

def findWaterContainerPath(a, b, c):
    
    """ A function that takes the capacity of the containers and desired
        goal state to search for a solution to reach the desired state (amount)
        by utilizing the breadth first search on a graph of states
    """
    
    starting_state = (0, 0)                 # initialize starting state as (0,0), both empty
    path = list()                           # list storing the path of states to solution
    current_pair = (0, 0)                   # holder value for the current pair of values
    dict_states = { starting_state : ()     # initial graph dictionary for graph with starting state
             }
    states = []                             # queue of states to cycle through
    visited_states = []                     # comprehensive list of all states attempted/visited
    states.append(starting_state)

    graph = Graph(dict_states)              # initialize graph using Graph class

    loop = 1                                # debugging counter

    # while loop to cycle through and visit all states in the states queue
    while (states):
        
        """
        # debugging statements, comment out if not debugging
        print("this is loop")
        print(loop)
        loop += 1
        """
        
        current_pair = states[0]            # retrieves next state from queue
        states.pop(0)                       # remove from queue

        # if states is empty and target not reached, create/re-create intermediate states
        if not states:
            
            # calls function to fill the containers and record the states
            fillContainers(states, current_pair, a, b)

            # debug code
            """
            print("states")
            print(states)
            """
            # calls function to pour water between the containers and record the states
            pourFromContainer(a, b, current_pair, states)

            # debug code
            """
            print("states")
            print(states)
            """
            # calls function to empty the containers and record the states
            emptyContainers(states, a, b)

            # debug code
            """
            print("states")
            print(states)
            """
               
        
        # check if state already visited
        if(current_pair in visited_states):
            """print("continuing...1")"""         # debug statement
            continue
        
        # checks for valid state with given container sizes
        if (current_pair[0] > a or current_pair[1] > b):
            """print("continuing...2")"""         # debug statement
            continue
        
        if (current_pair[0] < 0 or current_pair[1] < 0):
            """print("continuing...3")"""         # debug statement
            continue

        
        # add state to the solution path
        path.append(current_pair)
        
        # mark state as visited
        visited_states.append(current_pair)
        
        # add the state to graph as vector
        if (current_pair in dict_states) and (visited_states[-1] != current_pair):
            Graph.add_edge(dict_states[visited_states[-1]], current_pair)
        else:
            Graph.add_vertex(graph, current_pair)

        # check if target amount is accomplished
        if (current_pair[0] == c or current_pair[1] == c):
            if (current_pair[0] == c):
                if (current_pair[1] != 0):
                    # append final state
                    path.append((current_pair[0], 0))

            else:
                if (current_pair[0] != 0):
                    # append final state
                    path.append((0, current_pair[1]))

            # debug code to see what's stored in graph
            """
            print("vertices of graph")
            print(Graph.vertices(graph))
            print("edges of graph")
            print(Graph.edges(graph))
            """

            # return the final path
            return path


# begin helper functions

def fillContainers(self, pair, a, b):
    """ Function to produce and return states of full containers """
    self.append((pair[0], b))
    self.append((a, pair[1]))
    
def pourFromContainer(a, b, pair, self):
    """ Function to produce and return states produced by pouring back and forth """
    for amt in range(max(a,b)):

            # pouring amt from container 2 to container 1
            d = pair[0] + amt
            e = pair[1] - amt

            # check if possible state or not
            if (d == a) or (e >= 0):
                self.append((d, e))

            # pouring amt from container 1 to container 2
            d = pair[0] - amt
            e = pair[1] + amt

            # check if possible state or not
            if (d >= 0) or (e == b):
                self.append((d, e))

def emptyContainers(self, a, b):
    """ Function to produce and return states of empty containers """
    self.append((a, 0))
    self.append((0, b))

# depricated
"""        
def add(self, key, value):
    # Function to add to dictionary
    self[key] = value 
"""

class Graph(object):
    """ Graph class that will be used to produce and modify graph """

    def __init__(self, graph_dict=None):
        """ Initializes a graph object """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ Returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ Returns the edges of a graph """
        return self.__generate_edges()
        
    def add_vertex(self, vertex):
        """ Adds vertex to graph object """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ Adds edge between two vertices """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the graph """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges


class TestWaterContainerGraphSearch(unittest.TestCase):
    """ Unittest class to run tests on code to ensure functionality """

    def testFoundGoalAmount(self):
        """ Checks if the goal was actually found """
        capacity_a = 5
        capacity_b = 6
        goal_amount = 4
        path = findWaterContainerPath(int(capacity_a), int(capacity_b), int(goal_amount))
        expected = (0, 4)
        expected_alt = (4, 0)
        if (self.assertEqual(path[-1], expected)) == False:
            self.assertEqual(path[-1], expected_alt)

    def testFillContainers(self):
        """ Checks if fill containers function works """
        states = []
        fillContainers(states, (0, 0), 5, 6)
        expected = [(0, 6), (5, 0)]
        self.assertEqual(states, expected)

    def testEmptyContainers(self):
        """ Checks if empty containers function works """
        states = []
        emptyContainers(states, 5, 6)
        expected = [(5, 0), (0, 6)]
        self.assertEqual(states, expected)

    def testAddVertex(self):
        """ Checks if add vertex function works """
        graph = Graph()
        Graph.add_vertex(graph, (1, 0))
        vertices = []
        vertices = Graph.vertices(graph)
        (1, 0) in vertices
        expected = True

    def testPourFromContainer(self):
        """ Checks if pouring function works """
        states = []
        pourFromContainer(3, 4, (3, 4), states)
        expected = [(3, 4), (3, 4), (4, 3), (2, 5), (5, 2), (1, 6), (6, 1), (0, 7)]
        self.assertEqual(states, expected)

# main function
def main():
    capacity_a = input("Enter the capacity of container A: ")
    capacity_b = input("Enter the capacity of container B: ")
    goal_amount = input("Enter the goal quantity: ")

    # ADD SOME TYPE/VALUE CHECKING FOR THE INPUTS (OR INSIDE YOUR FUNCTION)

    if int(goal_amount) % math.gcd(int(capacity_a), int(capacity_b)) == 0:
        path = findWaterContainerPath(int(capacity_a), int(capacity_b), int(goal_amount))
    else:
        print("No solution for containers with these sizes and with this final goal amount")

    print("\nThe solution path for the given capacities and goal amount is...")
    print(path)


# unittest_main() - run all of TestWaterContainerGraphSearch's methods (i.e. test cases)
def unittest_main():
    unittest.main()

# evaluates to true if run as standalone program
if __name__ == '__main__':
    main()
    unittest_main()
