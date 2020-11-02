from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('tuple').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    lists = ['rohit 35', 'anand 25' , 'pugli 56']
    regular_rdd = sc.parallelize(lists)

    pairRdd = regular_rdd.map(lambda x: (x.split(' ')[0], x.split(' ')[1])) # pair rdd contains tuples/key-value pairs
    pairRdd.coalesce(1).saveAsTextFile('pairRdd/op_from_reg_rdd.txt')
