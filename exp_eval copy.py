# Name: Michal Golovanevsky
# Section: 7
#Project 2

from Stacks import StackArray

#returns the postfix expression
#string => string
def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """
    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""

    #creates a dictionary
    prec = {}
    #sets each operator priority
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    #initializes a stack
    op_stack = StackArray(30)
    #creates an empty list for the output
    postfixList = []
    #creates a list of tokens out of the given string
    tokenList = infixexpr.split(" ")

    #loops through the tokens in the list
    for token in tokenList:
        #checks if the token is a letter or a number
        if token not in "+-*/^()":
            #adds it to the end of the output list
            postfixList.append(token)
        #checks if a token is the left parenthesis
        elif token == '(':
            #pushes left parenthesis to stack
            op_stack.push(token)
        # checks if a token is the right parenthesis
        elif token == ')':
            #pops and saves the top token in the stack
            top_token = op_stack.pop()
            #loops until reaches right parenthesis
            while top_token != '(':
                #adds the top token to the output list
                postfixList.append(top_token)
                #pops the top token and updates it
                top_token = op_stack.pop()
        #checks if the token is the ^ operator
        elif token == '^':
            #pushes it to the stack
            op_stack.push(token)
        else:
            #loops until the stack is empty or the top operator in the stack is greater/equal to the priority of the token
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                #pop from the stack and adds it to the output list
                postfixList.append(op_stack.pop())
            #pushes token to the stack
            op_stack.push(token)
    #loops until the stack is empty
    while not op_stack.is_empty():
        #pops adds the operators in the stack to the output list
        postfixList.append(op_stack.pop())
    #returns the final string output
    return " ".join(postfixList)

#string => float
#returns an evaluation of the expression
def postfix_eval(postfixExpr):
    """Evaluates a postfix expression"""
    """Input argument: a string containing a postfix expression where tokens
    are space separated. Tokens are either operators {+ - * / ^} or numbers"""

    # initializes a stack
    operand_stack = StackArray(30)
    # creates a list of tokens out of the given string
    tokenList = postfixExpr.split()

    #loops through tokens in the token list
    for token in tokenList:
        #checks if the token is a number
        if token not in "+-*/^":
            #pushes it to the stack
            operand_stack.push(float(token))
        else:
            #saves the last operand in the stack
            operand2 = operand_stack.pop()
            # saves the second to last operand in the stack
            operand1 = operand_stack.pop()
            #calcualtes the result using the doMath function
            result = doMath(token, operand1, operand2)
            #pushes the result into the stack
            operand_stack.push(result)
    #returns the final result from the stack
    return operand_stack.pop()

#returns an evaluation of a mathematical expression
#operator float float => float
def doMath(op, op1, op2):
    """ compute the infix statement"""
    #checks what operator is being used and returns the result
    if op == "^":
        return op1 ^ op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        if op2 == 0:
            #raises an error when divided by zero
            raise ValueError('Cannot divide by zero')
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

#string => boolean
#returns True if the expression is valid and False otherwise
def postfix_valid(postfixexpr):
    """ Purpose """
    #creates a counter for the number of operands
    num_of_operands = 0
    #creates a list of tokens out of the postfix expression
    tokenList = postfixexpr.split(" ")
    #loops through the tokens in the token list
    for token in tokenList:
        #checks if the token is a number
        if token not in "+-*/^":
            #increases the number of operands
           num_of_operands += 1
        else:
            #checks and returns false if there are less than two operands
            if (num_of_operands < 2):
                return False
            else:
                #subtracts 1 for 2 pops, operation and 1 push
                num_of_operands -=1
    #returns true if the number of operands is 1 and false otherwise
    return num_of_operands == 1
