import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from pysparky import functions_ext as F_
from pysparky import spark_ext as se
from pysparky import transformation_ext as te

print(pyspark.__version__)

spark = SparkSession.builder.getOrCreate()

data_dict = {"key1": [1, 2, 3], "key2": [3]}
column_names = ["keys", "values"]
df = se.convert_dict_to_dataframe(spark, data_dict, column_names, explode=True)
df.show()
# key1,1
# key2,2

# pyspark.sql.SparkSession.convert_dict_to_dataframe = se.convert_dict_to_dataframe
spark.convert_dict_to_dataframe(data_dict, column_names, explode=True).show()
data_dict.items()
my_list = [1, 2, 3, 4]
spark.createDataFrame(my_list).show()
