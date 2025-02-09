def dfs_rec(adj_matrix, visited, s, row):
    # Նշում ենք ընթացիկ գագաթը որպես այցելված
    visited[s] = True
    # Տպում ենք ընթացիկ գագաթը
    row.append(str(s))

    # Ռեկուրսիվ կերպով այցելում ենք հարևան գագաթները,
    # որոնք դեռ այցելված չեն
    for i in range(len(adj_matrix[s])):
        if adj_matrix[s][i] == 1 and not visited[i]:
            dfs_rec(adj_matrix, visited, i, row)
    return ' '.join(row)

if __name__ == "__main__":
    try:
        # Տրված է գրաֆը հարևանության մատրիցայով
        n = int(input("Enter n: "))
        if n<=0:
            raise Exception("n should be natural")
        
        adj_matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            neighbor_row = input(f"Enter neighbors of vertex {i} (space-separated): ").split()
            if neighbor_row:
                for j in neighbor_row:  
                    j = int(j)
                    adj_matrix[i][j] = 1
                    adj_matrix[j][i] = 1
    
        for i in adj_matrix:
            print(i)

        source = int(input("Enter source vertex: "))
        if source<0 or source>n-1:
            raise Exception("Source can not be such value!")
        print("DFS from source:", source)
        
        visited = [False] * len(adj_matrix)
        row = []
        # Կանչում ենք ռեկուրսիվ DFS ֆունկցիան
        print("Result: ", dfs_rec(adj_matrix, visited, source, row))
        
    except Exception as e:
        print("Unexpected exception occured: ", e)
        