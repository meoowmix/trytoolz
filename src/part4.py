# Part IV - Dictionaries & Advanced Iteration

def create_dict(keys, values):
    """
    Create a dictionary from parallel lists of keys and values.

    Parameters:
        keys (list): List of keys
        values (list): List of values

    Returns:
        dict: Dictionary mapping keys to values
    """
    dict = {}

    for i in range(len(keys)):
        newkey = keys[i]
        newvalue = values[i]
        dict[newkey] = newvalue

    return dict

def get_value(dct, key):
    """
    Retrieve a value from a dictionary by key.

    Parameters:
        dct (dict): The dictionary to search
        key (any): The key to look up

    Returns:
        any: The value associated with the key if found, otherwise None
    """
    return (dct.get(key))

def set_value(dct, key, value):
    """
    Add or update a key-value pair in a dictionary.

    Parameters:
        dct (dict): The dictionary to modify
        key (any): The key to set
        value (any): The value to associate with the key

    Returns:
        dict: The modified dictionary
    """
    dct[key] = value

    return dct


def has_key(dct, key):
    """
    Check if a key exists in a dictionary.

    Parameters:
        dct (dict): The dictionary to search
        key (any): The key to check

    Returns:
        bool: True if key exists, False otherwise
    """
    if key in dct:
        return True
    else:
        return False

def get_keys(dct):
    """
    Get all keys from a dictionary.

    Parameters:
        dct (dict): The dictionary to query

    Returns:
        list: List of all keys
    """
    return list(dct)

def get_values(dct):
    """
    Get all values from a dictionary.

    Parameters:
        dct (dict): The dictionary to query

    Returns:
        list: List of all values
    """
    return list(dct.values())

def count_keys(dct):
    """
    Count the number of key-value pairs in a dictionary.

    Parameters:
        dct (dict): The dictionary to count

    Returns:
        int: Number of key-value pairs
    """
    return len(dct)


def remove_key(dct, key):
    """
    Remove a key-value pair from a dictionary.

    Parameters:
        dct (dict): The dictionary to modify
        key (any): The key to remove

    Returns:
        dict: The modified dictionary
    """
    if key in dct:
        dct.pop(key)
    
    return dct

def iterate_list(lst, callback):
    """
    Apply a callback function to each element of a list.

    Parameters:
        lst (list): The list to iterate over
        callback (function): Function to apply to each element

    Returns:
        list: List containing the results from applying callback to each element
    """
    list = [callback(thing) for thing in lst]

    return list

def find_item(lst, predicate):
    """
    Find the first item in a list that matches a condition.

    Parameters:
        lst (list): The list to search
        predicate (function): Function that returns True for matching items

    Returns:
        any: The first matching item if found, otherwise None
    """
    for thing in lst:
        if predicate(thing):    
            return thing
    return None