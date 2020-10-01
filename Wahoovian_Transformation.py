#tnm6qz Talia Miller

import numpy as np
import logging

def wahoovian(m):
    num_rows, num_cols = m.shape
    if num_rows!=num_cols:
        logging.info("Not a square matrix!")
        return m
    elif np.all((m == 0)):
        logging.info("This is a zero matrix!")
        return m
    else:
        logging.info("Matrix transposing and negation is beginning")
        f = np.transpose(m)
        logging.info("Transposing is done!")
        f*=-1
        logging.info("Negating is done!")
        return f
