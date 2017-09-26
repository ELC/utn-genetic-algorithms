"""Chromosome Class"""

class Chromosome():
    """Chromosome class"""
    def __init__(self, genes=None):
        """Creates a new chromosome"""
        self.genes = genes
        if genes is None:
            number_of_bits = Settings.get_chromosome_bits("exercise3")
            self.genes = util.get_random_permutation(number_of_bits)
        self.fitness = None

    def mutate(self):
        """Mutate the genes string using inversion"""
        amount_of_genes = len(self.genes)
        index = util.get_random_number(0, amount_of_genes - 1)
        mutated_genes = self._swap(index)
        self._set_genes_string(mutated_genes)

    def _swap(self, index):
        """Given an index, change the value of the gene in that index"""
        genes = util.swap_elements_from_list(self.genes)
        return genes

    def _set_genes_string(self, genes_string):
        """Change the gene string of the chromosome"""
        self.genes = genes_string

    def fit(self, total):
        """Calc the fitness value of this chromosome."""
        self.fitness = self.get_target()  / total

    def get_gene_string(self):
        """Return the genes string."""
        return self.genes

    def get_target(self):
        """Return the target value of this chromosome."""
        gene_string = self.get_gene_string()
        return target_function(gene_string)

    def get_fitness(self):
        """Return the fitness value of this chromosome."""
        return self.fitness

if __name__ != "__main__":
    from base.logic.settings_manager import Settings
    from exercise3.logic.target import target as target_function
    import base.util.util as util
