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
        dec_gene = Util.get_random_number(0, maximum)
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
        index = self.__pick_random_gene()
        if inverse:
            mutated_genes = self.inverse_gene(index)
        else:
            mutated_genes = func()
        self.set_genes_string(mutated_genes)

    def inverse_gene(self, index):
        genes = list(self.genes)
        gene = genes[index]
        if gene == "1":
                genes[index] = "0"
        else:
            genes[index] = "1"
        genes = "".join(genes)
        return genes
    
    def set_genes_string(self, genes_string):
        self.genes = genes_string

    def __pick_random_gene(self):
        index = Util.get_random_number(0, self.amount_genes -1)
        return index

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

if __name__ != "__main__":
    from settings import Settings
    from util import Util
