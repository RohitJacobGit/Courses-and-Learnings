from pyspark import SparkConf, SparkContext, StorageLevel

if __name__ == '__main__':
    conf = SparkConf().setAppName('collectExample').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    inputs = [1, 2, 3, 4, 5]

    ip = sc.parallelize(inputs)

    ip.persist(storageLevel = StorageLevel.MEMORY_ONLY) # to remove cache, use unpersist()

    print('product is: {}'.format(ip.reduce(lambda x, y: x*y))) # some action on rdd

    print('count is {}'.format(ip.count())) # another action on rdd , but the rdd doesnt need be parallized again due to persistence in memory

