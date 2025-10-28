# CarPricePredict
## Project for Training a Model from Scratch

### Objective
The goal of this project was to train a model from scratch: collect and prepare data, clean it, train the model, and evaluate its performance. Throughout this process, we went through all stages of the full machine learning cycle — from data preprocessing to result analysis.

## File Structure

- **`script*.py`** – scripts for data collection and cleaning.
- **`training.py`** – scripts for training the model.
- **`MSE.py`** – calculation of model quality metrics (e.g., MSE).
- **`weight.npy`** – file containing the trained weights.  
  To load the weights, use the following code:

```python
import numpy as np

w = np.load("weight.npy")
```
