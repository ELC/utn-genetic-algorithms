"""Chromosome Class"""

class Chromosome():
    """Chromosome class"""
    def __init__(self, genes=None):
        if genes is None:
            number_of_bits = Settings.get_chromosome_bits()
            genes = util.get_random_number_string(number_of_bits, binary=True)
        self.genes = genes
        self.amount_genes = len(self.genes)
        self.target = target_function(self.get_gene_int())
        self.fitness = None

    def mutate(self, inverse=True, func=None):
        """Mutate the genes string"""
        index = util.get_random_number(0, self.amount_genes -1)
        if inverse:
            mutated_genes = self._inverse_gene(index)
        else:
            mutated_genes = func()
        self._set_genes_string(mutated_genes)

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
        """Calc the fitness value of this chromosome."""
        self.fitness = self.target / total

    def get_gene_int(self):
        """Return the genes in decimal format."""
        return int(self.genes, 2)

    def get_gene_string(self):
        """Return the genes string."""
        return self.genes

    def get_target(self):
        """Return the target value of this chromosome."""
        return self.target

    def get_fitness(self):
        """Return the fitness value of this chromosome."""
        return self.fitness

    def get_size(self):
        """Return the amout of genes of this chromosome."""
        return self.amount_genes

if __name__ != "__main__":
    from exercise1.logic.settings_manager import Settings
    from exercise1.logic.target import target as target_function
    import exercise1.util.util as util
