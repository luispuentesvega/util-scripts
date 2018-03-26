import logging
import datetime

logging.basicConfig(filename='log'+datetime.datetime.now().strftime ("%Y%m%d")+'.log',format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')