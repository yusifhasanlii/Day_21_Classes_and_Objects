#!/usr/bin/python3

import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        frequency = {}
        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1
        
        mode_val = max(frequency, key=frequency.get)
        return {'mode': mode_val, 'count': frequency[mode_val]}

    def var(self):
        mean_val = self.mean()
        variance = sum((x - mean_val) ** 2 for x in self.data) / self.count()
        return round(variance, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        frequency = {}
        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1
        
        dist = [(round((v / self.count()) * 100, 1), k) for k, v in frequency.items()]
        dist.sort(reverse=True) # Böyükdən kiçiyə sıralamaq
        return dist

    def describe(self):
        return f"""
Count: {self.count()}
Sum:  {self.sum()}
Min:  {self.min()}
Max:  {self.max()}
Range:  {self.range()}
Mean:  {self.mean()}
Median:  {self.median()}
Mode:  ({self.mode()['mode']}, {self.mode()['count']})
Variance:  {self.var()}
Standard Deviation:  {self.std()}
Frequency Distribution: {self.freq_dist()}
"""


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print(data.describe())