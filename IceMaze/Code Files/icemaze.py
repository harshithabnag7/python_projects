"""
File: icemaze.py
Author: HARSHITHA BENAKANAHALLI NAGARAJ

Main implementation where maze is read from a file, constructs a graph, finds out
from which squares one can escape and
for those squares from which one can escape,how quickly one can run.

"""

import sys
import graph
import searchAlgos


def icemaze_shortest_path(icemaze_building, start, end):
    """
    A  function for building the graph for ice maze..
    :return: None
    """
    if icemaze_building is None:
        return -1
    # add all the edges to the graph
    ice_maze = graph.Graph()
    for ice, rock in icemaze_building.items():
        for star in rock:
            # this automatically creates a new vertices if not already present
            ice_maze.addEdge(ice, star)
    path = searchAlgos.findShortestPath(ice_maze.getVertex(start), ice_maze.getVertex(end))
    return len(path) - 1


def build_icemaze(start, end, lines_of_list, column, row):
    icemaze = {}
    queue = []
    visited = []
    queue.append(start)

    while len(queue) != 0:
        pos = queue.pop(0)
        string_list = ','.join(str(e) for e in pos)
        pos1 = pos.copy()
        icemaze[string_list] = []
        '''
        Right direction traversal to build a graph
        '''
        for i in range(pos[1], int(row)):
            if lines_of_list[pos[0]][i] == '*':
                pos1 = [pos[0], i - 1]
                break
            else:
                pos1 = [pos[0], i]
        if pos1 == end:
            icemaze[string_list].append(','.join(str(g) for g in pos1))
            return icemaze
        else:
            if pos1 not in visited:
                queue.append(pos1)
                visited.append(pos1)
            icemaze[string_list].append(','.join(str(f) for f in pos1))

        '''
        Left direction traversal to build a graph
        '''
        for i in range(pos[1], -1, -1):
            if lines_of_list[pos[0]][i] == '*':
                pos1 = [pos[0], i + 1]
                break
            else:
                pos1 = [pos[0], i]
        if pos1 == end:
            icemaze[string_list].append(','.join(str(g) for g in pos1))
            return icemaze
        else:
            if pos1 not in visited:
                queue.append(pos1)
                visited.append(pos1)
            icemaze[string_list].append(','.join(str(f) for f in pos1))

        '''
        Downwards direction traversal to build a graph
        '''
        for i in range(pos[0], int(column)):
            if lines_of_list[i][pos[1]] == '*':
                pos1 = [i - 1, pos[1]]
                break
            else:
                pos1 = [i, pos[1]]
        if pos1 == end:
            icemaze[string_list].append(','.join(str(g) for g in pos1))
            return icemaze
        else:
            if pos1 not in visited:
                queue.append(pos1)
                visited.append(pos1)
            icemaze[string_list].append(','.join(str(f) for f in pos1))

        '''
        Upward direction traversal to build a graph
        '''
        for i in range(pos[0], -1, -1):
            if lines_of_list[i][pos[1]] == '*':
                pos1 = [i + 1, pos[1]]
                break
            else:
                pos1 = [i, pos[1]]
        if pos1 == end:
            icemaze[string_list].append(','.join(str(g) for g in pos1))
            return icemaze
        else:
            if pos1 not in visited:
                queue.append(pos1)
                visited.append(pos1)
            icemaze[string_list].append(','.join(str(f) for f in pos1))


def main():
    # read the file name
    if len(sys.argv) < 3:
        with open(sys.argv[-1], 'r') as f:
            lines = f.readlines()
            lines_list = []
            first_line = lines[0].rstrip('\n').split(" ")
            lines.pop(0)
            for string in lines:
                each_line = string.rstrip('\n').split(" ")
                lines_list.append(each_line)

            column_num = first_line[0]
            exit_node = first_line[2] + ',' + str(int(column_num) - 1)
            row_num = first_line[1]
            exit_list = exit_node.split(',')
            ints_exit_list = [eval(x) for x in exit_list]
            final_answer = {}

            # to call build graph function for all the nodes.
            for i in range(0, int(row_num)):
                for j in range(0, int(column_num)):
                    if [i, j] == ints_exit_list:
                        final_answer.setdefault(1, []).append((j, i))
                        continue

                    # cannot start if starting position is *
                    if lines_list[i][j] == '*':
                        continue
                    else:
                        icemaze_built = build_icemaze([i, j], ints_exit_list, lines_list, column_num, row_num)
                        number_of_steps = icemaze_shortest_path(icemaze_built, str(i) + ',' + str(j), exit_node)
                        final_answer.setdefault(number_of_steps, []).append((j, i))
            print("Ice Maze built!")
            print("Format -> Number of steps:[(Column Number, Row Number)] ")
            for key in sorted(final_answer):
                if key == -1:
                    print('No Path' + ':' + str(final_answer[key]))
                else:
                    print(str(key) + ':' + str(final_answer[key]))


# main function call.
if __name__ == "__main__":
    print('Loading IceMaze!')
    main()
