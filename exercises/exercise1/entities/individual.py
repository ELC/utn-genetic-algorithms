"""Individual Class"""

class Individual():
    """Individual class"""
    def __init__(self, genes=None):
        if genes is None:
            bits = Settings.get_individual_bits()
            genes = self._generate_gene_string(bits)
        self.genes = genes
        self.amount_genes = len(self.genes)
        self._gene_int = self.get_gene()
        self.target = target_function(self._gene_int)
        self.fitness = None

    def _generate_gene_string(self, length):
        maximum = 2 ** length - 1
        dec_gene = util.get_random_number(0, maximum)
        bin_gene = util.dec_bin(dec_gene)
        gene = self._fill(bin_gene, length)
        return gene

    def _fill(self, raw, lenght, neutral="0"):
        raw_gene = list(raw)
        while len(raw_gene) < lenght:
            raw_gene.insert(0, neutral)
        filled_gene = "".join(raw_gene)
        return filled_gene

    def mutate(self, inverse=True, func=None):
        """Mutate the genes string"""
        index = self._pick_random_gene()
        if inverse:
            mutated_genes = self._inverse_gene(index)
        else:
            mutated_genes = func()
        self._set_genes_string(mutated_genes)

    def _pick_random_gene(self):
        index = util.get_random_number(0, self.amount_genes -1)
        return index

    def _inverse_gene(self, index):
        genes = list(self.genes)
        gene = genes[index]
        if gene == "1":
            genes[index] = "0"
        else:
            genes[index] = "1"
        genes = "".join(genes)
        return genes

    def _set_genes_string(self, genes_string):
        self.genes = genes_string

    def fit(self, total):
        """Calc the fitness value of this individual."""
        self.fitness = self.target / total

    def get_gene(self):
        """Return the genes in decimal format."""
        return int(self.genes, 2)

    def get_gene_string(self):
        """Return the genes string."""
        return self.genes

    def get_target(self):
        """Return the target value of this individual."""
        return self.target

    def get_fitness(self):
        """Return the fitness value of this individual."""
        return self.fitness

    def get_size(self):
        """Return the amout of genes of this individual."""
        return self.amount_genes

if __name__ != "__main__":
    from exercise1.logic.settings import Settings
    from exercise1.logic.target import target as target_function
    import exercise1.util.util as util
