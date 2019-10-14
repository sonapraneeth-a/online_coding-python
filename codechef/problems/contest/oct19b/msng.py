# File description
#
#        Filename: msng.py
#      Created on: 11 October 2019
#   Last modified: 11 October 2019
#          Author: sonapraneeth-a
#         Details: Problem Implementation for MSNG
#            Link: https://www.codechef.com/OCT19B/problems/MSNG
#     Description: 

# Changelog
#
# Date (DD-MM-YYYY)            Author               Update
# 11-10-2019               sonapraneeth-a      - Creation of the file
#
 
from typing import List
import logging


class MSNG:

    def __init__(self,
                 non_zero_b,
                 minus_one_b: List[str],
                 print_debug=False):
        self.non_zero_b = non_zero_b
        self.minus_one_b = minus_one_b
        self.min_allowed_base = dict()
        self.max_x = 1000000000000
        self.print_debug = print_debug
        self.logger = logging.getLogger('CodeChef.Main.Contest.OCT19B.MSNG.main')

    def find_x(self) -> int:
        x = None
        for number_pair in self.non_zero_b:
            b = number_pair[0]
            y = number_pair[1]
            current_x = self.number_in_base_10(b, y)
            if self.print_debug:
                self.logger.debug(f'B: {b}, Y: {y}, X: {current_x}')
            if current_x > self.max_x:
                return -1
            if x is None:
                x = current_x
            if x is not None and x != current_x:
                return -1
        if self.print_debug:
            self.logger.debug(f'X: {x}')
        return x

    def method_01(self) -> int:
        self.find_min_bases()
        x = self.find_x()
        for y in self.minus_one_b:
            does_b_exist, b = self.is_any_valid_b_exist_for_x_and_y(x, y)
            if not does_b_exist:
                return -1
        return x

    def get_all_valid_x(self, y: str) -> List[int]:
        min_base = self.min_allowed_base[y]
        allowed_x = []
        for base in range(min_base, 36+1):
            x = self.number_in_base_10(base, y)
            if x <= self.max_x:
                allowed_x.append(x)
        return allowed_x

    def find_min_bases(self):
        for y in self.minus_one_b:
            self.min_allowed_base[y] = self.get_min_base(y)
            if self.print_debug:
                self.logger.debug(f'Min base for {y} is {self.min_allowed_base[y]}')
        for b, y in self.non_zero_b:
            self.min_allowed_base[y] = self.get_min_base(y)
            if self.print_debug:
                self.logger.debug(f'Min base for {y} is {self.min_allowed_base[y]}')

    def method_02(self) -> int:
        if self.print_debug is True:
            self.logger.info(f'Method 02')
        self.find_min_bases()
        x = self.find_x()
        if self.print_debug is True:
            self.logger.info(f'X: {x}')
        if x is not None:
            for y in self.minus_one_b:
                does_b_exist, b = self.is_any_valid_b_exist_for_x_and_y(x, y)
                if not does_b_exist:
                    return -1
        else:
            if len(self.minus_one_b) == 0:
                return -1
            y = self.minus_one_b[0]
            if self.print_debug is True:
                self.logger.info(self.minus_one_b)
                self.logger.info(f'Finding possible X for given y: {y}')
            self.minus_one_b.pop()
            all_valid_x = self.get_all_valid_x(y)
            if self.print_debug is True:
                self.logger.info(all_valid_x)
                self.logger.info(self.minus_one_b)
            for y in self.minus_one_b:
                remove_invalid_x = []
                if len(all_valid_x) == 0:
                    return -1
                for x in all_valid_x:
                    does_b_exist, b = self.is_any_valid_b_exist_for_x_and_y(x, y)
                    if not does_b_exist:
                        remove_invalid_x.append(x)
                for x in remove_invalid_x:
                    all_valid_x.remove(x)
                remove_invalid_x.clear()
            if self.print_debug is True:
                self.logger.info('Remaining all valid x')
                self.logger.info(all_valid_x)
            x = all_valid_x[0]
        return x

    def get_min_base(self, Y: str) -> int:
        base = 2
        for c in Y:
            base = max(base, self.base_to_int_conversion(c) + 1)
        return base

    def base_to_int_conversion(self, c) -> int:
        # Reference: https://www.geeksforgeeks.org/convert-base-decimal-vice-versa/
        if '0' <= c <= '9':
            # if self.print_debug:
            #     self.logger.debug(f"c: {c}, val: {ord(c) - ord('0')}")
            return ord(c) - ord('0')
        else:
            # if self.print_debug:
            #     self.logger.debug(f"c: {c}, val: {ord(c) - ord('A') + 10}")
            return ord(c) - ord('A') + 10

    def number_in_base_10(self, base: int, number: str) -> int:
        answer = 0
        factor = 1
        for digit in number[::-1]:
            answer += factor * (self.base_to_int_conversion(digit))
            factor *= base
        return answer

    def is_any_valid_b_exist_for_x_and_y(self, x: int, y: str) -> (bool, int):
        answer = False
        base = None
        min_base = self.min_allowed_base[y]
        max_base = 36
        while min_base <= max_base:
            base = min_base + (max_base - min_base) // 2
            current_x = self.number_in_base_10(base, y)
            if x == current_x:
                return True, base
            if current_x < x:
                min_base = base + 1
            else:
                max_base = base - 1
        return answer, base
