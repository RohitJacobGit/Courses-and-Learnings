import sys
sys.path.insert(0, '.')
from commons.Utils import Utils
from pyspark import SparkConf, SparkContext

if __name__=='__main__':

    conf = SparkConf().setAppName("airports").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    lines = sc.textFile("airport/airports.txt")

    countryAndAirportNameAndPair = lines.map(lambda airport:
                                             (Utils.COMMA_DELIMITER.split(airport)[3],
                                              Utils.COMMA_DELIMITER.split(airport)[1]))

    airportsByCountry = countryAndAirportNameAndPair.groupByKey()

    for country, airportName in airportsByCountry.collectAsMap().items():
        print("{}: {}".format(country, list(airportName)))
