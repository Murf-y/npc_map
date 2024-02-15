class NPC_Problem:
    def __init__(self, name, descirption):
        self.name = name
        self.descirption = descirption


class Reduction:
    def __init__(self, source: NPC_Problem, target: NPC_Problem, description: str = None):
        self.source = source
        self.target = target
        self.description = description


PROBLEMS = {}

PROBLEMS["SAT"] = NPC_Problem(
    "SAT", "Given a boolean formula, is there a satisfying assignment?")

PROBLEMS["3SAT"] = NPC_Problem(
    "3SAT", "Given a boolean formula in 3-CNF, is there a satisfying assignment?")

PROBLEMS["CLIQUE"] = NPC_Problem(
    "CLIQUE", "Given a graph and a number k, is there a clique (all vert are adj) >= k")

PROBLEMS["VC"] = NPC_Problem(
    "VC", "Given a graph and a number k, is there a vertex cover (touch all edges) <= k")

PROBLEMS["IS"] = NPC_Problem(
    "IS", "Given a graph and a number k, is there an independent set (no vertex is adj) >= k")

PROBLEMS["DS"] = NPC_Problem(
    "DS", "Given a graph and a number k, is there a dominating set (touch all vert by including it or an adj vert) <= k")

PROBLEMS["3COL"] = NPC_Problem(
    "3COL", "Given a graph, can it be colored with 3 colors (no adj vert have same color)?")

PROBLEMS["7COL"] = NPC_Problem(
    "7COL", "Given a graph, can it be colored with 7 colors (no adj vert have same color)?")

PROBLEMS["HC"] = NPC_Problem(
    "HC", "Given a graph, is there a tour?")

PROBLEMS["DHC"] = NPC_Problem(
    "DHC", "Given a directed graph, is there a tour?")

PROBLEMS["TSP"] = NPC_Problem(
    "TSP", "Given a graph and a number k, is there a tour of length <= k?")

PROBLEMS["HP"] = NPC_Problem(
    "HP", "Given a graph, is there a PATH that visits every vertex exactly once?")

PROBLEMS["EDGECOVER"] = NPC_Problem(
    "EDGE COVER", "Given a graph and k, does there exists a set of edges such that every vertex of the graph is incident to at least one edge of the set, with size <= k")

PROBLEMS["SC"] = NPC_Problem(
    "SC", "Given a set S and subsets S1, .. Sn and number k, can we find at maximum k sets of the subsets s.t. their union is S")

PROBLEMS["SETSPLITTING"] = NPC_Problem(
    "SET SPLITTING", "Given a Set S, and collection C of subsets of S. Can we partition S into s1, s2 s.t. no element in C is entirely in s1 or s2")

PROBLEMS["SETPACKING"] = NPC_Problem(
    "SET PACKING", "Given a Set S, and subsets S1, .. Sn and number k, does there exists at least k subsets s.t. no two subsets have common elements (intersection zero)")

PROBLEMS["SUBSETSUM"] = NPC_Problem(
    "SUBSET SUM", "Given a set of positive integers and a number k, does there exists a subset of the set s.t. the sum of the subset is equal to k")

PROBLEMS["EXACTCOVER"] = NPC_Problem(
    "EXACT COVER", "Given Set X and set S of subsets of X s1, .. sn, does there exists a subset of S such that the union of the subsets is equal to X, and no two sets in the subsets have common elements")

PROBLEMS["KNAPSACK"] = NPC_Problem(
    "KNAPSACK", "Given a set of items, each with a weight and a value, a max capacity C, and a value target V, does there exists a subset of the items such that the total weight is <= C and the total value is >= V")

PROBLEMS["BINPACKING"] = NPC_Problem(
    "BIN PACKING", "Given a set of items S, each with a weight, a bin capacity C, and a number of bins k, can S be partitioned into k or fewer subsets such that the sum of the weights in each subset is <= C")

PROBLEMS["PARTITION"] = NPC_Problem(
    "PARTITION", "Given a set of integers, does there exists a partition of the set into two subsets such that the sum of the elements in the two subsets are equal")

PROBLEMS["SUBISO"] = NPC_Problem(
    "SUB ISO", "Given two graphs G1 and G2, does there exists a subgraph of G1 isomorphic to G2")


def get_reductions():
    reductions = []

    # =================================================================================================
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["3SAT"], description="""For each clause C in SAT, if it contains 1 variable X1, add 2 new variables Z1 and Z2 and create 4 clauses with all combination of Z1 and Z2 or X1.\n
                                If it contains 2 variables X1, X2, add 1 new variable Z1 and create 2 clauses X1 or X2 or Z1, X1 or X2 or not Z1.\n
                                If it contains 3 variables leave it as is.\n
                                If it contains n>=4 add n-2 variables, in first clause add Zi, in the subsequent clause add not Zi or X or Zi+1, ...., in the last clause add not Zn-2 or Xn-1 or Xn"""))
    reductions.append(Reduction(
        PROBLEMS["SAT"], PROBLEMS["CLIQUE"], description="For each clause, place every literal as a node, after placing all literals, go through each clause for each literal node connect it to all other literal node in OTHER clauses such that they are not the opposite literal. Set K to the number of clauses."))

    # =================================================================================================
    reductions.append(Reduction(
        PROBLEMS["3SAT"], PROBLEMS["CLIQUE"], description="Same as SAT to Clique"))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["3COL"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["VC"], description="For each clause create a triangle formed by its literals as nodes (clause gadget), for each VARIABLE add the literal and its negation (variable gadget) as nodes and connect them,\n go over each variable gadget and connect each literal to the same literal node in the clauses gadgets (crossing edges), set K = 2m + n"))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["IS"], description="3SAT -> VC -> IS OR 3SAT -> Clique -> IS i.e. For each clause create a triangle formed by its literals as nodes (clause gadget), for each VARIABLE add the literal and its negation (variable gadget) as nodes and connect them,\n go over each variable gadget and connect each literal to the same literal node in the clauses gadgets (crossing edges), set K = m + n"))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["SUBSETSUM"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["SETSPLITTING"]))
    reductions.append(Reduction(
        PROBLEMS["3SAT"], PROBLEMS["SETPACKING"], description="3SAT -> IS -> SETPACKING"))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["DS"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["HC"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["HP"]))

    # =================================================================================================
    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["IS"],
                      description="Complement the graph and set new K = old K, the clique will become IS"))
    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["VC"],
                      description="Complement the graph and set new K = V - old K"))
    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["SAT"], description="""
                                Variables: yi,r (true if node i is the rth node of the clique) for 1 ≤ i ≤ n, 1 ≤ r ≤ k.
                                Create the following clauses:
                                For each r, y(1,r) OR y(2,r) OR .. OR y(n,r) (some node is the rth node of the clique).
                                For each i,r<s not y(i,r) OR not y(i,s) (no node is both the rth and sth node of clique).
                                For each r ≠ s and i < j such that (i,j) is not and edge of G, add  not y(i,r) OR not y(i,s) (if theres no edge from i to j, then nodes i and j cannot both be in the clique).
                                """))

    # =================================================================================================
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["CLIQUE"],
                      description="Complement the graph and set new K = old K, the IS will become clique"))
    reductions.append(Reduction(
        PROBLEMS["IS"], PROBLEMS["VC"], description="The IS of size K will become VC of size V - K"))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["SETPACKING"],
                      description="S=E, for each vertex v in G, create a set Sv such that it contains all edges that are incident to v, set K = k, the sets of the IS verticies will be the solution of the set packing"))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["DS"]))

    # =================================================================================================
    reductions.append(
        Reduction(PROBLEMS["EXACTCOVER"], PROBLEMS["SETPACKING"]))
    reductions.append(
        Reduction(PROBLEMS["EXACTCOVER"], PROBLEMS["SC"]))
    # =================================================================================================
    reductions.append(
        Reduction(PROBLEMS["SUBSETSUM"], PROBLEMS["KNAPSACK"]))
    reductions.append(
        Reduction(PROBLEMS["SUBSETSUM"], PROBLEMS["PARTITION"]))
    reductions.append(
        Reduction(PROBLEMS["SUBSETSUM"], PROBLEMS["BINPACKING"]))
    # =================================================================================================

    reductions.append(
        Reduction(PROBLEMS["PARTITION"], PROBLEMS["SUBSETSUM"]))
    reductions.append(
        Reduction(PROBLEMS["PARTITION"], PROBLEMS["BINPACKING"]))
    # =================================================================================================

    reductions.append(Reduction(
        PROBLEMS["VC"], PROBLEMS["IS"], description="The VC of size K will become IS of size V - K"))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["CLIQUE"],
                      description="Complement the graph and set new K = V - old K"))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["SUBSETSUM"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["HC"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["HP"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["DS"]))
    reductions.append(Reduction(
        PROBLEMS["VC"], PROBLEMS["SC"], description="S=E, for each vertex v in G, create a set Sv such that it contains all edges that are incident to v, set K = k, the sets of the vertex cover verticies will be the solution of the set cover"))
    # =================================================================================================

    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["VC"]))
    # =================================================================================================

    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["7COL"],
                      description="Add 4 verticies connected to all nodes, this will ensure the graph is 7col iff it was 3 col"))
    reductions.append(Reduction(
        PROBLEMS["3COL"], PROBLEMS["CLIQUE"], description="3COL -> SAT -> CLIQUE"))
    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["SAT"], description="For each vertex u in G, create 3 variables Ru Gu Bu , each represents the color of the vertex u (if u is red <=> Ru = 1, else Ru = 0), for each vertex create clauses (Ru or Gu or Bu) and (not Ru or not Gu) and (not Ru or not Bu) and (not Gu or not Bu) this ensures that u has exactly 1 color, then for each edge (u, v) create clauses (not Ru or not Rv) and (not Gu or not Gv) and (not Bu or not Bv) this ensures that u and v have different colors"))
    reductions.append(Reduction(
        PROBLEMS["3COL"], PROBLEMS["IS"]))
    reductions.append(Reduction(
        PROBLEMS["3COL"], PROBLEMS["VC"]))
    # =================================================================================================

    reductions.append(Reduction(
        PROBLEMS["HC"], PROBLEMS["TSP"], description="For each edge in the graph set the weight to 1, add all missing edges with weight 2, set K = number of vertices"))
    reductions.append(Reduction(PROBLEMS["HC"], PROBLEMS["HP"]))
    reductions.append(
        Reduction(PROBLEMS["HC"], PROBLEMS["SUBISO"], description="""
                  Keep it as is. A Hamiltonian cycle in a graph is a cycle that includes every vertex, so if we ignore the other edges in the graph,\n
                  we can think of the Hamiltonian cycle as a subgraph of the original graph with the properties that it contains all the vertices,\n
                  only some of the edges, and those edges make a cycle. That is, a Hamiltonian cycle in an n-vertex is isomorphic to the graph Cycle-n.
                  """))
    # =================================================================================================

    reductions.append(Reduction(PROBLEMS["TSP"], PROBLEMS["HC"]))
    # =================================================================================================

    reductions.append(Reduction(PROBLEMS["HP"], PROBLEMS["HC"]))
    # =================================================================================================

    return reductions
