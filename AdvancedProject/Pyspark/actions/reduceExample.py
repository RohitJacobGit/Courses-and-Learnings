from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('collectExample').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    inputs = [1,2,3,4,5]

    ip = sc.parallelize(inputs)

    product = ip.reduce(lambda  x, y: x*y)
    print('product is: {}'.format(product))