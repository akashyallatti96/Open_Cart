import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure the 'logs' directory exists
        log_dir = os.path.join(os.path.abspath(os.path.curdir), "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Create the directory if it doesn't exist

        # Set the log file path
        log_file = os.path.join(log_dir, "automation.log")
        print(log_dir)

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # Configure logging
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,  # Set the level to DEBUG (can be adjusted)
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'  # Updated date format
        )

        # Return logger instance
        logger = logging.getLogger()
        logger.setLevel(50)
        return logger


# Test the logging setup
logger = LogGen.loggen()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.log(logging.NOTSET, "This is a NOTSET level message (but doesn't usually get logged).")
logger.critical("This is a critical message")
