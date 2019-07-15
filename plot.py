import matplotlib.pyplot as plt
import numpy as np

# homeA = np.load("./Fully_connected/Home A/threshold0-2-st10-lr0001-batch16_te_acc.npy")[:300, ...]
# homeB = np.load("./Fully_connected/Home B/threshold0-2-st10-lr0001-batch16_te_acc.npy")[:300, ...]

# homeA = np.load("./LSTM/HomeA/threshold0-2-st10-lr0001-batch16_tr_acc.npy")
# homeB = np.load("./LSTM/HomeA/threshold0-2-st10-lr0001-batch16_te_acc.npy")


#fcn_te = np.load("./Fully_connected/Home B/threshold0-2-st10-lr0001-batch16_te_acc.npy")[:300, ...]
lstm_te = np.load("./LSTM/threshold0-2-st10-lr0001-batch16_te_acc.npy")[:1000, ...]
#fcn_tr = np.load("./Fully_connected/Home B/threshold0-2-st10-lr0001-batch16_tr_acc.npy")[:300, ...]
lstm_tr = np.load("./LSTM/threshold0-2-st10-lr0001-batch16_tr_acc.npy")[:1000, ...]
# homeA[0, 1] = 0.45

def smooth_data(data, smoothing_weight):
    last = data[0]
    for i in range(1, data.shape[0]):
        data[i] = last * smoothing_weight + (1 - smoothing_weight) * data[i]
        last = data[i]

    return data


# plt.plot(homeA[:, 0], smooth_data(homeA[:, 1], 0.9), 'r--', label="Train Set", linewidth=3.0)
# plt.plot(homeB[:, 0], smooth_data(homeB[:, 1], 0.9), 'b-.', label='Test Set', linewidth=3.0)


# plt.plot(fcn_tr[:, 0], smooth_data(fcn_tr[:, 1], 0.9), 'm-', label="Train on Home B (FCN)", linewidth=3.0)
plt.plot(lstm_tr[:, 0], smooth_data(lstm_tr[:, 1], 0.9), 'c-', label='Train on Random Sequence (LSTM)', linewidth=3.0)
#plt.plot(fcn_te[:, 0], smooth_data(fcn_te[:, 1], 0.9), 'y-', label="Test on Home B (FCN)", linewidth=3.0)
plt.plot(lstm_te[:, 0], smooth_data(lstm_te[:, 1], 0.9), 'g-', label='Test on Random Sequence (LSTM)', linewidth=3.0)


plt.xlabel("Number of Epochs", fontsize=18)
plt.ylabel("Accuracy", fontsize=18)
plt.yscale('linear')
# plt.xlim(0, 100)
plt.ylim(0, 1.1)
# plt.title("Home B")
plt.title("Train/Test on Random Sequence with LSTM")

plt.legend(loc='right')
plt.show()
