# header6ff05843-c222-461f-8226-36a7abe6806e

from lib import decorator, exception


class DecoratePublicMethods(type):
    # todo: this should be refactored to DecorateMethods and used with a factory
    """
    Decorates all test methods with a decorator that makes a screenshot on
    any exception.
    """
    def __new__(mcs, name, bases, dct):
        for attr_name, value in dct.items():
            if all([name in attr_name for name in ["test_", "_test"]]) \
                    and hasattr(value, "__call__"):
                dct[attr_name] = decorator.take_screenshot_on_error(value)

        return super(DecoratePublicMethods, mcs).__new__(mcs, name, bases, dct)


class RequireDocs(type):
    """
    Requires from all methods to include docstrings.
    """
    def __new__(mcs, name, bases, dct):
        for attr_name, value in dct.items():
            if hasattr(value, "__call__") and not hasattr(value, "__doc__"):
                raise exception.DocstringsMissing(attr_name)

        return super(RequireDocs, mcs).__new__(mcs, name, bases, dct)
