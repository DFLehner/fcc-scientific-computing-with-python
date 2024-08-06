#This script formats addition and negation sums into column format.
#It takes input of the form of a string 'a + b' or 'a - b' where
# a and b is an integer between 1 and 9999.


import re

def arithmetic_arranger(problems, show_answers=False):
    result = ''
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    
    #User input validation:
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        if not re.match(r'^[\d\+\-\/\* ]+$', problem):
            return 'Error: Numbers must only contain digits.'
        num1 = problem.split(' ')[0]
        op = problem.split(' ')[1]
        num2 = problem.split(' ')[2]
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if op == '*' or op == '/':
            return "Error: Operator must be '+' or '-'."
        
        #format answer string:
        num_of_chars = max(len(num1), len(num2)) + 2
        padded1 = num1.rjust(num_of_chars, ' ')
        padded2 = op + num2.rjust(num_of_chars-1, ' ')
        line1 += padded1
        line2 += padded2
        line3 += ''.rjust(num_of_chars, '-')
    
        #Solve problem if necessary:
        if show_answers == True:
            if op == '+':
                solution = str(int(num1) + int(num2))
            else:
                solution = str(int(num1) - int(num2))
            line4 += solution.rjust(num_of_chars, ' ')
    
    #Final output being formed:
        problem_delimiter = '    '
        line1 += problem_delimiter
        line2 += problem_delimiter
        line3 += problem_delimiter
        line4 += problem_delimiter
    
    line1 = line1[:-len(problem_delimiter)]
    line2 = line2[:-len(problem_delimiter)]
    line3 = line3[:-len(problem_delimiter)]
    line4 = line4[:-len(problem_delimiter)]

    result = line1 + '\n' + line2 + '\n' + line3
    if show_answers == True:
        result += '\n' + line4
    
    return result

print(arithmetic_arranger(["32 + 698", "380 - 2", "45 + 43", "123 + 49",]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85002", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
