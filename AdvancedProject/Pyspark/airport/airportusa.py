#import sys
#sys.path.append('/Applications/Utilities/anaconda3/lib/python3.7/site-packages')
#from common import utils

import sys
sys.path.insert(0,'.') # root directory
from commons.Utils import Utils
from pyspark import SparkConf, SparkContext, SQLContext


def splitComma(line: str):
    splits = Utils.COMMA_DELIMITER.split(line)
    return '{}:{}'.format(splits[1], splits[2])

if __name__=='__main__':
    conf = SparkConf().setAppName('Airport').setMaster('local[2]') # local[*]=all cores, local=1 core, local=local CPU
    sc = SparkContext(conf = conf)

    airports_rdd = sc.textFile('airport/airports.txt') # each item in string rdd represents a line
    print(airports_rdd)

    # sc.stop()

    # airports located in the USA
    # airportsInUSA = airports_rdd.filter(lambda line: line.split(',')[3]=="\"United States\"")
    airportsInUSA = airports_rdd.filter(
        lambda line: Utils.COMMA_DELIMITER.split(line)[3] == "\"United States\"")
    
    airportsAndCityNames = airportsInUSA.map(splitComma)
    airportsAndCityNames.saveAsTextFile('airport/airportsInUsa.txt')

