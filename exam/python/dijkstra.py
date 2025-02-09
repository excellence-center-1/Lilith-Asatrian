graph = [
    [0,10,5,100,100],
    [100,0,2,100,1],
    [100,3,0,2,9],
    [7,100,100,0,6],
    [100,100,100,4,0]
]

def minimum(my_list):
    m = float('inf')
    m_ind = 0
    for i in range(len(my_list)):
        if my_list[i]==0:
            continue
        if my_list[i]<m:
            m = my_list[i]
            m_ind = i
    return m_ind

my_set = set()
my_set.add(minimum(graph[0]))
print(my_set)