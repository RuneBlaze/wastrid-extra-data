Extra data for weighted ASTRID
==============================

## `s100_missing_data`

Contains 50 replicates, each with 200 gene trees from the S100[^1]
dataset (seqlen = 400). The species tree is also provided in
`s_tree.trees` to enable full reproduction of the results.

### Fixed number of taxa deleted

The file names are in the form of `g200.p{x}.tre`, where $x$
is the amount of taxa randomly sampled and removed for each gene tree
randomly. For example $x = 0.8$ means that 80% of the taxa each gene tree
are sampled and removed. The support values and branch lengths are reevaluated by IQ-TREE using the following command using aBayes support:

```bash
iqtree2 -nt 1 -m GTR+G -abayes -t $tree -s $alignment_with_taxa_removed
```

### Clade-based missing taxa

The file names are in the form of `g200.clade.p{x}.tre`,
where $x$ is the lower bound of a candidate clade in the species tree. For example $x = 0.2$ means that only clades that are above 20% in size in the species tree are candidates.


## Scripts

Scripts should be run from their respective directories as the working directory.

All scripts depend on TreeSwift. As such the scripts
are licensed as GPL-3.0. Additionally, they depend on BioPython and.

```
s100_missing_data/count_leaves.py # count the number of leaves in each clade-based gene tree
random_clade.py # generate clade-based missing data for gene trees
random_missing.py # generate fixed-number-of-taxa-missing gene trees
```

## Note

These data are provided for the purpose of reproducing the results. The ownership of the data belongs to the authors of the original paper.


[^1]: Zhang, C., Rabiee, M., Sayyari, E., Mirarab, S.: ASTRAL-III: polynomial time species tree reconstruction from
partially resolved gene trees. BMC Bioinformatics 19(6), 153 (2018).