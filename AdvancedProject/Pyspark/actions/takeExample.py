from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('collectExample').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    inputWords = ['India', 'Africa', 'China',
                  'India', 'India', 'China', 'Brazil']

    wordRDD = sc.parallelize(inputWords)

    words_taken = wordRDD.take(3)

    for i in words_taken:
        print(i, end=' ')