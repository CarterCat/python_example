import time


def logit(logger, start=False, error=False, timeit=False, prefix=""):
    def outer(func):
        def inner(*args, **kwargs):
            if start:
                logger.info(
                    f"{prefix}:{func.__name__}:start:args:{args}:kwargs:{kwargs}"
                )
            ts = time.time()
            result = None
            if error:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    logger.error(f"{prefix}:{func.__name__}:error:{e}", exc_info=True)
            else:
                result = func(*args, **kwargs)
            te = time.time()
            if timeit:
                logger.warning(f"{prefix}:{func.__name__}:timeit:{(te - ts) * 1000}")
            return result

        return inner

    return outer


# import logging
# logging.getLogger().setLevel(logging.INFO)
# logger = logging.getLogger("auction.%s" % __name__)

# @logit(logger, start=True, error=True, timeit=True, prefix="foo")
# def f(a,b,c):
#     time.sleep(2)
#     return a + b + c

# @logit(logger, start=True, error=True, timeit=True)
# def f(a,b,c):
#     time.sleep(2)
#     raise("xxx")
#     return a + b + c


####

# todo

# - learn logging
# - logger
# - handler

##

logging

import logging

logger = logging.getLogger(name)

handler = logging.FileHandler(filename.log)

handler = logging.StreamHandler()

formatter = logging.Formatter(format)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(level)

handler.setLevel(level)

logger.info("message")

# debugger

# import logging

# logging.basicConfig(level=logging.INFO)

# logging level: debug, info, warning, error
