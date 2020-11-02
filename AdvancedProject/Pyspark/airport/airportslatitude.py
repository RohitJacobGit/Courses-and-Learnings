
import sys
sys.path.insert(0, '.')  # root directory

from pyspark import SparkConf, SparkContext, SQLContext
from commons.Utils import Utils

def splitComma(line: str):
    splits = Utils.COMMA_DELIMITER.split(line)
    return '{}:{}'.format(splits[1], splits[6])


if __name__ == '__main__':
    # local[*]=all cores, local=1 core, local=local CPU
    conf = SparkConf().setAppName('AirportLatitude').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # each item in string rdd represents a line
    airports_rdd = sc.textFile('airport/airports.txt')
    print(airports_rdd)

    # sc.stop()

    # airports located in the USA
    # airportsInUSA = airports_rdd.filter(lambda line: line.split(',')[3]=="\"United States\"")
    airportsInUSA = airports_rdd.filter(
        lambda line: float(Utils.COMMA_DELIMITER.split(line)[6])>40)

    airportsAndCityNames = airportsInUSA.map(splitComma)
    airportsAndCityNames.saveAsTextFile('airport/airportslatitude.txt')
