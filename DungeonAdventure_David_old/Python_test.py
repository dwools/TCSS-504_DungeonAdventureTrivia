from dungeon import Dungeon
import statistics
dungeon1 = Dungeon(5, 3)
count = 0
maze_totals = []
for i in range(1, 100):
    dungeon1.__init__(5, 3)
    maze_totals.append(dungeon1.get_mazes_created())
    count +=1
    print(count)
# print(maze_totals)
print(statistics.mean(maze_totals))





