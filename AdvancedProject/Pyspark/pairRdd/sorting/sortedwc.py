from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('reducebykey').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    lines = sc.textFile('input/word_count.txt')
    wordRdd = lines.flatMap(lambda line: line.split(' '))

    wordPairRdd = wordRdd.map(lambda word: (word, 1))
    wordCounts = wordPairRdd.reduceByKey(lambda x, y: x + y)

    sortedWordCounts = wordCounts\
        .sortBy(lambda wordCount: wordCount[1], ascending=False)

    for key, value in sortedWordCounts.collect():
        print('{}:{}'.format(key, value))
