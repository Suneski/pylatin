pyg = 'ay' #adds 'ay' at the end

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower() #makes word lowercase
    first = word[0] #determines first letter
    new_word = word[1:len(word)] + first + pyg
    print new_word
else:
    print 'empty'
