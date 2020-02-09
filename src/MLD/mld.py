from itertools import product
from Utils.utils import find_max_idxs
from random import choice


class MLD:
    def __init__(self, codes: tuple, probs: list):
        self.code_tx, self.code_rx = codes
        self.alph = self.code_tx.alphabet
        self.probs = probs
        self.mld_probs = []

    def calc_prob(self):
        probs = []
        for codeword_rx in self.code_rx:
            for codeword_tx in self.code_tx:
                prob_accum=1.0
                for i in range(self.code_tx.n_length):
                    if codeword_tx[i] == codeword_rx[i]:
                        prob_accum*=self.probs[int(codeword_tx[i])]
                    else:
                        prob_accum*=(1 - self.probs[int(codeword_tx[i])])
                probs +=[round(prob_accum, 3)]

        return probs
    


class Complete(MLD):
    def __init__(self, codes: tuple, probs: list):
        MLD.__init__(self, codes, probs)
    
    def determinate_by_probs(self):
        probs = super().calc_prob()
        selection = ['-' for i in range(0, len(probs))]

        code_tx_len = len(self.code_tx)
        for i in range(0, len(probs), code_tx_len):
            slice_list = probs[i: i +  code_tx_len]
            max_probs_idx = find_max_idxs(slice_list)
            arbitrary_choice = choice(max_probs_idx)
            selection[i + arbitrary_choice] = 'x'
        
        return selection
        



class Incomplete(MLD):
    def __init__(self, codes: tuple, probs: list):
        MLD.__init__(self, codes, probs)

    def determinate_by_probs(self):
        probs = super().calc_prob()
        selection = ['-' for i in range(0, len(probs))]
        retransmission = []
        code_tx_len = len(self.code_tx)
        for i in range(0, len(probs), code_tx_len):
            slice_list = probs[i: i +  code_tx_len]
            max_probs_idx = find_max_idxs(slice_list)
            if(len(max_probs_idx) > 1):
                retransmission += [True]
            else:
                retransmission += [False]
            
            for e in max_probs_idx:
                selection[i + e] = 'x'


        
        return [selection, retransmission]