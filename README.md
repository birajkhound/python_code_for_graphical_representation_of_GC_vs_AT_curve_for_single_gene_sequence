# python_code_for_graphical_representation_of_GC_vs_AT_curve_for_single_gene_sequence
In bioinformatics, GC skew and AT skew are graphical representations of the nucleotide composition bias in a DNA sequence. They are used to analyze and visualize variations in the distribution of guanine-cytosine (GC) and adenine-thymine (AT) base pairs along a DNA molecule. These skew graphs can provide insights into various genomic features and processes.

1. **GC Skew**:
   - GC skew measures the relative abundance of guanine (G) and cytosine (C) nucleotides on the leading and lagging strands of a DNA sequence.
   - It is calculated using the formula: GC skew = (G - C) / (G + C)
   - A positive GC skew indicates that there is an excess of guanine over cytosine on the leading strand, which is the template strand for DNA replication.
   - A negative GC skew indicates that there is an excess of cytosine over guanine on the leading strand.
   - GC skew can help identify the origin of replication in bacterial genomes and the direction of replication forks.

2. **AT Skew**:
   - AT skew measures the relative abundance of adenine (A) and thymine (T) nucleotides on the leading and lagging strands.
   - It is calculated using the formula: AT skew = (A - T) / (A + T)
   - A positive AT skew indicates that there is an excess of adenine over thymine on the leading strand.
   - A negative AT skew indicates that there is an excess of thymine over adenine on the leading strand.
   - AT skew can also be used to predict the location of the replication origin and direction.

To create GC skew and AT skew graphs, you would typically follow these steps:

1. Load or obtain the DNA sequence of interest.
2. Calculate the GC skew and AT skew values along the sequence using sliding windows.
3. Plot the GC skew and AT skew values as functions of the genomic position (nucleotide position).
   
To generate GC vs AT curve using this Python program you just need to  
-Run this code on any Python IDE  
-insert the name of the sequence file as input(the program and the sequence file should be in the same directory)    
-this program deals with files that contain only one gene sequence. 
