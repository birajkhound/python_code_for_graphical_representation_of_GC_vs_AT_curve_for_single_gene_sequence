  # importing matplot library 
import matplotlib.pyplot as plt

  # declaring two array to store Gc_skew and AT_skew values
Agc = []
Aat = []

  # declaring two variable to store cumilitive Gc_skew and cumilitive AT_skew values
Cgc = 0
Cat = 0

  # function to calculate total repeatatation of a specific character in a string
def count_letters(input_string , target_character):
    count = 0
    for char in input_string:
        if char.isalpha():
            if char == target_character:
                count += 1
    return count  
   
  # to take the text file addres as input
address  = str(input("enter the txt file address of the gene sequance :"))

  #calculation of GC_skew and AT_skew values
with open(address, 'r') as file:
    for line in file:    
        # to Skip header lines
        if not line.startswith(">"):
           Na = count_letters(line, 'a')
           Nt = count_letters(line, 't')
           Ng = count_letters(line, 'g')
           Nc = count_letters(line, 'c')
           Gc = (Ng-Nc)/(Ng+Nc)
           At = (Na-Nt)/(Na+Nt)
           Cgc = Cgc + Gc
           Cat = Cat + At
           Agc.append(Cgc)
           Aat.append(Cat)


  # Downsample the data (there are lots of data points so i am taking some average points so that graph look more clear)
downsample_factor = 2000  # Adjust this value as needed
Agc_downsampled = Agc[::downsample_factor]
Aat_downsampled = Aat[::downsample_factor]
  
  #AT_skew_and_GC_skew_graph
plt.plot(Agc_downsampled, marker='o', color = 'green')
plt.plot(Aat_downsampled, marker='o', color = 'red')
  # Add labels and title
plt.xlabel('Genomic position')
plt.ylabel('red is AT-skew, and green is GC-skew')
plt.title('AT_skew_and_GC_skew_graph')
  # display plot
plt.show()