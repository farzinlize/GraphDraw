class Graph:

    '''
    initial graph interface class with 4 differente modes:
        (1) empty       -> just a empty class without any data
        (2) matrix      -> inital with a adjacency matrix 
            inital_var: 2D n*n array (n = graph nodes count)
        (3) adj-list    -> inital with a adjacency list
            initial_var: list containing lists of neighbours for any node
        (4) obj-list    -> import list of objects from pre-defined classess
            initial_var|: a list of object (this list could contain only one object that hold all data)
    '''
    def __init__(self, mode='empty', initial_var=None):
        self.empty = False
        self.has_matrix = False
        self.matrix = None
        self.has_adj_list = False
        self.adj_list = None
        self.has_obj_list = False
        self.obj_list = None

        if mode == 'empty':
            self.empty = True
        elif mode == 'matrix':
            self.has_matrix = True
            self.matrix = initial_var
        elif mode == 'adj-list':
            self.has_adj_list = True
            self.adj_list = initial_var
        elif mode == 'obj-list':
            self.has_obj_list = True
            self.obj_list = initial_var


    def make_matrix(self):
        pass


    def get_matrix(self):
        if not self.empty:
            if self.has_matrix:
                return self.matrix
            return self.make_matrix()


    '''
    read a matrix from file
        (WARNING) omit previous data
    '''
    def read_save_matrix(self, filename):
        with open(filename, 'r') as graph:
            node_count = int(graph.readline())
            self.matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]
            for line in graph:
                edge_nodes = [int(node_code) for node_code in line.split()]
                self.matrix[edge_nodes[0]][edge_nodes[1]] = 1


def test_main():
    interface = Graph()
    interface.read_save_matrix('g.graph')
    
    for l in interface.matrix:
        print(l)


test_main()