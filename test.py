# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, dense_rank
# from pyspark.sql.window import Window
#
# # Initialize Spark
# spark = SparkSession.builder.appName("SecondHighestSalary").getOrCreate()
#
# # Create Employees DataFrame
# employee_data = [
#     ("James", 1, "NY", 90000, 34, 10000),
#     ("Michael", 1, "NY", 86000, 56, 20000),
#     ("Robert", 1, "CA", 81000, 30, 23000),
#     ("Maria", 2, "CA", 90000, 24, 23000),
#     ("Raman", 2, "CA", 99000, 40, 24000),
#     ("Scott", 2, "NY", 83000, 36, 19000),
#     ("Jen", 2, "NY", 79000, 53, 15000),
#     ("Jeff", 4, "CA", 80000, 25, 18000),
#     ("Kumar", 4, "NY", 91000, 50, 21000),
# ]
# columns_emp = ["employee_name", "deptid", "state", "salary", "age", "bonus"]
# df_employees = spark.createDataFrame(employee_data, columns_emp)
#
# # Create Departments DataFrame
# department_data = [
#     ("Sales", 1),
#     ("Sales", 1),
#     ("Sales", 1),
#     ("Finance", 2),
#     ("Sales", 1),
#     ("Finance", 2),
#     ("Finance", 2),
#     ("Marketing", 4),
#     ("Marketing", 4),
# ]
# columns_dept = ["department", "deptid"]
# df_departments = spark.createDataFrame(department_data, columns_dept)
#
# # Remove duplicate departments
# df_departments = df_departments.dropDuplicates()
#
# # Join DataFrames
# joined_df = df_employees.join(df_departments, on="deptid", how="inner")
#
# # Define Window for dense_rank
# window_spec = Window.partitionBy("deptid").orderBy(col("salary").desc())
#
# # Rank salaries and filter second highest
# ranked_df = joined_df.withColumn("rank", dense_rank().over(window_spec)) \
#                      .filter(col("rank") == 2) \
#                      .select("employee_name", "salary", "department")
#
# # Show result
# ranked_df.show()
# def log(func):
#     print('inside log func')
#     def wrapper(*args, **kwargs):
#         print("Calling", func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
# @log
# def func():
#     print('hello ashutosh')
#
#
# if __name__ == '__main__':
#     func()


a = {1,2,3}
b = {3,4,5}
# a = [1,2]

# print(list(map(lambda x: x*x, range(5))))


# a = lambda x: 'even' if x % 2 == 0 else 'odd'

# print(list(map(lambda x,y: x+y, a, b)))

# print(list(filter(None, [0, 1, "", "hi"])))

# m =
from functools import reduce
print((reduce(lambda x,y: x if x>y else y, [2,5,1])))

print(list(map(lambda x,y: x if x>y else y, [1,5,2], [0,8,9])))


