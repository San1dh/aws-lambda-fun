import csv

reader = csv.reader(open('languages.csv', 'r'))
d = {}
for row in reader:
  k, v = row
  # remove white spaces using .strip()
  v = v.strip()
  d[v] = k

# print(d)

print("{")
for key in d:
  # print(key)
  # print(f"{{'{key}' : '{d[key]}'}},")
  print(f"'{key}'  : '{d[key]}',")
print("}")
