Extra data for weighted ASTRID
==============================

## `s100_missing_data`

Contains 50 replicates, each with 200 gene trees from the S100[^1]
dataset (seqlen = 400).

The file names are named in the form of `g200.p{x}.tre`, where $x$
is the amount of taxa randomly sampled and removed for each gene tree
randomly. For example $x = 0.8$ means that 80% of the taxa each gene tree
are sampled and removed. The support values and branch lengths are reevaluated by IQ-TREE using the following command using aBayes support:

```bash
iqtree2 -nt 1 -m GTR+G -abayes -t $tree -s $alignment_with_taxa_removed
```

These data are provided for the purpose of reproducing the results. The ownership of the data belongs to the authors of the original paper.


[^1]: Zhang, C., Rabiee, M., Sayyari, E., Mirarab, S.: ASTRAL-III: polynomial time species tree reconstruction from
partially resolved gene trees. BMC Bioinformatics 19(6), 153 (2018).