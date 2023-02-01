# Get url from DVC
import pandas as pd
import dvc.api

path='../data/wine_original.csv'
repo='/Users/mpaga/desktop/Data_science/DSTI/Courses/MLOps/dsti-mlops-2023-spring/06.data-versioning/data_versioning'

data_url = dvc.api.get_url(
  path=path,
  repo=repo
  )

data = pd.read_csv(data_url, sep=";")
print(data)
