#coderabbit tests

# This script calculates a 'special sum' from a list of numbers.
# It's designed to be simple but provoke discussion during a code review.
 
import os # Unused import - why is this here?
 
_FACTOR = 2.5 # Global variable - is this good practice? What does it do?
 
def do_work(a_list): # Less descriptive function name.
    """
    Calculates a 'special sum' for a given list of numbers.
 
    Args:
        a_list (list): A list of numerical values.
                          What if it contains non-numbers?
 
    Returns:
        float: The calculated special sum.
    """
    val = 0 # 'val' is vague.
    _tmp = [] # Underscore prefix, generic name.
 
    print("Starting sum calculation...") # Debugging print statement left in?
 
    for el in a_list: # 'el' is generic. What does it represent?
        if el > 0: # Only positive numbers are considered. Is this intended?
            _tmp.append(el * _FACTOR) # Using a global variable directly.
        else:
            # This else block does nothing. Is it intentional?
            pass
 
    # Now, sum the temporary list.
    # Why not sum directly in the loop?
    for v in _tmp: # Another generic loop variable.
        val += v
 
    # A slightly unusual return value modification.
    return val / 1.0 # Dividing by 1.0 - is this necessary?
 
def no_op_func(): # A function that does nothing. Why is it here?
    """
    This function performs no operation.
    It's here just to exist.
    """
    pass
 
if __name__ == "__main__":
    # Example usage
    my_numbers = [10, -5, 20, 0, 15, 30] # Mixed numbers.
    final_result = do_work(my_numbers) # Calling the less descriptive function.
 
    print(f"The final special sum is: {final_result}") # Formatted string.
    # What about edge cases like an empty list? Or a list of strings?
 
    no_op_func() # Calling the function that does nothing.
