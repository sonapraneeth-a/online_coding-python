# File description
#
#        Filename: Problem.main.py
#      Created on: 11 October 2019
#   Last modified: 11 October 2019
#          Author: sonapraneeth-a
#         Details: Implementation for Problem
#            Link: https://www.codechef.com/ContestName/problems/Problem
#     Description: 

# Changelog
#
# Date (DD-MM-YYYY)            Author               Update
# 11-10-2019               sonapraneeth-a      - Creation of the file
#

import os
import sys
import logging

from codechef.templates.contest.problem import Problem


def msng__method_01(online_judge=False, print_debug=False):
    logger = None
    if print_debug:
        # Reference: https://realpython.com/python-logging/
        log_file = os.getcwd() + '/Contest/ContestNAme/Problem/' + 'log.txt'
        logging.basicConfig(filename=log_file, filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG)
        # Create a custom logger
        logger = logging.getLogger(__name__)
        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.DEBUG)
        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
        # logging.basicConfig(filename=log_file, filemode='w',
        #                     format='%(asctime)s - %(message)s',
        #                     level=logging.INFO)
        logger.debug('This is a debug message')
        logger.info('This is an info message')
    if online_judge is True:
        input_file = os.getcwd() + '/Contest/ContestName/Problem/' + 'in.txt'
        output_file = os.getcwd() + '/Contest/ContestName/Problem/' + 'out.txt'
        temp_stdin = sys.stdin
        temp_stdout = sys.stdout
        sys.stdin = open(input_file, 'r')
        sys.stdout = open(output_file, 'w')
    t = int(input())
    for test in range(1, t + 1):
        n = int(input())
        try:
            problem = Problem(print_debug=print_debug,
                              logger=logger)
            print(problem.method_01())
        except Exception as error:
            print(str(error))
            exit(255)
    if online_judge is True:
        sys.stdin = temp_stdin
        sys.stdout = temp_stdout
