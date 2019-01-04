"""Chromosome Class"""


class Chromosome():
    def __init__(self, genes=None):
        if genes is None:
            number_of_bits = Settings.get_chromosome_bits()
            genes = util.get_random_number_string(number_of_bits, binary=True)
        self.genes = genes
        self.probability = None

    def mutate(self):
        amount_of_genes = len(self.genes)        
        index = util.get_random_number(0, amount_of_genes - 1)

        genes = list(self.genes)
        gene = genes[index]
        genes[index] = "1" if gene == "0" else "0"
        
        self.genes = "".join(genes)

    def fit(self, total):
        self.probability = self.get_target() / total

    def get_target(self):
        gene_dec_value = util.bin_to_dec(self.genes)
        return target_function(gene_dec_value)

    def get_fitness(self):
        return self.probability


if __name__ != "__main__":
    from exercise1.logic.settings_manager import Settings
    from exercise1.logic.target import target as target_function
    import exercise1.util.util as util
