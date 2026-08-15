// Shortest distance - Dijkstra's algorithm

/* STEP 0: Example of graph representation
For each node, you want to capture the neighboring nodes and the distance to them.
So the keys are the nodes, and the values are objects of neighboring nodes and their distances.
*/
const graph = {
    "A": { "B": 1, "C": 4 },
    "B": { "A": 1, "D": 2 },
    "C": { "A": 4, "D": 1, "E": 2 },
    "D": { "B": 2, "C": 1, "E": 3 },
    "E": { "C": 2, "D": 3 },
};

/* STEP 1: Initialize all the nodes.
Starting node is the node from which the distance is calculated. 
The distance to the starting node is 0, and all other nodes are set to null/infinity/not-known.
*/
function initializeNodes(graph, startNode) {
    const distances = {};
    for (const node in graph) {
        distances[node] = node === startNode ? 0 : Infinity;
    }
    return distances;
};


/* STEP 2: Find the smallest unvisited Node
Find the minimum distance node among all unvisited nodes (from the start node).
We will use the distances object to find it.
*/
function findSmallestUnvisitedNode(distances, visited) {
    let smallestNode = null;
    let smallestDistance = Infinity;

    for (const node in distances) {
        if (!visited.has(node) && distances[node] < smallestDistance) {
            smallestDistance = distances[node];
            smallestNode = node;
        }
    }
    return smallestNode;
};

/* STEP 3: Update distances of neighboring nodes or the edges.
For the smallest unvisited node, we will check its neighbors and update their distances if a shorter path is found.
*/
function updateNeighborDistances(graph, distances, currentNode) {
    const neighbors = graph[currentNode];
    console.log("Neighbors of " + currentNode + " are: ", neighbors);

    for (const neighbor in neighbors) {
        const currentDistanceToNeighbor = distances[neighbor];
        console.log("Current distance to " + neighbor + " is: ", currentDistanceToNeighbor);

        const newDistance = distances[currentNode] + neighbors[neighbor];
        console.log("Calculated distance to " + neighbor + " is: ", newDistance);
        if (newDistance < currentDistanceToNeighbor) {
            distances[neighbor] = newDistance;
        }
    }
};


/* MAIN FUNCTION: Dijkstra's algorithm implementation
This function will use the above helper functions to find the shortest distance from the start node to all other nodes in the graph.
*/
function dijkstra(graph, startNode) {
    const distances = initializeNodes(graph, startNode);
    console.log("Initial distances: ", distances);
    const visited = new Set();
    const lenGraph = Object.keys(graph).length;

    while (visited.size < lenGraph) {
        let smallestNode = findSmallestUnvisitedNode(distances, visited);
        console.log("Smallest Unvisited Node: ", smallestNode);

        updateNeighborDistances(graph, distances, smallestNode);
        console.log("Updated distances: ", distances);
        console.log();
        visited.add(smallestNode);
    }
}

dijkstra(graph, "A");
