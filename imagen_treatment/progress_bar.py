import math
import time

from tqdm import tqdm

results = []

results = [math.factorial(x) for x in tqdm(range(8000))]