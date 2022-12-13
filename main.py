import combinations
import math

def ctg(text: str) -> float: # Trigonometrial function, cotangens
    return 1 / math.tan(text)

def factorial_math(text: str) -> int: # Replacing factorial expression with factorial result
    return combinations.factorial(int(text[:text.index('!')])) # Finding factorial expression and returning factorial

def placement_math(text: str) -> int: # Replacing placement expression with placement result
    text = text.strip('P()').replace(',', ' ').split(' ') # Splitting expression for 2 numbers, start and end of placement
    number1 = int(text[0]) # First number
    number2 = int(text[1]) # Second number
    return combinations.placement(number1, number2) # Returning placement result

def combination_math(text: str) -> int: # Replacing combination expression with combination result
    text = text.strip('C()').replace(',', ' ').split(' ') # Splitting expression for 2 numbers, start and end of combination
    number1 = int(text[0]) # First number
    number2 = int(text[1]) # Second number
    return combinations.combinations(number1, number2) # Returning combination result

def sqrt_math(text: str) -> float: # Replasing root expression with root result
    text = text.strip('sqrt()') # Getting number
    return math.sqrt(float(text)) # Returning result

def trigonometry(text: str) -> int: # Replacing trigonometry expression with trigonometry function result
    if 'sin' in text: # Sin function
        text = text.strip('sin()')
        return f'{math.sin(math.radians(int(text))):.3f}' # Returning result
    if 'cos' in text: # Cos function
        text = text.strip('cos()')
        return f'{math.cos(math.radians(int(text))):.3f}' # Returning result
    if text.startswith('tg'): # Tg function
        text = text.strip('tg()')
        return f'{math.tan(math.radians(int(text))):.3f}' # Returning result
    if 'ctg' in text: # Ctg function
        text = text.strip('ctg()')
        return f'{ctg(math.radians(int(text))):.3f}' # Returning result

def quadratic_equation(text: str) -> list: # Replacing quiadratic equation with its result
    text = text.strip('CB()').split(',') # Getting coefficients
    text = [int(i) for i in text] # From str to int
    disk = (text[1] ** 2) - (4 * text[0] * text[2]) # Disctiminant
    if disk >= 0: # If discriminant >= 0 then equation has answer
        x1 = eval(f'(-{text[1]}+{math.sqrt(disk)})/(2*{text[0]})')
        x2 = eval(f'(-{text[1]}-{math.sqrt(disk)})/(2*{text[0]})')
        return [x1, x2]
    else: return '' # If discriminant < 0 then its has no answer, so returning ''

def global_check(text: str) -> str: # Checking expression
    for index, i in enumerate(text):
        try:
            if '!' in i: # Factorial
                text[index] = factorial_math(i)
            if i.upper().startswith('P') and i not in 'previous': # Placement
                text[index] = placement_math(i)
            if i.upper().startswith('C') and 'CB' not in i: # Combination
                text[index] = combination_math(i)
            if i.startswith('sqrt'): # Root
                text[index] = sqrt_math(i)
            if 'sin' in i or 'cos' in i or 'tg' in i or 'ctg' in i: # Trigonomerial
                text[index] = trigonometry(i)
            if i.startswith('CB'): # Cubic Equation
                text[index] = quadratic_equation(i)
            if 'previous'.startswith(str(text[0])):  # Getting previous result
                with open('prev.txt', 'r') as result: # Opening file with previouse result
                    text[index] = result.read()
        except ValueError: # If something went wrong returning -1
            print('Wrong expression!' + '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
            return '-1'
    return ''.join([str(i) for i in text])

def main(): # Main function. To use script run it
    print('Standart look\nFactorial: (your number)!\nPlacement: P(from,to)\nCombinations: C(from,to)\nRoot: sqrt(your number)\nTo solve quadratic equation: CB(a,b,c)'
          '\nSin, Cos, Tg, Ctg: sin/cos/tg/ctg + (degrees)\nPrevious result: previous\nType "quit" to quit\n'
          '\n1: Example: C(2,5) + 5! + P(2,10)\nResult = 220.0\n'
          '\n2: Example: prev(was 220) + 5!\nResult = 340.0\n') # Explaining
    task = input('______________________\n' + 'Write your expression: ').split(' ') # Taking expression from user
    while task[0].lower() != 'quit': # If expression not equal to "quit"
        task = global_check(task) # Calling global_check function
        try:
            if task != '-1': # If all went right
                res = eval(''.join([str(i) for i in task])) # Calling eval() function
                with open('prev.txt', 'w') as result: # Writing result to file
                    result.write(str(res))
                    result.close()
                print('Result = ' + str(res) + '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
                task = input('\n' + '______________________\n' + 'Write your task: ').split(' ') # Taking next one expression from user
            else: # If something went wrong
                task = input('\n' + '______________________\n' + 'Write your task: ').split(' ') # Taking next one expression from user
        except NameError or SyntaxError or ValueError: # If something went wrong
            print('Wrong expression!' + '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
            task = input('\n' + '______________________\n' + 'Write your task: ').split(' ') # Taking next one expression from user
    else: # If user's expression not equal to "quit"
        print('Result = ' + 'exit' + '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾') # Taking next one expression from user

if __name__ == '__main__':
    main() # Start point