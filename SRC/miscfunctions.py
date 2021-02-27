def GSTaddedCost(OriginalCost,GST):
    GSTAmount = (OriginalCost*GST) / 100.
    NetPrice = OriginalCost + GSTAmount
    return NetPrice
