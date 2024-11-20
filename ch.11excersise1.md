Are Python tuples always hashable?

Yes, Python tuples are generally hashable, but there are some conditions to consider:

Conditions for Hashability
Immutable: Tuples are immutable, which means that their contents cannot be changed after they are created. This immutability is a key factor in their hashability.

Contain Hashable Elements: A tuple is hashable only if all of its elements are also hashable. For example, a tuple containing only immutable types (like integers, floats, strings, and other tuples) is hashable. However, if a tuple contains any mutable types (like lists or dictionaries), it will not be hashable.

Example
Hashable Tuple:

python
Copy code
t1 = (1, 2, 3)  # This tuple is hashable
print(hash(t1))  # Outputs a hash value
Non-Hashable Tuple:

python
Copy code
t2 = (1, 2, [3])  # This tuple is not hashable because it contains a list
try:
    print(hash(t2))  # This will raise a TypeError
except TypeError as e:
    print(e)  # Outputs: unhashable type: 'list'
Summary
Always Hashable: A tuple itself is hashable as long as all its elements are hashable.
Immutable Requirement: The immutability of tuples is what allows them to maintain a consistent hash value.
If you need to check whether a tuple is hashable, you can do so by trying to compute its hash and catching the potential TypeError.