# reducebykey
    # combine o/p by a common key on each partition before shuffling 
    # Level 1
        # combine on partition 1: (a,2), (b,2)
        # combine on partition 2: (a,1), (b,3)
        # combine on partition 3: (a,4), (b,1)
    # shuffle such that final result has 
    # Level 2
        # partition 1: reduce by: (a,7)
        # partition 1: reduce by: (b,6)

# reducing the amount of shuffling in groupbykey
    # loss of data transmission over network which can be reduced
    # before any transformation
        # use hash partition: to shuffle data with the same key at the same worker
            # make partition using key of pairRDD
                # combine on partition 1: (a,1), (b,2)
                # combine on partition 2: (b,2), (c,3)
                # combine on partition 3: (a,2), (c,3)
            # shuffle data with same key on same worker partition
                # combine on partition 1: (a,1), (a,2)
                # combine on partition 2: (b,2), (b,2)
                # combine on partition 3: (c,3), (c,3)
            # reduce by
                # partition 1: (a,3)
                # partition 2: (a,4)
                # partition 3: (a,6)


