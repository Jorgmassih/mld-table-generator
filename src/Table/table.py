from MLD.mld import MLD, Complete, Incomplete

class MLDTable:
  def __init__(self, mld:MLD):
    self.mld = mld
    self.probs = mld.calc_prob()
    self.rows, self.columns = (len(mld.code_rx) + 1, len(mld.code_tx)+1)

  def gen_table(self, data):
    for i, d in enumerate(data):
      line = '|'.join(str(x).ljust(12) for x in d)
      print(line)
      if i == 0:
          print('-' * len(line))


  def probs_table(self):
    header = ['rx/tx'] + self.mld.code_tx.code_set
    jump_point = len(self.mld.code_tx)
    starter_point = 0
    ending_point = jump_point
    rows = []
    
    for e in self.mld.code_rx:
      rows += [[e] + self.probs[starter_point:ending_point]]
      starter_point += jump_point
      ending_point+=jump_point
    
    data = [header] + rows
    self.gen_table(data)


      

  def complete_table(self):
    header = ['rx/tx'] + self.mld.code_tx.code_set
    jump_point = len(self.mld.code_tx)
    starter_point = 0
    ending_point = jump_point
    rows = []
    
    determination_by_prob = self.mld.determinate_by_probs()
    for e in self.mld.code_rx:
      rows += [[e] + determination_by_prob[starter_point:ending_point]]
      starter_point += jump_point
      ending_point+=jump_point

    data = [header] + rows
    self.gen_table(data)

  def incomplete_table(self):
    header = ['rx/tx'] + self.mld.code_tx.code_set + ['Retransmission']
    jump_point = len(self.mld.code_tx)
    starter_point = 0
    ending_point = jump_point
    rows = []

    determination_by_prob = self.mld.determinate_by_probs()
    for e,r in zip(self.mld.code_rx, determination_by_prob[1]):
      rows += [[e] + determination_by_prob[0][starter_point:ending_point] + [r]]
      starter_point += jump_point
      ending_point+=jump_point

    data = [header] + rows
    self.gen_table(data)


