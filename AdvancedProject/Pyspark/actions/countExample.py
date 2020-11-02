from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('collectExample').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    inputWords = ['India', 'Africa', 'China',
                  'India', 'India', 'China', 'Brazil']

    wordRDD = sc.parallelize(inputWords)

    print('Number of elements: {}'.format(wordRDD.count()))

    wordRDD_dict = wordRDD.countByValue()

    for key, value in wordRDD_dict.items():
        print('{}: {}'.format(key, value))
