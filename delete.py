import numpy as np
import torch



d = 1
a = torch.tensor([2], device='cuda:0')
b = torch.tensor([3], device='cuda:0')
c = a-b
print(c)