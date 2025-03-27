import great_expectations as gx
import pandas as pd

df = pd.read_csv("/dq_sample.txt")
df_ge = gx.from_pandas(df)

a = df_ge.expect_column_values_to_not_be_null(
   column = ' Name',
   meta = {
     "dimension": "Completeness"
   }
)


print(a)