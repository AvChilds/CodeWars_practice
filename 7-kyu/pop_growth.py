"""
In a small town the population is p0 = 1000 at the beginning of a year.
The population regularly increases by 2 percent per year and
moreover 50 new inhabitants per year come to live in the town.
How many years does the town need to see its population
greater than or equal to p = 1200 inhabitants?
"""
#p0 - population
#percent - to convert to decimal
#aug - int, number of people coming or going
# p - end result population


def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        percent_dec = float(percent / 100)
        pop_growth_year = int(p0 * percent_dec,) + augj
        p_year = p0 + pop_growth_year
        p0 = p_year
        count += 1

    return count

print(nb_year(1000, 2, 50, 1200))

#result should be 3
