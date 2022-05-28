from loguru import logger


logger.add(
    './logfiles/file.log',
    format="{time} {level} {function} {message}",
    level="INFO",
    rotation="512 KB",
    compression="zip"
)
