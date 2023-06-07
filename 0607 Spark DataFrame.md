from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("trip_count_sql").getOrCreate()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("trip_count_sql").getOrCreate()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("trip_count_sql").getOrCreate()

import pandas as pd

titanic_pdf = pd.read_csv(filepath, header='infer')
titanic_pdf.head()

#### pandas DataFrame의 head()와 spark DataFrame head() 비교 및 print() 적용 시 차이
* pandas DataFrame의 head(N)는 Dataframe의 선두 N개 Record를 가지는 DataFrame을 반환
* spark DataFrame의 head(N)는 DataFrame의 선두 N개 Row Object를 list로 반환. 
* spark DataFrame의 limit(N)가 DataFrame의 선두 N개 Record를 가지는 DataFrame을 반환. 
* pandas DataFrame은 print() 적용 시 DataFrame의 내용을 출력하지만 spark DataFrame은 DataFrame의 schema만 출력

titanic_sdf.head(5)

# limit : Transformations
titanic_sdf.limit(5).show()

# limit : Transformations
titanic_sdf.limit(5).show()

# spark dataframe을 pandas dataframe으로 만들기
titanic_sdf.select("Pclass", "Embarked").toPandas()

## pandas DataFrame의 info()에 대응하는 Spark DataFrame 메소드 및 로직
* pandas DataFrame의 info()는 컬럼명, data type과 not null 건수를 함께 출력
* spark DataFrame의 info() 메소드가 없으며 대신 printSchema() 메소드로 스키마(컬럼명, data type)만 출력
* not null 건수를 위해서는 별도의 SQL성 쿼리 작성 필요.

# spark df의 타입은 java object type
titanic_sdf.printSchema()

# SQL의 count case when과 유사한 로직으로 null 값을 포함한 컬럼 확인
#  문제는 파이썬에서 Null값을 NaN, Null을 모두 사용한다.
from pyspark.sql.functions import count, isnan, when, col

# Spark DF에서 컬럼만 확인
titanic_sdf.columns

# 위의 나온 컬럼 별로 NaN값의 존재 여부 파악 및 개수를 세야 한다.
titanic_sdf.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in titanic_sdf.columns]).show()

def check_spark_null(spark_df):
    return spark_df.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in spark_df.columns])

check_spark_null(titanic_sdf).show()


## pandas DataFrame describe()와 spark DataFrame describe() 비교
* spark dataframe은 pandas dataframe과 비슷하게 describe()를 통해 모든 컬럼값들의 건수/평균/표준편차/최소값/최대값 등의 정보를 확인할 수 있음. 다만 percentile값을 만들지 않음. 
* pandas dataframe과 다르게 describe()시 숫자형 컬럼 뿐만 아니라 문자형 컬럼에 대해서도 건수/평균/표준편차/최소값/최대값 조사

titanic_pdf.describe()

titanic_sdf.describe().show()

# 숫자 형태의 데이터에 대해서만 describe 해보기
titanic_sdf.dtypes

number_columns = [ column_name for column_name, dtype in titanic_sdf.dtypes if dtype != 'string' ]
number_columns

titanic_sdf.select(number_columns).describe().show()

## pandas DataFrame의 shape에 이에 대응하는 spark Dataframe 로직
* pandas DataFrame의 shape는 row건수와 column 개수를 매우 빠르게 제공.
* spark DataFrame은 shape를 제공하지 않음. column 개수는 spark DataFrame의 columns로 확인. row건수는 count() 메소드(쿼리성)로 확인.

titanic_pdf.shape

# Spark DataFrame에서 컬럼 개수 얻어내기
print("컬럼 개수 :", len(titanic_sdf.columns))

print("데이터 개수 :", titanic_sdf.count())

print("titanic_sdf shape :", (titanic_sdf.count(), len(titanic_sdf.columns)))

## Spark DataFrame의 select() 메소드 알아보기⭐️
* select() 메소드는 SQL의 Select 절과 유사하게 한개 이상의 컬럼들의 값을 DataFrame형태로 반환. 
* 한개의 컬럼명, 또는 여러개의 컬럼명을 인자로 입력할 수 있음.
* 개별 컬럼명을 문자열 형태로 또는 DataFrame의 컬럼 속성으로 지정
* DataFrame의 컬럼 속성으로 지정시에는 DataFrame.컬럼명, DataFrame[컬럼명], col(컬럼명) 으로 지정 가능.

# Pandas 데이터프레임에서 단일 컬럼값 가져오기
titanic_pdf['Name']

titanic_pdf[["Name", "Fare"]]

# Spark DataFrame의 select 사용
titanic_sdf.select("Name").show() # select name from titanic_sdf

# 여러 개의 컬럼을 select
titanic_sdf.select("Name", "Fare").show() # select(*args)

select_columns = titanic_sdf.columns
select_columns.remove("Name")
select_columns

# *list를 사용하거나 list를 그대로 사용해서 데이터를 조회
#   *list : list내의 모든 원소를 unpack 한다. 스파크 데이터프레임에서는 리스트가 아닌, 컬럼의 목록이 그대로 들어가는 것이 원칙!
# select("A", "B", "C") 처럼 선택하는 것이 원칙! 버전 업이 되면서 select(["A", "B", "C"]) 처럼 리스트가 그대로 들어갈 수 있게 됨!
print(select_columns)
print(*select_columns)

titanic_sdf.select(select_columns).show()
titanic_sdf.select(*select_columns).show() # 이렇게 쓰는 것이 원칙!

# 컬럼 속성으로 지정하기. 브라켓( [ ] )을 활용하여 컬럼지정
#  pandas dataframe의 브라켓은 "컬럼을 포함한 배열(시리즈, DataFrame)"
#  spark dataframe의 브라켓은 "컬럼 자체"를 지정
titanic_sdf['Name']

titanic_pdf["Name"]

titanic_sdf.select(titanic_sdf["Name"]).show()

titanic_sdf.Fare * 100

titanic_sdf.select(titanic_sdf.Fare, titanic_sdf.Fare * 100).show()

# 스파크 데이터 프레임에서 컬럼을 다룰 때 가장 많이 사용하는 방식
from pyspark.sql.functions import col

titanic_sdf.select(col("Name"), col("Fare")).show()

from pyspark.sql.functions import upper, lower, col

# 1. 브라켓을 활용해서 함수 연산 적용
titanic_sdf.select("Name", upper(titanic_sdf["Name"])).show()

# 2. .을 활용해서 함수 연산 적용
titanic_sdf.select("Name", upper(titanic_sdf.Name)).show()

# 3. col을 활용해서 함수 연산 적용
titanic_sdf.select("Name", upper(col("Name")).alias("Cap Name")).show()

## spark DataFrame filter() 메소드 알아보기
* filter()는 SQL의 where와 유사하게 DataFrame내의 특정 조건을 만족하는 레코드를 DataFrame으로 반환. 
* filter()내의 조건 컬럼은 컬럼 속성으로 지정 가능. 조건문 자체는 SQL 과 유사한 문자열로 지정 할 수 있음(조건 컬럼은 문자열 지정이 안됨. )
* where() 메소드는 filter()의 alias이며 SQL where와 직관적인 동일성을 간주하기 위해 생성. 
* 복합 조건 and는 & 를, or를 | 를 사용. 개별 조건은 ()로 감싸야 함.

titanic_sdf.filter(col("Embarked") == "Q").show()
# titanic_sdf.filter("Embarked" == "Q").show()

titanic_sdf.where(col("Embarked") == "Q").show()

titanic_sdf.filter("Embarked == 'Q'").show()

# Embarked가 "S"이고, Pclass가 1인 사람의 정보
titanic_sdf.filter( (col("Embarked") == 'S') & (col("Pclass") == 1) ).show()

# Embarked가 "S"이거나 Pclass가 1인 사람의 정보
titanic_sdf.filter( (col("Embarked") == 'S') | (col("Pclass") == 1) ).show()

# 이름에 Miss가 들어가는 사람의 정보 가져오기
titanic_sdf.filter( col("Name").like("%Miss%")).show()

# 이름이 H로 시작하는 사람
titanic_sdf.filter( col("Name").like("H%")).show()

titanic_sdf.filter(lower(col("Name")).like("h%")).show()

titanic_sdf.filter("Name like '%Mr%'").show()

titanic_sdf.filter(" lower(Name) like '%mr%'").show() # 별도의 pyspark.sql.functions 호출이 없이 사용이 가능.

titanic_sdf.filter(upper(col("Name")).like("%MISS%")).select("Pclass", "Embarked", "Name").show()

spark.stop()
