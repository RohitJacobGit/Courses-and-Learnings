from pyspark import SparkConf, SparkContext

if __name__=='__main__':
    conf = SparkConf().setAppName('tuple').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    tuples = [('rohit', 35),('anand', 25),('pugli', 56)]
    paidRdd = sc.parallelize(tuples) # pair rdd contains tuples/key-value pairs

    paidRdd.coalesce(1).saveAsTextFile('pairRdd/op_from_tuple.txt')