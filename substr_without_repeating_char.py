from collections import defaultdict

def find_longest_substring(input_str):
   start = 0
   index_dict = defaultdict(int)
   length = 0
   for end, c in enumerate(input_str):
      if c in index_dict and index_dict[c] >= start:
         start = index_dict[c] + 1

      curr_length = end - start + 1
      length = max(length, curr_length)
      index_dict[c] = end
   
   return length

print(find_longest_substring("abcdbea"))