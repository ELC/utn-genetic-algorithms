"""Chromosome Class"""

class Chromosome():
    """Chromosome class"""
    def __init__(self, genes=None):
        """Creates a new chromosome"""
        self.genes = genes
        if genes is None:
            number_of_bits = Settings.get_chromosome_bits("exercise2")
            self.genes = util.get_random_number_string(number_of_bits, binary=True)
            self.validate()
        self.fitness = None

    def validate(self):
        while True:
            if self.get_target() != 0:
                return
            list_genes = list(self.genes)
            list_ones = [i for i,j in enumerate(list_genes) if j=="1"]
            if len(list_ones) == 0:
                break
            remove_index = list_ones[util.get_random_number(0, len(list_ones)-1)]
            list_genes[remove_index] = "0"
            self.genes = "".join(list_genes)


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
    from exercise2.logic.target import target as target_function
    import base.util.util as util
