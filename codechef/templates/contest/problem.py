# File description
#
#        Filename: Problem.py
#      Created on: 11 October 2019
#   Last modified: 11 October 2019
#          Author: sonapraneeth-a
#         Details: Implementation for Problem in ContestName
#            Link: https://www.codechef.com/ContestName/problems/Problem
#     Description: 

# Changelog
#
# Date (DD-MM-YYYY)            Author               Update
# 11-10-2019               sonapraneeth-a      - Creation of the file
#

class Problem:

    def __init__(self, print_debug=False, logger=None):
        if print_debug is True and logger is None:
            raise Exception('print_debug is True bug logger is None')
        self.print_debug = print_debug
        self.logger = logger

    def method_01(self):
        return self.print_debug
