# header6ff05843-c222-461f-8226-36a7abe6806e

from functools import wraps
from lib import environment, constants, file_ops


def take_screenshot_on_error(fun):
    # todo: replace with pytest-selenium which automagically takes
    # screenshots on failures
    @wraps(fun)
    def wrapper(self, *args, **kwargs):
        try:
            return fun(self, *args, **kwargs)
        except Exception as e:
            file_path = environment.PROJECT_ROOT_PATH \
                + constants.path.LOGS_DIR \
                + self.__class__.__name__ \
                + "." \
                + args[0].driver.title
            unique_file_path = file_ops.get_unique_postfix(file_path, ".png")
            args[0].driver.get_screenshot_as_file(unique_file_path)
            raise
    return wrapper
