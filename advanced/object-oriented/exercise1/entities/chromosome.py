"""Chromosome Class"""


class Chromosome():
    """Chromosome class"""

    def __init__(self, genes=None):
        """Creates a new chromosome"""
        if genes is None:
            number_of_bits = Settings.get_chromosome_bits()
            genes = util.get_random_number_string(number_of_bits, binary=True)
        self.genes = genes
        self.fitness = None

    def mutate(self):
        """Mutate the genes string using inversion"""
        amount_of_genes = len(self.genes)
        index = util.get_random_number(0, amount_of_genes - 1)
        mutated_genes = self._inverse_gene(index)
        self._set_genes_string(mutated_genes)

    def _inverse_gene(self, index):
        """Given an index, change the value of the gene in that index"""
        genes = list(self.genes)
        gene = genes[index]
        genes[index] = "1" if gene == "0" else "0"
        genes = "".join(genes)
        return genes

    def _set_genes_string(self, genes_string):
        """Change the gene string of the chromosome"""
        self.genes = genes_string

    def fit(self, total):
        """Calc the fitness value of this chromosome."""
        self.fitness = self.get_target() / total

    def get_gene_string(self):
        """Return the genes string."""
        return self.genes

    def get_target(self):
        """Return the target value of this chromosome."""
        gene_string = self.get_gene_string()
        gene_dec_value = util.bin_to_dec(gene_string)
        return target_function(gene_dec_value)

    def get_fitness(self):
        """Return the fitness value of this chromosome."""
        return self.fitness


if __name__ != "__main__":
    from exercise1.logic.settings_manager import Settings
    from exercise1.logic.target import target as target_function
    import exercise1.util.util as util
