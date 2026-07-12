import sys


def error_message_detail(error, error_detail: sys):
    # Get traceback information about the current exception
    _, _, exc_tb = error_detail.exc_info()

    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a detailed error message
    error_message = (
        "Error occurred in Python script name [{0}] "
        "line number [{1}] "
        "error message [{2}]"
    ).format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        # Call the parent Exception class constructor
        super().__init__(error_message)

        # Create our detailed error message
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

