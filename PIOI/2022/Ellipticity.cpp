#include <bits/stdc++.h>

#define ll long long
#define lli long long int
#define li long int
#define ld long double
using namespace std;
const lli mod = 1e9 + 7;

constexpr int64_t INF = numeric_limits<int64_t>::max();

/**
 * @namespace graph
 * @brief Graph Algorithms
 */

namespace graph
{
    /**
 * @brief Function that add edge between two nodes or vertices of graph
 *
 * @param u any node or vertex of graph
 * @param v any node or vertex of graph
 */
    void addEdge(vector<vector<pair<int, int>>> *adj, int u, int v,
                 int w)
    {
        (*adj)[u - 1].push_back(make_pair(v - 1, w));
        (*adj)[v - 1].push_back(make_pair(u - 1, w));

        // (*adj)[v - 1].push_back(make_pair(u - 1, w));
    }

    /**
 * @brief Function runs the dijkstra algorithm for some source vertex and
 * target vertex in the graph and returns the shortest distance of target
 * from the source.
 *
 * @param adj input graph
 * @param s source vertex
 * @param t target vertex
 *
 * @return shortest distance if target is reachable from source else -1 in
 * case if target is not reachable from source.
 */
    int dijkstra(vector<vector<pair<int, int>>> *adj, int s, int t, vector<vector<vector<int64_t>>> *parents)
    {
        /// n denotes the number of vertices in graph
        int n = adj->size();

        /// setting all the distances initially to INF
        vector<int64_t> dist(n, INF);

        /// creating a min heap using priority queue
        /// first element of pair contains the distance
        /// second element of pair contains the vertex
        priority_queue<pair<int, pair<int, vector<int64_t>>>, vector<pair<int, pair<int, vector<int64_t>>>>,
                       greater<pair<int, pair<int, vector<int64_t>>>>>
            pq;

        /// pushing the source vertex 's' with 0 distance in min heap
        vector<int64_t> z(n, -1);
        pq.push(make_pair(0, make_pair(s, z)));

        /// marking the distance of source as 0
        dist[s] = 0;

        while (!pq.empty())
        {
            /// second element of pair denotes the node / vertex
            int currentNode = pq.top().second.first;
            vector<int64_t> p = pq.top().second.second;
            vector<int64_t> prev = p;

            /// first element of pair denotes the distance
            int currentDist = pq.top().first;

            pq.pop();

            /// for all the reachable vertex from the currently exploring vertex
            /// we will try to minimize the distance
            for (pair<int, int> edge : (*adj)[currentNode])
            {
                /// minimizing distances
                if (currentDist + edge.second < dist[edge.first])
                {
                    dist[edge.first] = currentDist + edge.second;
                    prev[edge.first] = currentNode;
                    (*parents)[edge.first].push_back(prev);
                    pq.push(make_pair(dist[edge.first], make_pair(edge.first, prev)));
                }
                else if (currentDist + edge.second == dist[edge.first])
                {
                    prev[edge.first] = currentNode;
                    (*parents)[edge.first].push_back(prev);
                    pq.push(make_pair(dist[edge.first], make_pair(edge.first, prev)));
                }
            }
        }
        if (dist[t] != INF)
        {
            return dist[t];
        }
        return -1;
    }
} // namespace graph

/** Main function */
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int vertices = int(), edges = int();
    cin >> vertices;
    cin >> edges;

    vector<vector<pair<int, int>>> adj(
        vertices, vector<pair<int, int>>());

    vector<int> A(vertices);

    for (int i = 0; i < vertices; i++)
    {
        cin >> A[i];
    }

    int u = int(), v = int(), w = int();
    while (edges--)
    {
        cin >> u >> v >> w;
        graph::addEdge(&adj, u, v, w);
    }

    vector<vector<vector<int64_t>>> parents(vertices, vector<vector<int64_t>>());

    int dist = graph::dijkstra(&adj, 0, vertices - 1, &parents);

    int result = 0;

    for (auto parent : parents[vertices - 1])
    {
        vector<int64_t> B;
        B.clear();
        B.push_back(A[vertices - 1]);
        int x = parent[vertices - 1];

        while (x != -1)
        {
            B.push_back(A[x]);
            x = parent[x];
        }

        sort(B.begin(), B.end());
        int n = B.size();
        int median;

        if (n & 1)
        {
            median = B[n / 2];
        }
        else
        {
            median = (B[n / 2] + B[(n / 2) - 1]) / 2;
        }

        result = max(result, median);
    }

    cout << dist << " " << result << endl;
    return 0;
}
