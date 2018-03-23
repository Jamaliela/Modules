######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: A6: It's in your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence: a DNA sequence
    :return: A boolean value indicating if the sequence is valid
    """
    valid_string = ["A", "C", "G", "T"]
    for letter in sequence:
        if letter not in valid_string:
            return False
    return True


def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence: A DNA sequence
    :return: the complement string for the DNA sequence
    """

    complement = ""         # This can be used to "build" the complement

    letter_dictionary = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for letter in sequence:
        if letter in letter_dictionary:
            complement += letter_dictionary[letter]
        else:
            return "Sequencing Error"

    return complement


def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence: the DNA sequence
    :return: The same sequence with T's replaced by U's
    """

    mrna = ""

    for letter in sequence:
        if letter == "T":
            mrna += "U"
        else:
            mrna += letter

    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence: the DNA sequence
    :return: A list where each element is a set of three DNA values
    """

    list_of_chunks = []

    for i in range(len(sequence)//3):
        list_of_chunks.append(sequence[i*3:i*3+3])

    return list_of_chunks


def amino_acid_chunks(threecharseq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character AminoAcid

    :param threecharseq: a sequence of three characters
    :return: A string representing the animo acid chunk for that sequence
    """

    ###################################################################
    #  This function was already completed correctly! No changes needed!
    ###################################################################

    # We haven't learned about dictionaries yet, but here is one for the extra curious.
    # You aren't expected to know what this is yet.
    translator = { "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                        "AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                        "GAC":"D", "GAU":"D",
                        "AAC":"N", "AAU":"N",
                        "UGC":"C", "UGU":"C",
                        "GAA":"E", "GAG":"E",
                        "CAA":"Q", "CAG":"Q",
                        "GGA":"G", "GGC":"G", "GGU":"G", "GGG":"G",
                        "CAC":"H", "CAU":"H",
                        "AUA":"I", "AUC":"I", "AUU":"I",
                        "UUA":"L", "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                        "AAA":"K", "AAG":"K",
                        "AUG":"M",
                        "UUC":"F", "UUU":"F",
                        "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                        "AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                        "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                        "UGG":"W",
                        "UAC":"Y", "UAU":"Y",
                        "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                        "UAA":"*", "UAG":"*", "UGA":"*" }

    if threecharseq in translator.keys():
        return translator[threecharseq]     # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a a sequence of nucleotides:
    A, C, G, and T and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    ###################################################################
    #  This function was already completed correctly! No changes needed!
    ###################################################################

    aaseq = ""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + amino_acid_chunks(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function call which prints the resulting amino acid sequence given a DNA sequence

    :return: None
    """
    sequence = input("Please enter a valid gene sequence to convert to an amino acid: \n")
    print("The input sequence {0} produces the amino acid {1}".format(sequence, sequence_gene(sequence)))         # Uncomment this line to use the function directly
    # Notice the missing call to the test suite?!!?


if __name__ == "__main__":
    main()
