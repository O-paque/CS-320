# simple Bloom filter using binary strings


BLOOMSIZE = 32  # bits = 4 octets
bloom_filter = bytearray(b'\x00\x00\x00\x00')
NUMHASHES = 5  # hash five times
PRIME1 = 37
PRIME2 = 101


# multi-hash function
def m_hash(k, i):
    assert (k is not None)
    b_str = k.encode()
    b_val = 0
    for j in range(0, len(b_str)):
        b_val = ((b_val * 256) + b_str[j])

    p1 = b_val % PRIME1
    p2 = i * (b_val % PRIME2)
    return ((p1 + p2) % BLOOMSIZE)


# add to bloom filter
def add(str):
    if (str is None):
        return
    for i in range(0, NUMHASHES):
        hash_val = m_hash(str, i)
        hash8 = int(hash_val/8)
        bloom_filter[hash8] = bloom_filter[hash8] | (1 << (hash_val % 8))


# is str likely present in bloom filter?
def member(str):
    if (str is None):
        return False

    for i in range(0, NUMHASHES):
        hash_val = m_hash(str, i)
        hash8 = int(hash_val/8)
        bit_set = bloom_filter[hash8] & (1 << (hash_val % 8))
        if (bit_set == 0):
            return False

    return True


# print bloom filter
def print_bloom():
    for i in range(0, BLOOMSIZE):
        i8 = int(i/8)
        if ((bloom_filter[i8] & (1 << (i % 8))) != 0):
            print("1", end="")
        else:
            print("0", end="")
    print("")


print_bloom()

for i in range(0, NUMHASHES):
    h = m_hash("orange", i)
    print(f"m_hash(orange, {i}) = {h}")
for i in range(0, NUMHASHES):
    h = m_hash("apple", i)
    print(f"m_hash(apple, {i}) = {h}")
for i in range(0, NUMHASHES):
    h = m_hash("banana", i)
    print(f"m_hash(banana, {i}) = {h}")
for i in range(0, NUMHASHES):
    h = m_hash("grapes", i)
    print(f"m_hash(grapes, {i}) = {h}")


add("orange")
add("apple")
add("banana")
add("grapes")

print_bloom()

if (member("banana")):
    print("banana in set")
else:
    print("banana not in set")
if (member("avocado")):
    print("avocado in set")
else:
    print("avocado not in set")
if (member("lettuce")):
    print("lettuce in set")
else:
    print("lettuce not in set")
if (member("tomato")):
    print("tomato in set")
else:
    print("tomato not in set")
