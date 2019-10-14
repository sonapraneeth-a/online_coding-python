# File description
#
#        Filename: msng.main.py
#      Created on: 11 October 2019
#   Last modified: 11 October 2019
#          Author: sonapraneeth-a
#         Details: Main Implementation for MSNG
#            Link: https://www.codechef.com/OCT19B/problems/MSNG
#     Description: 

# Changelog
#
# Date (DD-MM-YYYY)            Author               Update
# 11-10-2019               sonapraneeth-a      - Creation of the file
#

import os
import sys
import logging

from codechef.problems.contest.oct19b import MSNG


def msng__method_01(online_judge=False, print_debug=False):
    logger = None
    if print_debug:
        # Reference: https://realpython.com/python-logging/
        log_file = os.getcwd() + '/Contest/OCT19B/MSNG/' + 'log.txt'
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
    if online_judge is True:
        input_file = os.getcwd() + '/Contest/OCT19B/MSNG/' + 'in.txt'
        output_file = os.getcwd() + '/Contest/OCT19B/MSNG/' + 'out.txt'
        temp_stdin = sys.stdin
        temp_stdout = sys.stdout
        sys.stdin = open(input_file, 'r')
        sys.stdout = open(output_file, 'w')
    t = int(input())
    for test in range(1, t + 1):
        if print_debug:
            logger.info(f'Test: {test}')
        n = int(input())
        non_zero_b = []
        minus_one_b = []
        for number in range(1, n+1):
            b, y = [x for x in input().rstrip().split()]
            if b == '-1':
                minus_one_b.append(y)
            else:
                non_zero_b.append((int(b), y))
        try:
            msng = MSNG(non_zero_b=non_zero_b,
                        minus_one_b=minus_one_b,
                        print_debug=print_debug)
            print(f'{msng.method_01()}')
        except Exception as error:
            print(error)
            if print_debug:
                logger.exception(str(error))
            exit(255)
        non_zero_b.clear()
        minus_one_b.clear()
    if online_judge is True:
        sys.stdin = temp_stdin
        sys.stdout = temp_stdout


def msng__method_02(online_judge=False, print_debug=False):
    logger = None
    if print_debug:
        # Reference: https://realpython.com/python-logging/
        log_file = os.getcwd() + '/Contest/OCT19B/MSNG/' + 'log.txt'
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
    if online_judge is True:
        input_file = os.getcwd() + '/Contest/OCT19B/MSNG/' + 'in.txt'
        output_file = os.getcwd() + '/Contest/OCT19B/MSNG/' + 'out.txt'
        temp_stdin = sys.stdin
        temp_stdout = sys.stdout
        sys.stdin = open(input_file, 'r')
        sys.stdout = open(output_file, 'w')
    t = int(input())
    for test in range(1, t + 1):
        if print_debug:
            logger.info(f'Test: {test}')
        n = int(input())
        non_zero_b = []
        minus_one_b = []
        for number in range(1, n+1):
            b, y = [x for x in input().rstrip().split()]
            if b == '-1':
                minus_one_b.append(y)
            else:
                non_zero_b.append((int(b), y))
        try:
            msng = MSNG(non_zero_b=non_zero_b,
                        minus_one_b=minus_one_b,
                        print_debug=print_debug)
            print(f'{msng.method_02()}')
        except Exception as error:
            print(error)
            if print_debug:
                logger.exception(str(error))
            exit(255)
        non_zero_b.clear()
        minus_one_b.clear()
    if online_judge is True:
        sys.stdin = temp_stdin
        sys.stdout = temp_stdout
