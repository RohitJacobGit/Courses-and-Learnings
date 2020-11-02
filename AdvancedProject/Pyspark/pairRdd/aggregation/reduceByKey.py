from pyspark import SparkConf, SparkContext

if __name__=='__main__':
    conf = SparkConf().setAppName('reducebykey').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    # if disk memory is limited, wordcount.py will overflow for a huge text file, so use reduceByKey

    lines = sc.textFile('input/word_count.txt')
    wordRdd = lines.flatMap(lambda line: line.split(' '))
    wordPairRdd = wordRdd.map(lambda word: (word,1))

    wordCounts = wordPairRdd.reduceByKey(lambda  x, y: x + y)
    
    for key, value in wordCounts.collect():
        print('{}:{}'.format(key, value))