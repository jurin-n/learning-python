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
