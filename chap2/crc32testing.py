import random
import numpy as np
import matplotlib.pyplot as plt
from zlib import crc32

# Function to compute crc32 hash values
def compute_crc32_hashes(n):
    hashes = []
    for i in range(n):
        identifier = random.randint(0, 2**32 - 1)  # Generate a random integer within 32-bit range
        hash_value = crc32(np.int64(identifier)) & 0xffffffff  # Compute crc32 and ensure it is 32-bit
        hashes.append(hash_value)
    return hashes



# Function to plot the hash values
def plot_hash_distribution(hashes):
    plt.figure(figsize=(10, 6))
    plt.hist(hashes, bins=100, range=(0, 2**32), color='blue', edgecolor='black')
    plt.title('Distribution of crc32 Hash Values')
    plt.xlabel('Hash Value')
    plt.ylabel('Frequency')
    plt.show()

# Main function
def main():
    n = int(input("Enter the number of integers (n): "))
    hashes = compute_crc32_hashes(n)
    plot_hash_distribution(hashes)

if __name__ == "__main__":
    main()
