# model.py

from pycalc.constants import *

# Simple "model" to handle calculator functionality
# This function just uses the Python "eval()" function
# to evaluate the expression entered.
def evaluateExpression(expression):
    """
    Evaluate the given mathematical expression and return the result.

    This function takes a mathematical expression as input, evaluates it using the `eval()` function,
    and returns the result as a string. If an error occurs during evaluation, it returns an error message.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        str: The result of the evaluation as a string, or an error message if evaluation fails.
    """
    try:
        result = str(eval(expression, {}, {}))
    except:
        result = ERROR_MSG
        
    return result