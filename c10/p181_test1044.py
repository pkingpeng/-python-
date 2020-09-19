import logging

# disable 的默认参数是 level=CRITICAL，所以需要禁用所有日志使可以不写参数
logging.disable()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

"""
"""
