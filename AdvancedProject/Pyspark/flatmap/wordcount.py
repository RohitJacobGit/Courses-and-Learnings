# flatmap: we want to produce multiple element as an output for each input element
# https://code.visualstudio.com/docs/python/jupyter-support-py

from pyspark import SparkContext, SparkConf

if __name__=='__main__':

    conf = SparkConf().setAppName('Wordcount').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    lines = sc.textFile('word_count.txt')

    # words = lines.map(lambda x: x.split(' '))
    '''
    I am Rohit. I am crazy.
    map: ['I','am','Rohit.']['I','am','crazy.']
    flatmap: I 
            am 
            Rohit. 
            I 
            am 
            crazy.
    '''
    # for x in words.collect():
    #     print(x)

    words = lines.flatMap(lambda x: x.split(' '))

    # for x in words.collect():
    #     print(x)

    word_count = words.countByValue() # dictionary

    for key, value in word_count.items():
       print('{}:{}'.format(key, value))
    



   
    # map??
    # from pyspark import SparkContext
    # sc = SparkContext()
    # rdd = sc.parallelize(['b','a','c'])
    # print(sorted(rdd.map(lambda x: (x,1)).collect()))

    # rdd = sc.parallelize([2,3,4])
    # print(sorted(rdd.flatMap(lambda x: range(1,x)).collect()))

    # rdd = sc.parallelize([2, 3, 4])
    # print(sorted(rdd.flatMap(lambda x: [(x,x),(x,x)]).collect()))

