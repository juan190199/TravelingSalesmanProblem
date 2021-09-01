# TravelingSalesmanProblem

## About
Python implementation of Christofides algorithm with Google Maps API. The purpose of this project is to visualize and understand with help of Google Maps API the Christofides algorithm.

## Table of Contents
- [About](#about)
- [Introduction](#introduction)
- [Algorithm Details](#algorithm-details)

## Introduction

In the Traveling Salesman Problem (TSP), there is a given set of cities {1, ..., n} and the input consists of a symmetric n by n matrix C that specifies the cost of travelling from city i to city j. By convention, the cost of traveling from any city to itself is equal to 0, and costs are nonnegative.

If we instead view the input as an undirected complete graph with cost associated with each edge, then a tour or cycle consists of a Hamiltonian cycle in this graph; that is, a cyclic permutation of the cities or, equivalently, a traversal of the cities in the order k(1), k(2), ..., k(n), where each city i is listed as a unique image k(i). The task is to find a Hamiltonian cycle in G of minimum weight.

It is NP-complete to decide whether a given undirected graph G = (V, E) has a Hamiltonian cycle. Since the Hamiltonian cycle problem can be reduced to the TSP, the latter is NP-hard. However, approximation algorithms for the TSP can be used to solve the Hamiltonian cycle problem 

Christofides algorithm is an 3/2-approximation algorithm for solving TSP in a metric space. It was first published by Nicos Christofides in 1976.

## Algorithm Details

The algorithm is described by following steps:
1. Minimum Spanning Tree
2. Odd Degree Vertices
3. Minimum Weight Perfect Matching
4. Connected Multigraph
5. Eulerian Circuit
6. Hamiltonian Circuit

More details about the algorithm can be found on following [link](https://en.wikipedia.org/wiki/Christofides_algorithm)

![alt text](https://github.com/juan190199/TravelingSalesmanProblem/blob/main/googlemaps.png)
