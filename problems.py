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
    "CLIQUE", "Given a graph and a number k, is there a clique >= k")
PROBLEMS["VC"] = NPC_Problem(
    "VC", "Given a graph and a number k, is there a vertex cover (cover all edges) <= k")
PROBLEMS["IS"] = NPC_Problem(
    "IS", "Given a graph and a number k, is there an independent set (no vertex is adj) >= k")
PROBLEMS["DS"] = NPC_Problem(
    "DS", "Given a graph and a number k, is there a dominating set (cover all vert by including it or an adj vert) <= k")
PROBLEMS["SC"] = NPC_Problem(
    "SC", "Given a set S and subsets S1, .. Sn and number k, can we find at maximum k sets of the subsets s.t. their union is S")
PROBLEMS["3COL"] = NPC_Problem(
    "3COL", "Given a graph, can it be colored with 3 colors (no adj vert have same color)?")
PROBLEMS["7COL"] = NPC_Problem(
    "7COL", "Given a graph, can it be colored with 7 colors (no adj vert have same color)?")
PROBLEMS["HC"] = NPC_Problem(
    "HC", "Given a graph, is there a tour?")
PROBLEMS["TSP"] = NPC_Problem(
    "TSP", "Given a graph and a number k, is there a tour of length <= k?")
PROBLEMS["SS"] = NPC_Problem(
    "SS", "Given a Set S, and collection C of subsets of S. Can we partition S into s1, s2 s.t. no element in C is entirely in s1 or s2")


def get_reductions():
    reductions = []

    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["3SAT"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["SAT"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["CLIQUE"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["CLIQUE"]))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["IS"], PROBLEMS["DS"]))
    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["IS"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["DS"]))
    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["CLIQUE"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["CLIQUE"]))
    reductions.append(Reduction(PROBLEMS["VC"], PROBLEMS["SC"]))
    reductions.append(Reduction(PROBLEMS["SC"], PROBLEMS["VC"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["3COL"]))
    reductions.append(Reduction(PROBLEMS["3COL"], PROBLEMS["7COL"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["HC"]))
    reductions.append(Reduction(PROBLEMS["HC"], PROBLEMS["TSP"]))
    reductions.append(Reduction(PROBLEMS["TSP"], PROBLEMS["HC"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["SS"]))
    reductions.append(Reduction(PROBLEMS["SAT"], PROBLEMS["SC"]))
    reductions.append(Reduction(PROBLEMS["3SAT"], PROBLEMS["DS"]))
    reductions.append(Reduction(PROBLEMS["DS"], PROBLEMS["3SAT"]))

    return reductions
