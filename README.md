# BFS-Water-Jug-Problem
CS 2050 Assignment 5 - Fall 2020

Programming Assignment #5: Graph Solution to the Water Jug Problem

What is the assignment?
  To implement a function that uses a graph-search approach to produce a "path" that represents a solution to the water container problem.
      https://en.wikipedia.org/wiki/Water_pouring_puzzle (Links to an external site.)
      
What needs to be done?
  Ultimately, all that needs to be done is to have a function, named findWaterContainerPath, return a list of states that represents a solution to the water container problem. 
  Note that each state can be thought of a vertex on a graph, and the transitions between the states can be thought of as the edges. 
  
  To successfully implement the function you will need to figure out what all of the possible state transitions (i.e. edges). You'll then perform a BFS across all of these     
  states; adding a state to your final solution path when it is used (and being sure to not add, or to remove, states that are not on the solution path).
