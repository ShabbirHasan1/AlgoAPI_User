import subprocess
import sys
import time
import asyncio
from commons_telegram import *


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        time.sleep(5)

    except Exception as e:
        asyncio.run(log_with_bot('e', e))


if __name__ == '__main__':
    print("No New Package to install !!!")
