class Edge:
    def __init__(self, u, v, w, r=False):
        self.source = u
        self.sink = v
        self.capacity = w
        self.reverse = r
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork:
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0, True)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path and edge.redge not in path:
                result = self.find_path( edge.sink, sink, path + [edge])
                if result != None:
                    return result

    def maxLength_path(self, source, sink):
        if source == sink:
            return []

        children = []
        for edge in self.adj[source]:
            if not edge.reverse:
                children.append((edge.sink, edge))

        # print(source, ":", children)

        maxPath = []
        firstEdge = None
        maxPathLength = -1
        for value in children:
            child, sourceChildEdge = value
            path = self.maxLength_path(child, sink)
            # print(source, ":", path)

            if path is None:
                continue

            # if len(path) == 0:
            #     return [sourceChildEdge]

            if len(path) > maxPathLength:
                maxPath = path
                firstEdge = sourceChildEdge
                maxPathLength = len(path)

        if maxPathLength == -1:
            return None

        # firstSink = maxPath[0].source
        # firstEdge = None
        # for edge in self.adj[source]:
        #     if (not edge.reverse) and edge.source == source and edge.sink == firstSink:
        #         firstEdge = edge

        return [firstEdge] + maxPath

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))
