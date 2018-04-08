def main():
    allGalaxies = {
        "Galaxy S": 2010,
        "Galaxy S2": 2011,
        "Galaxy S3": 2012,
        "Galaxy S4": 2013,
        "Galaxy S5": 2014,
        "Galaxy S6": 2015,
        "Galaxy S7": 2016,
        "Galaxy S8": 2017,
        "Galaxy S9": 2018,
    }
    printValues(allGalaxies)
    printDict(allGalaxies)
    printKeys(allGalaxies)


def printDict(allGalaxies):
    for key, val in allGalaxies.items():
        print(key, '=>', value)


def printKeys(allGalaxies):
    print(allGalaxies.keys())


def printValues(allGalaxies):
    for year in allGalaxies:
        print(allGalaxies[year])


main()
