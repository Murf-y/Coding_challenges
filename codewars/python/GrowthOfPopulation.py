def nb_year(p0, percent, aug, p):
    perc = round(p0 * percent/100)
    total_population = p0 + (perc) + aug
    year = 1
    while(total_population < p):
        perc = round(total_population * percent/100)
        total_population = total_population + perc + aug
        year += 1

    return year
