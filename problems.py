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
    "SUBSET SUM", "Given a set of integers and a number k, does there exists a subset of the set s.t. the sum of the subset is equal to k")

PROBLEMS["EXACTCOVER"] = NPC_Problem(
    "EXACT COVER", "Given set S of sets s1, .. sn, and set X, does there exists a subset of S such that the union of the subset is equal to X, and no two sets in the subset have common elements")

PROBLEMS["KNAPSACK"] = NPC_Problem(
    "KNAPSACK", "Given a set of items, each with a weight and a value, a max capacity C, and a value target V, does there exists a subset of the items such that the total weight is <= C and the total value is >= V")

PROBLEMS["BINPACKING"] = NPC_Problem(
    "BIN PACKING", "Given a set of items S, each with a weight, a bin capacity C, and a number of bins k, can S be partitioned into k or fewer subsets such that the sum of the weights in each subset is <= C")

PROBLEMS["PARTITION"] = NPC_Problem(
    "PARTITION", "Given a set of integers, does there exists a partition of the set into two subsets such that the sum of the elements in the two subsets are equal")


def get_reductions():
    reductions = []

    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["3SAT"]))
    reductions.append(Reduction(
        PROBLEMS["SAT"], PROBLEMS["CLIQUE"], description="For each clause, place every literal as a node, after placing all literals, go through each clause for each literal node connect it to all other literal node in OTHER clauses such that they are not the opposite literal. Set K to the number of clauses."))

    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["CLIQUE"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["3COL"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["SUBSETSUM"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["SETSPLITTING"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["DS"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["HC"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["HP"]))

    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["IS"],
                      description="Complement the graph and set new K = old K, the clique will become IS"))
    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["VC"]))

    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["CLIQUE"],
                      description="Complement the graph and set new K = old K, the IS will become clique"))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["SETPACKING"]))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["DS"]))

    reductions.append(
        Reduction(PROBLEMS["EXACTCOVER"], PROBLEMS["SETPACKING"]))
    reductions.append(
        Reduction(PROBLEMS["EXACTCOVER"], PROBLEMS["SC"]))

    reductions.append(
        Reduction(PROBLEMS["SUBSETSUM"], PROBLEMS["KNAPSACK"]))
    reductions.append(
        Reduction(PROBLEMS["SUBSETSUM"], PROBLEMS["PARTITION"]))
    reductions.append(
        Reduction(PROBLEMS["SUBSETSUM"], PROBLEMS["BINPACKING"]))

    reductions.append(
        Reduction(PROBLEMS["PARTITION"], PROBLEMS["SUBSETSUM"]))
    reductions.append(
        Reduction(PROBLEMS["PARTITION"], PROBLEMS["BINPACKING"]))

    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["CLIQUE"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["SUBSETSUM"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["HC"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["HP"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["DS"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["SC"]))

    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["VC"]))

    reductions.append(Reduction(PROBLEMS["SC"], PROBLEMS["VC"]))

    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["7COL"]))
    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["CLIQUE"]))
    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["SAT"]))
    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["IS"]))

    reductions.append(Reduction(PROBLEMS["HC"], PROBLEMS["TSP"]))
    reductions.append(Reduction(PROBLEMS["HC"], PROBLEMS["HP"]))

    reductions.append(Reduction(PROBLEMS["TSP"], PROBLEMS["HC"]))

    reductions.append(Reduction(PROBLEMS["HP"], PROBLEMS["HC"]))

    return reductions
