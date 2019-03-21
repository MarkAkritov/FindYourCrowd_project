import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from glob import glob


class Data:

	"""Class for Data manipulation"""

	def __init__(self, df):
	 	
		self.df = df

	def select_dtypes(self):

		data_num = self.df.select_dtypes(exclude="object")
		data_obj = self.df.select_dtypes(include="object")

		return (data_num, data_obj)

	def drop_col(self, col_or_ls):

		return self.df.drop(col_or_ls, axis=1, inplace=True)

