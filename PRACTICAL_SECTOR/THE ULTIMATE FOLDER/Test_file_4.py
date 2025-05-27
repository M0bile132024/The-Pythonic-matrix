import numpy as np


# Check if the lengths of frequencies and values match
def mean_freq(frequencies, values):
    if len(frequencies) != len(values):
        raise ValueError("The lengths of frequencies and values must match.")
    for i in range(len(frequencies)):
        if frequencies[i] < 0:
            raise ValueError("Frequencies must be non-negative.")
        if values[i] < 0:
            raise ValueError("Values must be non-negative.")

    total_freq_list = []
    for i in range(len(frequencies)):
        total_freq_list.append(frequencies[i] * values[i])
    total_frequency = sum(total_freq_list)

    total_value = sum(values)
 
    mean = total_frequency / total_value
    return mean

mean = mean_freq(frequencies, values)
print("Mean frequency:", mean)









