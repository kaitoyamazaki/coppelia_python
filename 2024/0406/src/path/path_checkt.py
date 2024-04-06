from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import pandas as pd
from time import sleep

class Path:

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

def main():
    print(f'プログラム開始')
    path = Path()
    try:
        pass

    except KeyboardInterrupt:
        pass

    finally:
        print(f'プログラム終了')

if __name__ == '__main__':
    main()