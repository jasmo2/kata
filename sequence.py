class Sequence:
    def sequence(self, seq):
        if seq == "":
            return [0]
        else:
            seq_len = len(seq.split(','))
            return [seq_len]


    def min_el(self,seq):
        if seq == "":
            return [0, 0]
        else:
            seq_len = len(seq.split(','))
            arr = [seq_len]
            arr.extend(self.sequence(seq))
            return arr
