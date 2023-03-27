import treeswift as ts
from Bio import SeqIO
import argparse
from random import sample

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tree", help="Input tree file", required=True)
    parser.add_argument("-a", "--align", help="Input alignment file", required=True)
    parser.add_argument("-p", "--perc", help="Percentage of leaves to delete", required=True, type=float)
    args = parser.parse_args()
    tree = ts.read_tree_newick(args.tree)
    taxa = [l.label for l in tree.traverse_leaves()]
    n = int(len(taxa) * args.perc)
    taxa_to_delete = sample(taxa, n)
    exclude_set = set(taxa_to_delete)
    tree.extract_tree_without(taxa_to_delete).write_tree_newick(args.tree + ".random" + str(args.perc) + ".tre")
    SeqIO.write((s for s in SeqIO.parse(args.align, "phylip-relaxed") if s.id not in exclude_set), args.align + ".random" + str(args.perc) + ".phylip", "phylip")