import treeswift as ts
from Bio import SeqIO
import argparse
from random import sample

def clades_above_certain_size(tree, size_lb):
    clades = set()
    for node in tree.traverse_postorder():
        if node.is_leaf():
            node.clade = frozenset([node.label])
        else:
            node.clade = frozenset.union(*[c.clade for c in node.children])
        clades.add(node.clade)
    return [c for c in clades if len(c) >= size_lb]

NUMGENES = 400

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--replicate", help="Replicate number", required=True, type=int)
    parser.add_argument("-p", "--perc", help="Percentage of leaves to delete", required=True, type=float)
    args = parser.parse_args()
    repname = f"{args.replicate:02d}"
    stree = ts.read_tree_newick(f"{repname}/s_tree.trees")
    taxa = set([l.label for l in stree.traverse_leaves()])
    numspecies = 101
    permitted_clades = list(clades_above_certain_size(stree, args.perc * numspecies))
    for i in range(600):
        gtree_name = f"{repname}/gtrees_400.tre.l{i}"
        gtree = ts.read_tree_newick(gtree_name)
        alnpath = f"{repname}/bestMLestimatedgenetree_400/all-genes_400.phylip.{i}.phylip"
        allowlist = sample(permitted_clades, 1).pop()
        exclude_list = list(taxa - allowlist)
        exclude_set = set(exclude_list)
        gtree.extract_tree_without(exclude_list).write_tree_newick(gtree_name + ".clade" + str(args.perc) + ".tre")
        SeqIO.write((s for s in SeqIO.parse(alnpath, "phylip-relaxed") if s.id not in exclude_set), alnpath + ".clade" + str(args.perc) + ".phylip", "phylip")