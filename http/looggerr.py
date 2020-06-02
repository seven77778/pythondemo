import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    filename="hhh.txt",
    filemode='a'
)
logging.info("xxxx")