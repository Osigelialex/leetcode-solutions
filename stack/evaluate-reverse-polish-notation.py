from math import trunc
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        ops = {'+', '-', '*', '/'}

        for i in tokens:
            if i not in ops:
                operands.append(i)
            else:
                op1 = int(operands.pop())
                op2 = int(operands.pop())

                if i == "-":
                    operands.append(op2 - op1)
                elif i == "+":
                    operands.append(op1 + op2)
                elif i == "*":
                    operands.append(op1 * op2)
                else:
                    operands.append(trunc(op2 / op1))

        return int(operands.pop())