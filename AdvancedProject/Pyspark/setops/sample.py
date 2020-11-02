# sample: random sample from rdd

from pyspark import SparkContext, SparkConf

def removeHeaderLine(line: str):
    return not (line.startswith('host') and 'bytes' in line)

if __name__=='__main__':

    conf = SparkConf().setAppName('unionLogs').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    julyLogs = sc.textFile('input/nasa_19950701.tsv')
    # for x in julyLogsSample.collect():
    #     print(x)

    augLogs = sc.textFile('input/nasa_19950801.tsv')

    aggregatedFiles = augLogs.union(julyLogs)

    cleanedLogs = aggregatedFiles.filter(removeHeaderLine)
    sample = cleanedLogs.sample(withReplacement=True, fraction=0.1)

    sample.saveAsTextFile('setops/nasalogop.txt')

    

