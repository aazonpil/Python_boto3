import logging

# Step 2: Create a Logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)  # Capture all levels of logs

# Step 3: Set the Logging Level (Already done above)

# Step 4: Create Handlers
console_handler = logging.StreamHandler()  # Console handler
file_handler = logging.FileHandler('example.log')  # File handler

console_handler.setLevel(logging.WARNING)  # Console only shows warnings and above
file_handler.setLevel(logging.DEBUG)  # File gets all levels of logs

# Step 5: Create Formatters
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Setting formatters to handlers
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Step 6: Add Handlers to the Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Step 7: Start Logging
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
