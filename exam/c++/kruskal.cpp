#include <iostream>
using namespace std;

int find(int i, int* parent) {
    if (parent[i] == -1)
        return i;
    return parent[i] = find(parent[i], parent);
}

void unite(int x, int y, int* parent, int* rank) {
    int s1 = find(x, parent);
    int s2 = find(y, parent);

    if (s1 != s2) {
        if (rank[s1] < rank[s2]) {
            parent[s1] = s2;
        } else if (rank[s1] > rank[s2]) {
            parent[s2] = s1;
        } else {
            parent[s2] = s1;
            rank[s1]++;
        }
    }
}

void kruskals(int V, int edgeCount, int** edges, int* parent, int* rank) {
    for (int i = 0; i < edgeCount - 1; i++) {
        for (int j = 0; j < edgeCount - i - 1; j++) {
            if (edges[j][0] > edges[j + 1][0]) {

                for (int k = 0; k < 3; k++) {
                    int temp = edges[j][k];
                    edges[j][k] = edges[j + 1][k];
                    edges[j + 1][k] = temp;
                }
            }
        }
    }

    int mstWeight = 0;
    cout << "Following are the edges in the constructed MST:" << endl;

    // Process the edges and apply Kruskal's algorithm
    for (int i = 0; i < edgeCount; i++) {
        int w = edges[i][0];
        int u = edges[i][1];
        int v = edges[i][2];

        // If including this edge doesn't form a cycle, include it in the MST
        if (find(u, parent) != find(v, parent)) {
            unite(u, v, parent, rank);
            mstWeight += w;
            cout << u << " -- " << v << " == " << w << endl;
        }
    }

    cout << "Minimum Cost Spanning Tree: " << mstWeight << endl;
}

int main() {
    int edgesCount;
    int vCount;
    int* parent = new int[vCount];
    int* rank = new int[vCount];

    cout << "Enter the number of vertices: ";
    cin >> vCount;
    cout << "Enter the number of edges: ";
    cin>>edgesCount;

    int** edges = new int*[edgesCount];
    for(int i = 0; i<edgesCount; ++i){
        edges[i] = new int[3];
    }

    for(int i = 0; i<edgesCount; ++i){
        for(int j = 0; j<3; ++j){
            cout<<"edges["<<i<<"]["<<j<<"]=";
            cin>>edges[i][j];
        }
    }

    for(int i = 0; i<vCount; ++i){
        parent[i] = -1;
        rank[i] = 1;
    }

    kruskals(vCount,edgesCount, edges, parent, rank);
    for(int i = 0; i<edgesCount; ++i){
        delete []edges[i];
    }
    delete[]edges;
    delete[]parent;
    delete[]rank;
    return 0;
}
