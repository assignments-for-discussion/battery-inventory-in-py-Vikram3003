def count_batteries_by_usage(cycles):
    
    lowCount = 0
    mediumCount = 0
    highCount = 0
    
    for i in range(len(cycles)):
        if cycles[i] < 400:
            lowCount += 1
        elif cycles[i] >= 400 and cycles[i] <= 919:
            mediumCount += 1
        else:
            highCount += 1
            
            
    return [lowCount, mediumCount, highCount]
 


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  
  
  
  try:
      print(counts)
      assert(counts[0] == 2)
      assert(counts[1] == 3)
      assert(counts[2] == 1)
      print("Done counting :)")
      
  except AssertionError as msg:
        print(msg)
  


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
