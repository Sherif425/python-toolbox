"""
    Using * and zip to 'unzip'
    You know how to use zip() as well as how to print out values from a zip object. Excellent!

    Let's play around with zip() a little more. There is no unzip function for doing the reverse of what zip() does. We can, however, reverse what has been zipped together by using zip() with a little help from *! * unpacks an iterable such as a list or a tuple into positional arguments in a function call.

    In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().

    Two tuples of strings, mutants and powers have been pre-loaded.

"""
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

powers = ['telepathy',
          'thermokinesis',
          'teleportation',
          'magnetokinesis',
          'intangibility']


# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# print(list(z1))

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# print(result1)
# print(result2)

# Check if unpacked tuples are equivalent to original tuples
print(list(result1) == mutants)
print(list(result2) == powers)
