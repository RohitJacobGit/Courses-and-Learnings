from pyspark import SparkConf, SparkContext

if __name__=='__main__':
    conf = SparkConf().setAppName('Joins').setMaster('local[1]')
    sc = SparkContext(conf=conf)

    ages = sc.parallelize([('Maria', 30),('John', 25)])
    addresses = sc.parallelize([('John', 'Turkey'), ('Matt', 'Spain')])

    innerJoin = ages.join(addresses)
    innerJoin.saveAsTextFile('pairRdd/joins/innerJoins.txt')

    leftOuterJoin = ages.leftOuterJoin(addresses)
    leftOuterJoin.saveAsTextFile('pairRdd/joins/leftOuterJoin.txt')

    rightOuterJoin = ages.rightOuterJoin(addresses)
    rightOuterJoin.saveAsTextFile('pairRdd/joins/rightOuterJoin.txt')

    fullOuterJoin = ages.fullOuterJoin(addresses)
    fullOuterJoin.saveAsTextFile('pairRdd/joins/fullOuterJoin.txt')
