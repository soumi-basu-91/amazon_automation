import pytest_check as check


class Assertutility:
    def check_equals(self, actual, expected, message=None):
        if message is None:
            message = "Actual and expected results do not match"
        check.equal(actual, expected, message)

    def check_true(self, flag_val, message=None):
        if message is None:
            message = "Actual and expected results do not match"
        check.is_true(flag_val, message)

    def check_false(self, flag_val, message=None):
        if message is None:
            message = "Actual and expected results do not match"
        check.is_false(flag_val, message)

    def check_greater(self, actual, expected, message=None):
        if message is None:
            message = "Actual and expected results do not match"
        check.greater(actual, expected, message)

    def check_lesser(self, actual, expected, message=None):
        if message is None:
            message = "Actual and expected results do not match"
        check.less(expected, actual, message)