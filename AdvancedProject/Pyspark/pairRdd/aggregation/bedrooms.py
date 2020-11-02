import sys
sys.path.insert(0,'.')
from pyspark import SparkConf, SparkContext
from pairRdd.aggregation.AvgCnt import AvgCnt

if __name__=='__main__':

    conf = SparkConf().setAppName('reducebykey').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    lines = sc.textFile('input/RealEstate.csv')

    # remove header
    cleanedLines = lines.filter(lambda line: 'Bedrooms' not in line)
    housePricePairRdd = cleanedLines.map(lambda line:
                                         (line.split(",")[3], AvgCnt(1, float(line.split(",")[2]))))

    housePriceTotal = housePricePairRdd \
        .reduceByKey(lambda x, y: AvgCnt(x.count + y.count, x.total + y.total))

    print("housePriceTotal: ")
    for bedroom, avgCount in housePriceTotal.collect():
        print("{} : ({}, {})".format(bedroom, avgCount.count, avgCount.total))

    housePriceAvg = housePriceTotal.mapValues(
        lambda avgCount: avgCount.total / avgCount.count)
    print("\nhousePriceAvg: ")
    for bedroom, avg in housePriceAvg.collect():
        print("{} : {}".format(bedroom, avg))
