from itertools import product
import random
from Utils.utils import decimal_to_q_ary

class Code:
    def __init__(self, n:int, m:int, q=2, code_set:list=None):
        if m > q**n:
            raise ValueError('The "m" value is larger than all possible combiantions with "n" value')
        self.n_length = n
        self.m_size = m
        self.q_size = q
        self.alphabet = {str(i) for i in range(0, self.q_size)}
        
        if not code_set:
            self.code_set = []
        else:
            self.code_set = code_set

    def get_all_posibilities(self):
        possible_words = [decimal_to_q_ary(num=i, base=self.q_size, length=self.n_length) for i in range(0, self.q_size**self.n_length)]
        
        n_ = self.n_length
        m_ =  self.q_size**n_
        return Code(n=n_, m=m_, q=self.q_size, code_set=possible_words)

    def __getitem__(self, item:int):
        return self.code_set[item]

    def __len__(self):
        return self.m_size

    def __repr__(self):
        return str(self.code_set)

    def __str__(self):
        return str(self.code_set)

    def add_codeword(self, codeword:str):
        if len(codeword) == self.n_length:
            self.code_set += [codeword]
            return True
        else:
            print('Invalid codeword, the length of this codeword is larger than n')
            return False

    def remove_codeword(self, codeword:str):
        for e in self.code_set:
            if e == codeword:
                self.code_set.remove(e)
                return True
        
        print('Invalid codeword, this codeword do not belong to this alphabet')
        return False


    def randomly_fill_set(self):
        self.code_set = []
        while len(self.code_set) < self.m_size:    
            self.code_set += [''.join([random.choice(list(self.alphabet)) for i in range(0, self.n_length)])]
            