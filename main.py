def count_batteries_by_usage(cycles):    
    count = {
        "lowCount":0,
        "mediumCount":0,
        "highCount":0
    }

    for i in cycles:
      if i<=400:
       count["lowCount"] = count["lowCount"] + 1 
      elif i >400 and i <=919 :
       count["mediumCount"] = count["mediumCount"] + 1
      else: count["highCount"] = count["highCount"] + 1
    
    return count

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  print(counts)
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")



test_bucketing_by_number_of_cycles()
