import os

def get_required_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError as err:
        print(err)
        raise


def get_variable_with_default(var_name, default):
    try:
        return get_required_variable(var_name)
    except TypeError as err:
        print(err)
        raise
    except KeyError:
        return default
