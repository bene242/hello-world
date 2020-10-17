import logging
logger = logging.getLogger()
hdlr = logging.FileHandler('/home/pi/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)
logger.info('While this is just chatty')
