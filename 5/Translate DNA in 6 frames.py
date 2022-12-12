def translate_with_frame(dna, frames=[1,2,3,-1,-2,-3]):
    reverse = ''
    for char in dna:
        if char == 'T':
            reverse += 'A'
        elif char == 'A':
            reverse += 'T'
        elif char == 'C':
            reverse += 'G'
        elif char == 'G':
            reverse += 'C'
    rev = reverse[::-1]
    array = []
    for char in frames:
        if char == 1:
            array.append(' '.join(dna[i:i+3] for i in range(0, len(dna), 3)).split(' '))
        elif char == 2:
            array.append(' '.join(dna[1:][i:i+3] for i in range(0, len(dna), 3)).rstrip().split(' '))
        elif char == 3:
            array.append(' '.join(dna[2:][i:i+3] for i in range(0, len(dna), 3)).split(' '))
        elif char == -1:
            array.append(' '.join(rev[i:i+3] for i in range(0, len(rev), 3)).split(' '))
        elif char == -2:
            array.append(' '.join(rev[1:][i:i+3] for i in range(0, len(rev), 3)).split(' '))
        elif char == -3:
            array.append(' '.join(rev[2:][i:i+3] for i in range(0, len(rev), 3)).split(' '))
    return ["".join((codons[char] for char in x if len(char) == 3)) for x in array]