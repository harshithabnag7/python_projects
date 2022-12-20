from collections import namedtuple
import sys

'''
@author : Harshitha Benakanahalli Nagaraj
 file : skyscrapers.py
'''

'''
This program checks whether skyscrapers puzzle file given is valid or not.
If valid, it returns true
else it returns false and mentions the description of rule violated
'''

# Reading file from command line input
with open(sys.argv[-1], 'r') as f:
    lines = f.readlines()
    newList = []

    for strings in lines:
        strings = strings.rstrip('\n').split(" ")
        newList.append(strings)
        Row_list = []
        for z in range(5, len(newList)):
            # inserting values of rows
            Row_list.append(newList[z])
        # transposing row values and storing it in column list
        Column_List = list((map(list, zip(*Row_list))))
    # Creating named tuples
    Clues = namedtuple('Clues', ['North', 'East', 'South', 'West'])
    Grid = namedtuple('Grid', ['Rows'])
    # Inserting values to Named Tuple
    All_clues = Clues(newList[1], newList[2], newList[3], newList[4])
    All_grid = Grid([Row_list])
    # Accessing values from Named Tuple
    list_West = list(All_clues.West)
    list_North = list(All_clues.North)
    list_East = list(All_clues.East)
    list_South = list(All_clues.South)
    [[list_Rows]] = [list(All_grid.Rows)]


# function to check west clues
def west_clue():
    for i in range(0, len(list_West)):
        # to check whether duplicate values are found
        if len(set(list_Rows[i])) != len(list_Rows[i]):
            print("Duplicate Values in Row" + str(i))
            return False
        else:
            buildingCount = 1
            selectedBuilding = int(list_Rows[i][0])
            for j in range(1, len(list_Rows[i])):
                # to check whether value is out of range or 0
                if int(list_Rows[i][j]) == 0 or int(list_Rows[i][j]) > int(newList[0][0]):
                    print("Invalid Value " + str(int(list_Rows[i][j])))
                    return False
                elif int(list_Rows[i][j]) > selectedBuilding and buildingCount <= int(list_West[i]):
                    buildingCount += 1
                    selectedBuilding = int(list_Rows[i][j])
                else:
                    pass
            if buildingCount == int(list_West[i]):
                pass
            else:
                print("Rule violated")
                return False
    print("Valid puzzle")
    return True


# function to compute east clue values
def east_clue():
    for i in range(0, len(list_East)):
        if len(set(list_Rows[i])) != len(list_Rows[i]):
            print("Duplicate values in row" + str(i))
            return False
        else:
            buildingCount = 1
            selectedBuilding = int(list_Rows[i][-1])
            for j in range(len(list_Rows[i]) - 2, -1, -1):
                if int(list_Rows[i][j]) == 0 or int(list_Rows[i][j]) > int(newList[0][0]):
                    print("Invalid Value " + str(int(list_Rows[i][j])))
                    return False
                elif int(list_Rows[i][j]) > selectedBuilding and buildingCount <= int(list_East[i]):
                    buildingCount += 1
                    selectedBuilding = int(list_Rows[i][j])
                else:
                    pass
            if buildingCount == int(list_East[i]):
                pass
            else:
                print("More buildings are seen")
                return False
    return True


# function to solve south clue values
def south_clue():
    for i in range(0, len(list_North)):
        if len(set(Column_List[i])) != len(Column_List[i]):
            print("Duplicate values in  column" + str(i))
            return False
        else:
            buildingCount = 1
            selectedBuilding = int(Column_List[i][-1])
            for j in range(len(Column_List[i]) - 2, -1, -1):
                if int(Column_List[i][j]) == 0 or int(Column_List[i][j]) > int(newList[0][0]):
                    print("Invalid Value " + str(int(Column_List[i][j])))
                    return False
                elif int(Column_List[i][j]) > selectedBuilding and buildingCount <= int(list_South[i]):
                    buildingCount += 1
                    selectedBuilding = int(Column_List[i][j])
                else:
                    pass
            if buildingCount == int(list_South[i]):
                pass
            else:
                print("Rule violated")
                return False
    return True


# function to solve North clues
def north_clue():
    for i in range(0, len(list_North)):
        if len(set(Column_List[i])) != len(Column_List[i]):
            print("Duplicate values in Column " + str(i))
            return False
        else:
            buildingCount = 1
            selectedBuilding = int(Column_List[i][0])
            for j in range(1, len(Column_List[i])):
                if int(Column_List[i][j]) == 0 or int(Column_List[i][j]) > int(newList[0][0]):
                    print("Invalid Value " + str(int(Column_List[i][j])))
                    return False
                elif int(Column_List[i][j]) > selectedBuilding and buildingCount <= int(list_North[i]):
                    buildingCount += 1
                    selectedBuilding = int(Column_List[i][j])
                else:
                    pass
            if buildingCount == int(list_North[i]):
                pass
            else:
                print("Rule violated in position")
                return False
    return True


# main function call
def main():
    # execute all the clues
    print(north_clue() and south_clue() and east_clue() and west_clue())
    # printing output file
    filename = sys.argv[-1][:-4] + '-out.txt'
    with open(filename, 'r') as f1:
        print(f1.read())


if __name__ == "__main__":
    main()
