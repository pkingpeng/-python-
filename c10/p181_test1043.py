import logging

# disable 可以关闭 CRITICAL 级别以下的日志打印
# logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
"""
2020-04-06 20:49:39,556 - DEBUG - Some debugging details.
2020-04-06 20:49:39,556 - INFO - The logging module is working.
2020-04-06 20:49:39,556 - WARNING - An error message is about to be logged.
2020-04-06 20:49:39,556 - ERROR - An error has occurred.
2020-04-06 20:49:39,556 - CRITICAL - The program is unable to recover!
"""
