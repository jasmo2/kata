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
            arr = self.sequence(seq)
            min_num = int(min(seq.split(',')))
            arr.extend([min_num])
            return arr

    def max_el(self,seq):
        if seq == "":
            return [0, 0, 0]
        else:
            arr = self.min_el(seq)
            max_num = int(max(seq.split(',')))
            arr.extend([max_num])
            return max_num
