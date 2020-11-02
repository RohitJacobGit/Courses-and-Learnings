from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('reducebykey').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    words = ['one', 'two', 'two', 'three', 'three', 'three']

    wordsRdd = sc.parallelize(words)
    wordsPairRdd = wordsRdd.map(lambda word: (word, 1))

    # wordsPairRdd = sc.parallelize(words).map(lambda word: (word, 1))

    # more efficient for larger datasets
    wcReduceByKey = wordsPairRdd\
                    .reduceByKey(lambda x, y: x + y)\
                    .collect()

    print(' WordCountsWithReduceByKey: {}'.format(list(wcReduceByKey)))

    # dont use unless we have to
    wcGroupByKey = wordsPairRdd\
        .groupByKey()\
        .mapValues(len)\
        .collect()
    # size of each iterable using mapValues(len)
    # https://learning.oreilly.com/videos/apache-spark-with/9781789133394/9781789133394-video4_6

    print(' WordCountsWithGroupByKey: {}'.format(list(wcReduceByKey)))
