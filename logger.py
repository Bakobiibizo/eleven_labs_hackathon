import logging

# Create a custom logger
debug_logger = logging.getLogger("debug_logger")
debug_logger.setLevel(logging.DEBUG)

# Create a file handler and set the log file name
file_handler = logging.FileHandler("debug.log")

# Define the log message format
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
debug_logger.addHandler(file_handler)

# Example usage
def some_function():
    debug_logger.debug("This is a debug message")
    debug_logger.info("This is an info message")
    debug_logger.warning("This is a warning message")
    debug_logger.error("This is an error message")
    debug_logger.critical("This is a critical message")

some_function()

