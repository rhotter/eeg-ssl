from preprocessing.preprocessing import preprocess
from ssl.SSL_create_TS_RP import create
from EEG_SSL_Dataset import get_RP_minibatch
import sys
import numpy as np


def eeg_ssl(data_folder, T_pos_RP, T_neg_RP, T_pos_TS, T_neg_TS, num_users, num_samples):
     """ Divides the mne dataset into many samples of length e_len seconds.

     Args:
        data_folder: folder containing EEG .edf files
        T_pos_RP: an integer representing the positive limit for relative positioning.
        T_neg_RP: an integer representing the negative limit for relative positioning.
        T_pos_TS: an integer representing the positive limit for temporal shuffling.
        T_neg_TS: an integer representing the negative limit for temporal shuffling.


     Returns:
        
     """
     preprocessed = get_RP_minibatch(data_folder, T_pos_RP, T_neg_RP, num_users, num_samples)
     # preprocessed = preprocess(data_folder)
     print(preprocessed)
     #np.save("preprocessed.npy", preprocessed)
     #create(preprocessed, T_pos_RP, T_neg_RP, T_pos_TS, T_neg_TS)

if __name__ == '__main__':
    data_folder = sys.argv[1]
    T_pos_RP = sys.argv[2]
    T_neg_RP = sys.argv[3]
    T_pos_TS = sys.argv[2]
    T_neg_TS = sys.argv[3]
    num_users = sys.argv[4]
    num_samples = sys.argv[5]
    eeg_ssl(data_folder, T_pos_RP, T_neg_RP, T_pos_TS, T_neg_TS, num_users, num_samples)

# AC :)