"""
Data Processor Tool
A simple Python script to calculate summary statistics from numerical data.
"""

import math

def calculate_stats(numbers):
    """Calculates mean, median, min, max, and standard deviation."""
    if not numbers:
        return None
    
    n = len(numbers)
    mean_val = sum(numbers) / n
    sorted_nums = sorted(numbers)
    
    # Median calculation
    if n % 2 == 1:
        median_val = sorted_nums[n // 2]
    else:
        median_val = (sorted_nums[(n // 2) - 1] + sorted_nums[n // 2]) / 2.0

    # Variance and Standard Deviation
    variance = sum((x - mean_val) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)

    return {
        "count": n,
        "min": sorted_nums[0],
        "max": sorted_nums[-1],
        "mean": round(mean_val, 2),
        "median": round(median_val, 2),
        "std_dev": round(std_dev, 2),
    }

def main():
    # Sample dataset
    data = [12.5, 45.0, 78.2, 23.4, 89.1, 34.6, 56.8, 90.0, 11.2]
    
    print("--- Data Processing Report ---")
    print(f"Dataset: {data}\n")
    
    stats = calculate_stats(data)
    
    print("Summary Statistics:")
    for key, value in stats.items():
        print(f"  - {key.replace('_', ' ').capitalize()}: {value}")

if __name__ == "__main__":
    main()
