def count_battries_by_usage(cycles):    
  count = {
    "lowCount":0,
    "mediumCount":0,
    "highCount"
  }
for i in cycles:
 if i<=400:
  count["lowCount"] = count["lowCount"] +1
 elif i >400 and i <=919 :
  count["mediumCount"] = count["mediumCount"] + 1
 else:
  count["highCount"] = count["highCount"] + 1
return count
