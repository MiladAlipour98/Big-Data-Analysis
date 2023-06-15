from pyspark import SparkConf, SparkContext
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number
import pyspark.sql.functions as f
import pyspark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

# part one) sort based on most feedback (only top 10 will be showed)
df = spark.read.json("reviews_MP3_Players_and_Accessories.json")
df2 = df.groupBy('asin').count()
df2 = df2.sort("count",ascending=False).limit(10)
df2.show()

#part two) sort based on worst feedback
df3 = df.groupBy('asin').count()
df3 = df3.sort("count",ascending=True).limit(10)
df3.show()


# #part three) sort based on average overall (top 10)
df4 = df.groupBy('asin').avg('overall')
df4.sort("avg(overall)",ascending=False).limit(10).show()


# #part Four) sort based on average overall (worst 10)
df4 = df.groupBy('asin').avg('overall')
df4.sort("avg(overall)",ascending=True).limit(10).show()

# part five)
inner_df = df4.join(df2, 'asin', how = "inner")
topTenOutput = inner_df.sort(['avg(overall)','count'],ascending = False).limit(10)
topTenOutput.write.option("header",True).csv("topTen.csv")

#part six)
inner_df_2 = df4.join(df2, 'asin', how = "inner")
worstTenOutput = inner_df_2.sort(['avg(overall)','count'],ascending = True).limit(10)
worstTenOutput.write.option("header",True).csv("worstTen.csv")
