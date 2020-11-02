from pyspark import SparkConf, SparkContext

if __name__=='__main__':
    conf = SparkConf().setAppName('collectExample').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    inputWords = ['India','Africa','China','India','India','China','Brazil']

    wordRDD = sc.parallelize(inputWords)

    for i in wordRDD.collect():
        print(i, end=' ')