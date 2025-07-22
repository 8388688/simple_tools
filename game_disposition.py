from simple_tools.misc import deprecated

__all__ = ["Users", ]


class Users:
    def __init__(self):
        import warnings
        warnings.warn(f"{deprecated(Users.__name__)}",
                      DeprecationWarning, stacklevel=4)
