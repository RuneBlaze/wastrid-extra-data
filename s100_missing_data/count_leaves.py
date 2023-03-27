import treeswift as ts
ps = [0.2, 0.4, 0.6]
rs = range(1,51)

def read_tree_list(path):
    with open(path) as f:
        return [ts.read_tree_newick(line.strip()) for line in f]

column_p = []
column_taxa_deletion_rate = []
for p in ps:
    for r in rs:
        repname = f"{r:02d}"
        gtreepath = f"{repname}/g200.clade.p{p}.tre"
        gtrees = read_tree_list(gtreepath)
        for gtree in gtrees:
            ntaxa = sum(1 for _ in gtree.traverse_leaves())
            deletion_rate = (101 - ntaxa) / 101
            column_p.append(p)
            column_taxa_deletion_rate.append(deletion_rate)

import pandas as pd
df = pd.DataFrame({"p": column_p, "taxa_deletion_rate": column_taxa_deletion_rate})
print(df.groupby("p").mean())