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
        return self.target_function(gene_dec_value)

    def get_fitness(self):
        return self.probability

    @staticmethod
    def target_function(number):
        exp = Settings.get_chromosome_bits()
        coef = (2 ** exp) - 1
        return (number / coef) ** 2


if __name__ != "__main__":
    from oop.data.filemanager import FileManager as Settings
    import oop.util.util as util
