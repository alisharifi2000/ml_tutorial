# AUTOGENERATED! DO NOT EDIT! File to edit: 02_logistic_regression.ipynb (unless otherwise specified).

__all__ = ['sigmoid']

# Cell
def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))