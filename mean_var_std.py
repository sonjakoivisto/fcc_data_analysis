import numpy as np

def calculate(list):

    if len(list) < 9:
      raise ValueError("List must contain nine numbers.")
    else:

      table = np.array([list[0:3],list[3:6],list[6:9]])


      calculations = {
      "mean": [[table[:,0].mean(), table[:,1].mean(), table[:,2].mean()],[table[0,:].mean(), table[1,:].mean(),table[2,:].mean()], table.mean()],

      "variance": [[table[:,0].var(), table[:,1].var(), table[:,2].var()],[table[0,:].var(), table[1,:].var(),table[2,:].var()], table.var()],

      "standard deviation": [[table[:,0].std(), table[:,1].std(), table[:,2].std()],[table[0,:].std(), table[1,:].std(),table[2,:].std()], table.std()],

      "max": [[table[:,0].max(), table[:,1].max(), table[:,2].max()],[table[0,:].max(), table[1,:].max(),table[2,:].max()], table.max()],

      "min": [[table[:,0].min(), table[:,1].min(), table[:,2].min()],[table[0,:].min(), table[1,:].min(),table[2,:].min()], table.min()], 

      "sum":[[table[:,0].sum(), table[:,1].sum(), table[:,2].sum()],[table[0,:].sum(), table[1,:].sum(),table[2,:].sum()], table.sum()]
      }
      return calculations

    

  
