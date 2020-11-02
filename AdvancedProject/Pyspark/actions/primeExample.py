from pyspark import SparkContext, SparkConf


if __name__=='__main__':
    
    conf = SparkConf().setAppName('collectExample').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    pr_nos = sc.textFile('input/prime_nums.txt')

    pr_nos_splitted = pr_nos.flatMap(lambda x: x.split('\t'))

    for i in pr_nos_splitted.collect():
        print(i, end=' ')
        
    pr_nos_filtered = pr_nos_splitted.filter(lambda x: x) # filter out empty strings if present

    pr_nos_integers = pr_nos_filtered.map(lambda x: int(x)) # convert to string

    summed = pr_nos_integers.reduce(lambda x, y: x+y)

    print('sum: {}'.format(summed))
