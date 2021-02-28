# -=- String Methods -=- 

text = 'Today is tomorrow, And tomorrow is today'

# Count

print('Count = ', text.count('i'))

# Find

print('Find = ', text.find('i'))

# Lower

print('Lower = ', text.lower())

# Upper 

print('Upper = ', text.upper())

# Swapcase

print('Swapcase = ', text.swapcase())

# Title

print('Title = ', text.title())

# Strip

print('Strip = ', text.strip())

# Split and Join

text_list = text.split(' ')
print('Split = ', text_list)
print('Join = ', '_'.join(text_list))

# Replace

print('Replace = ', text.replace('Today', 'Yesterday'))

# Startswith

print('Startswith = ', text.startswith('Today')) # == True
print('Startswith = ', text.startswith('Tomorrow')) # == False

# Endswith

print('Endswith = ', text.endswith('today')) # == True
print('Endswith = ', text.endswith('tomorrow')) # == False 

# Isalpha

print('Isalpha = ', text.isalpha()) # == False

# Isdigit

print('Isdigit = ', text.isdigit()) # == False

# isalnum

print('Isalnum = ', text.isalnum()) # == False
