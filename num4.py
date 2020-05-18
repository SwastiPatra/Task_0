sample = {'physics' : 88,
          'maths' : 75,
          'chemistry' : 72,
          'Basic electrical' : 69}
print(min(sample,
key = sample.get))