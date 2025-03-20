def reduce_fraction(fraction):
    n, d = fraction
    while d != 0:
        n, d = d, n % d
    return (fraction[0]/n, fraction[1]/n)


print (reduce_fraction([210,700]))





