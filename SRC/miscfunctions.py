def GSTaddedCost(OriginalCost,GST):
    GSTAmount = (OriginalCost*GST) / 100.
    NetPrice = OriginalCost + GSTAmount
    return NetPrice


def validate_decimal(s):
    return (s.replace('.', '', 1).isdecimal())


def validate_string(s):
    return (s.isalpha())


def validate_number(s: str):
    return (s.isdigit())
