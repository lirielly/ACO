# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 01-07-2018 06:00:00 PM
"""

import math
import numpy as np

# Class ant represents one ant and its path
class Ant(object):
    def __init__(self, start_node, size):
        self.path = [start_node]
        self.of_value = math.inf
        self.distance = 0.0
        self.possible_nodes = [x for x in range(size) if x != start_node]
        
    
    def calculate_probabilities(self, distances, pheromone, alpha, beta):
        '''
        Function to calculate all probability values
        '''
        probabilities = []
        current_node = self.path[-1]
        for i in self.possible_nodes:
            probabilities.append((pheromone[current_node, i]**alpha)*((1/distances[current_node, i])**beta))
        return probabilities/sum(probabilities)
        
    
    def chose_next_node(self, distances, pheromone, alpha, beta):
        '''
        Function to chose the next visited node
        '''
        probabilities = self.calculate_probabilities(distances, pheromone, alpha, beta)
        rw = np.random.rand()
        sum_ = 0.0
        for i in range(len(probabilities)):
            sum_ += probabilities[i]
            if sum_ >= rw:
                self.path.append(self.possible_nodes.pop(i))
                break
            
    def build_path(self, distances, pheromone, alpha, beta):
        '''
        Function to build a path for an ant
        '''
        for i in range(distances.shape[0] - 1):
            self.chose_next_node(distances, pheromone, alpha, beta)
                