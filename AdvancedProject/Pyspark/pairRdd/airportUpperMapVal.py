

import sys
sys.path.insert(0, '.')  # root directory

from commons.Utils import Utils
from pyspark import SparkConf, SparkContext, SQLContext

if __name__ == '__main__':

    conf = SparkConf().setAppName('airportNotUsa').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    airportRdd = sc.textFile('airport/airports.txt')
    airportPairRdd = airportRdd.map(lambda x: (
        Utils.COMMA_DELIMITER.split(x)[1], Utils.COMMA_DELIMITER.split(x)[3]))

    airportUpper = airportPairRdd.mapValues(lambda value: value.upper()) # only takes the values by default from KV to modify

    airportUpper.saveAsTextFile('pairRdd/op_air_upper.txt')
