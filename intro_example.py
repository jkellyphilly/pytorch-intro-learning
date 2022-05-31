import torch
import numpy as np
import pdb


if __name__ == "__main__":
    data = [[1, 2],[3, 4]]
    x_data = torch.tensor(data)
    
    np_data = np.array(data)
    x_np = torch.from_numpy(np_data)
    pdb.set_trace()