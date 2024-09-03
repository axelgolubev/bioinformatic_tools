class Dna:
    '''DNA related manipulations and calculations'''

    def __init__(self, seq: str) -> None:
        self.seq = seq

    def reverse_complement(self) -> str:
        ''' Function take a sequence as an input and reverse complement the sequence
        '''
        low_sequence = self.seq.lower()
        rev_comlement = []
        for nt in low_sequence[::-1]:
            if nt == 'a':
                rev_comlement.append("t")
            elif nt == 't':
                rev_comlement.append("a")
            elif nt == 'g':
                rev_comlement.append("c")
            elif nt == 'c':
                rev_comlement.append("g")
            else:
                print('The sequence contains wrong nucleotides!')
                rev_comlement.append("X")
        return ''.join(rev_comlement)
    
    def transcription(self) -> str:
        '''Transcrive DNA to RNA - same chain non-reversed'''
        low_sequence = self.seq.lower()
        return low_sequence.replace("t", 'u')
