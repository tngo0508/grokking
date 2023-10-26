def number_of_paths(n, corridors):
    graph = {i + 1: [] for i in range(n)}
    count = 0
    for s, d in corridors:
        graph[s].append(d)
        graph[d].append(s)

    print(graph)
    
    for r1, r2 in corridors:
        nei1 = graph[r1]
        nei2 = graph[r2]
        print(r1, r2)
        tmp = []
        for x in nei1:
            if x in nei2:
                tmp.append(x)
        print(tmp)
        count += len(tmp)
    
    return count // 3

# solution
from collections import defaultdict

def number_of_paths(n, corridors):
    neighbours = defaultdict(set)
    cycles = 0

    for room1, room2 in corridors:
        neighbours[room1].add(room2)
        neighbours[room2].add(room1)
        cycles += len(neighbours[room1].intersection(neighbours[room2]))

    return cycles

# Driver code
def main():
    n_list = [5, 4, 5, 5, 4]
    corridors_list= [[[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]],
                      [[1,2],[3,4]],
                      [[1,2],[5,2],[4,1], [3,1],[3,4]],
                      [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4],[1,5]],
                      [[1,2], [2,3], [3,4]] 
                    ]

    for i in range(len(n_list)):
        print(i + 1, ".\tn: ", n_list[i], sep = "")
        print("\tcorridors: ", corridors_list[i], sep = "")
        print("\tcycles :", number_of_paths(n_list[i], corridors_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()