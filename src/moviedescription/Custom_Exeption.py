import sys

class MovieDescriptionException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message, error_detail)

    def error_message_detail(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno

        error_message_detail = f"Error occurred in file: {file_name} on line number: {line_no}. Error message: {error_message}"
        return error_message_detail

    def __str__(self):
        return self.error_message


try:
    # Some operation that might raise an exception
    pass
except Exception as e:
    raise MovieDescriptionException("An error occurred during the movie description generation process.", sys) from e
