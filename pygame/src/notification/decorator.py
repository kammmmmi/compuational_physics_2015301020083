import warnings


def deprecated(fo):
    def f(*args, **kwargs):
        warnings.warn("The method is deprecated!")
        return fo(*args, **kwargs)
    return f
