import math

class CuckooTable:
    """Hash table with Cuckoo hashing.

    We have two hash functions, which map 32-bit keys to buckets of a common
    hash table. Unused buckets contain None.
    """

    def __init__(self, num_buckets, hashes):
        """Initialize the table with the given number of buckets.
        The number of buckets is expected to stay constant."""

        # The array of buckets
        self.num_buckets = num_buckets
        self.table = [None] * num_buckets
        self.hashes = hashes

    def get_table(self):
        return self.table

    def lookup(self, key):
        """Check if the table contains the given key. Returns True or False."""

        b0 = self.hashes[0].hash(key)
        b1 = self.hashes[1].hash(key)
        # print("## Lookup key={} b0={} b1={}".format(key, b0, b1))
        return self.table[b0] == key or self.table[b1] == key

    def insert(self, key):
        """Insert a new key to the table. Assumes that the key is not present yet."""

        # TODO: Implement
        def log(x):
            result = 0
            while x // 2 > 0:
                x //= 2
                result += 1
            return result

        h0 = self.hashes[0].hash(key)
        h1 = self.hashes[1].hash(key)

        if self.table[h0] == key or self.table[h1] == key:
            return None

        if self.table[h0] is None or self.table[h1] is None:
            self.table[h0 if self.table[h0] is None else h1] = key
            return None

        self.table[h0], key = key, self.table[h0]

        counter = 6 * log(self.num_buckets)
        old_hash = h0

        while counter > 0 and key is not None:
            counter -= 1
            h = self.hashes[0].hash(key)

            if h == old_hash:
                h = self.hashes[1].hash(key)

            self.table[h], key = key, self.table[h]
            old_hash = h
        if key is not None:
            self.rehash(key)
        return key
        
    def rehash(self, key):
        """ Relocate all items using new hash functions and insert a given key. """
        # Obtain new hash functions
        for i in range(2):
            self.hashes[i].regenerate()

        # TODO: Implement
        old_table = self.table[:]

        while True:
            end = True
            self.table = [None] * self.num_buckets

            for value in old_table:
                if value is not None:
                    if self.insert(value) is not None:
                        end = False
                        break

            if self.insert(key) is None:
                break

            if end:
                break
