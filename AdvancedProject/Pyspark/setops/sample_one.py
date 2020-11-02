
from pyspark import SparkContext, SparkConf

if __name__=='__main__':

    conf = SparkConf().setAppName('nasaLogSame').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    julyLogs = sc.textFile('input/nasa_19950701.tsv')
    augLogs = sc.textFile('input/nasa_19950801.tsv')

    julyFirstHosts = julyLogs.map(lambda x: x.split('\t')[0])
    augFirstHosts  = augLogs.map(lambda x: x.split('\t')[0])

    # for i in julyFirstHosts.collect():
    #     print(i, end=' ')

    intersection = julyFirstHosts.intersection(augFirstHosts)

    cleanedHostIntersection = intersection.filter(lambda x: x != 'host') # removing the header line
    cleanedHostIntersection.saveAsTextFile('setops/nasaLogSame.txt')
