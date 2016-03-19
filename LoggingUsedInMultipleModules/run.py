import logging
import auxiliary

logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = auxiliary.Auxiliary()
logger.info('created an instance of auxiliary.Auxiliary')
logger.info('calling auxiliary.Auxiliary.do_somethine')
a.do_something()

logger.info('finished auxiliary.Auxiliary.do_somethine')
logger.info('calling auxiliary.some_function()')
auxiliary.some_function()
logger.info('done with auxiliary.some_function()')
