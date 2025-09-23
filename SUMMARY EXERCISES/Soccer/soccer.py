from operator import itemgetter


def main():
    filename = input("Which file do you want to use? ")
    # the file is initially read as a list of dictionaries (one record per player)
    playerStats = readFile(filename)

    computeEfficiency(playerStats)

    printBestThree(playerStats, 'fw_eff')
    printBestThree(playerStats, 'mf_eff')

    # here we re-organise our data structure as a dictionary with team names as
    # keys, # each value is then a list of dictionaries, containing the players
    # that belong to that team
    statsByTeam = groupByTeam(playerStats)

    # find and print the three teams with the lowest average age
    # listAge will be a list of elements, each like this:
    # {'team': 'Argentina', 'avgAge': 23}
    listAge = []
    for teamName in statsByTeam:
        # this is the list of players of the current team
        teamPlayers = statsByTeam[teamName]
        avgAge = 0
        for player in teamPlayers:
            avgAge = avgAge + player['age']
        avgAge = avgAge / len(teamPlayers)
        listAge.append({'team': teamName, 'avgAge': avgAge})
    youngestThree = sorted(listAge, key=itemgetter('avgAge'))[:3]
    print("The three teams with the lowest average age are:")
    for elem in youngestThree:
        print(f"{elem['team']:<30s}{elem['avgAge']:30.3f}, years")

    # find and print most efficient team
    # listEff will be structured similarly to listAge, but will contain
    # elements such as:
    # {'team': 'Argentina', 'totEff': 0.1234}
    listEff = []
    for teamName in statsByTeam:
        teamPlayers = statsByTeam[teamName]
        # sort by decreasing efficiency, then iterate over the first three
        teamPlayers.sort(key=itemgetter('fw_eff'), reverse=True)
        totEff = 0
        for player in teamPlayers[:3]:
            totEff += player['fw_eff']
        listEff.append({'team': teamName, 'totEff': totEff})
    # IMPORTANT NOTE: itemgetter can also be used with max()
    bestEff = max(listEff, key=itemgetter('totEff'))
    bestTeam = bestEff['team']
    print("The most efficient team is:", bestTeam)
    # also print the three most efficient players of the bestTeam
    for player in statsByTeam[bestTeam][:3]:
        print(f"{player['player']}'s forward efficiency: {player['fw_eff']:.3f}")


# read the input file as a list of dictionaries
def readFile(filename):
    res = []
    with open(filename, "r") as f:
        # read the first line, which contains the column names
        firstLine = f.readline()
        firstLine = firstLine.strip()
        columnNames = firstLine.split(",")
        # read rest of file from 2nd line to the end
        for line in f:
            line = line.strip()
            fields = line.split(",")
            # convert list of fields to a dictionary and convert numeric fields
            # to integer
            record = {}
            for i in range(len(fields)):
                col = columnNames[i]
                if i >= 3:
                    record[col] = int(fields[i])
                else:
                    record[col] = fields[i]
            # compute the player's age (not directly present in the file, but
            # useful later)
            record['age'] = 2022 - record['birth_year']
            res.append(record)
    return res


# compute forward and midfield efficiency for each player
# modifies the list of dictionaries passed as parameter "in-place"
def computeEfficiency(playerStats):
    for elem in playerStats:
        try:
            fwEff = ((elem['goals'] / elem['minutes']) +
                    (elem['assists'] / elem['minutes']) -
                    (elem['offsides'] / elem['minutes'])
                    )
        except ZeroDivisionError:
            # very negative value... this is not super-clean, could be improved
            # given more information on the problem (what is the efficiency if
            # minutes = 0 or crosses = 0?
            fwEff = -1000
        try:
            mfEff = ((elem['interceptions'] + elem['ball_recoveries'] +
                    elem['assists'] / elem['crosses'] ) / elem['minutes']
                    )
        except ZeroDivisionError:
            mfEff = -1000
        elem['fw_eff'] = fwEff
        elem['mf_eff'] = mfEff


# prints the best three players according to any key in the dictionary.
def printBestThree(playerStats, key):
    sortedByKey = sorted(playerStats, key=itemgetter(key), reverse=True)
    threeBest = sortedByKey[:3]
    print("Name" + " " * 26 + "Team" + " " * 26 + "Efficiency")
    for elem in threeBest:
        name = elem['player']
        team = elem['team']
        eff = elem[key]
        print(f"{name:<30s}{team:<30s}{eff:30.3f}")


# reorganizes the data grouping players from the same team.
# the final structure is a dictionary with key --> team name, and
# value --> list of players. Each list element (one player's data) is also
# a dictionary
def groupByTeam(playerStats):
    res = {}
    for player in playerStats:
        teamName = player['team']
        if teamName not in res:
            res[teamName] = list()
        res[teamName].append(player)
    return res


main()
