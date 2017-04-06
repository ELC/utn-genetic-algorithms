"""Individual Class"""

class Individual():
    """Individual class"""
    def __init__(self, genes=None):
        if genes is None:
            bits = Settings.individual_bits
            genes = self.__generate_gene_string(bits)
        self.genes = genes
        self.amount_genes = len(self.genes)
        self.target = None
        self.fitness = None

    def __generate_gene_string(self, length):
        maximum = 2 ** length - 1
        dec_gene = randint(0, maximum)
        bin_gene = Util.dec_bin(dec_gene)
        gene = self.__fill(bin_gene, length)
        return gene

    def __fill(self, raw, lenght, neutral="0"):
        raw_gene = list(raw)
        while len(raw_gene) < lenght:
            raw_gene.insert(0, neutral)
        filled_gene = "".join(raw_gene)
        return filled_gene

    def mutate(self, inverse=True, func=None):
        """Mutate the genes string"""
        gene = self.__pick_random_gene()
        if inverse:
            if gene == "1":
                gene = "0"
            else:
                gene = "1"
        else:
            gene = func(gene)

    def __pick_random_gene(self):
        index = randint(0, self.amount_genes -1)
        return self.genes[index]

    def fit(self, target, total):
        """Calc the fitness value of this individual."""
        usable_gene = self.get_gene()
        self.target = target(usable_gene)
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

if __name__ == "__main__":
    pass
else:
    from numpy.random import randint
    from settings import Settings
    from util import Util
