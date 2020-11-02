from pyspark.sql import SparkSession

AGE_MIDPOINT = 'age_midpoint'
SALARY_MIDPOINT = 'salary_midpoint'
SALARY_MIDPOINT_BUCKET = 'salary_midpoint_bucket'

if __name__=='__main__':
    session = SparkSession.builder.appName('SOSQL').master('local[1]').getOrCreate()
    # builder factory design pattern
    # getOrCreate: create a spark session if it doesnt exist or get a session if we have already created it

    df_reader_object = session.read

    responses = df_reader_object\
                .option('header','True')\
                .option('inferSchema', value=True)\
                .csv('Pyspark/input/2016-stack-overflow-survey-responses.csv')

    print('-----Print Schema-----')
    responses.printSchema()

    # responses: small sql db sitting in the memory of spark application
    # responses: regular sql db

    # SELECT country,occupation,AGE_MIDPOINT, SALARY_MIDPOINT, SALARY_MIDPOINT_BUCKET FROM TABLE
    selectedRows = responses.select('country','occupation',AGE_MIDPOINT, SALARY_MIDPOINT)
    selectedRows.show()

    # where clause
    selectedRows.filter(selectedRows["country"] == "Afghanistan").show()
