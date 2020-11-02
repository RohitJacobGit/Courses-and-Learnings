
import sys
sys.path.insert(0, '.')  # root directory

from pyspark import SparkConf, SparkContext, SQLContext
from commons.Utils import Utils

if __name__=='__main__':

    conf = SparkConf().setAppName('airportNotUsa').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    airportRdd = sc.textFile('airport/airports.txt')
    airportPairRdd = airportRdd.map(lambda x: (
        Utils.COMMA_DELIMITER.split(x)[1], Utils.COMMA_DELIMITER.split(x)[3]))

    airportNotUsaPairRdd = airportPairRdd.filter(
        lambda kv: kv[1] != "\"United States\"")

    airportNotUsaPairRdd.saveAsTextFile('pairRdd/op_air_not_usa.txt')
    
