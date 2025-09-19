from test2 import divide
import logging


# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler("app1.log"),
#         logging.StreamHandler()
#     ]
# )

# create a logger for module1
logger1=logging.getLogger("Arithmetic Module")
logger1.setLevel(logging.DEBUG)

# # create a logger for module 2

# logger2=logging.getLogger("module2")
# logger2.setLevel(logging.WARNING)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



def add(a,b):
    result=a+b
    logger1.debug(f"Adding {a} and {b}: {result}")
    return result

def subtract(a, b):
    result = a - b
    logger1.debug(f"Subtracting {b} from {a}: {result}")
    return result

def multiply(a, b):
    result = a * b
    logger1.debug(f"Multiplying {a} and {b}: {result}")
    return result

add(10,15)
subtract(15,10)
multiply(10,20)

# breakpoint()
# import pdb; pdb.set_trace()

divide(20,0)