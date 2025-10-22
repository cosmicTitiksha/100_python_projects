# The code is Acronym generator - e.g; Portable Document Format -> PDF

# capitalizing first letter of each word in a sentence.
line = input("Enter the line : ").title()
# line.split(" ") : only splits on space
# line.split() : splits by any sequence of whitespaces (spaces, tabs, newlines)
words = line.split()

acronym = ''
for each_w in words:
    # Adding first character of each word into the variable reference 'acronym'
    acronym += each_w[0]

print(acronym)