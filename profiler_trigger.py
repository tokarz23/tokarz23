import data_profiler
import sys
import pandas as pd

sys.path.append("/")

dq_file_path = r"C:\Users\tokar\PycharmProjects\DQ\dq_sample.txt"
profiler_obj = data_profiler.CheckDq(dq_file_path)
profiler_obj.data_loader()



