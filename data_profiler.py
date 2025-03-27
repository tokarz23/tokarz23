import pandas as pd
import os


class CheckDq:
    def __init__(self, path):
        self.df = None
        self.path = path

    def data_loader(self):
        path = self.path
        df = pd.read_csv(path)
        self.df = df
        print(df)

    def dq_check(self):
        print(self.df.describe())


