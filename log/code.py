import logging
import logging.handlers

LOG_FILE_NAME = 'code.log'
logger = logging.getLogger()

def setup_logger():
    logger.setLevel(logging.INFO)
    #时间 进程id 线程名字 路径 行 日志级别名称 信息
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE_NAME, maxBytes=10485760, backupCount=5, encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

setup_logger()
