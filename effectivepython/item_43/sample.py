import logging
from contextlib import contextmanager

def my_function():
    logging.debug('Some debug data')
    logging.error('Error log Here')
    logging.debug('More debug data')

my_function()

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    except:
        print('Inside Exception')
        pass
    finally:
        print('Inside Finally')
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    print('Inside')
    my_function()
    i = 1 / 0

print('After')
my_function()


print('[INFO]Start with target *******************************:')

@contextmanager
def log_level(level,name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level(logging.DEBUG,'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')

logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')