l = ['a', 'b', 'c']

l.append('d')
print(l) # Output = ['a', 'b', 'c', 'd']

l2 = ['e', 'f']
l.extend(l2)
print(l) # Output = ['a', 'b', 'c', 'd', 'e', 'f'] , Note: we added "d" with "append" method

l.insert(6, 'g') # 6 = index, g = string
print(l) # Output = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# ----------------------------------

ln = [(0, 0), (0, 1), (1, 1)]

ln.sort(key=lambda x: (x[0] + x[1]), reverse=True)
print(ln)
