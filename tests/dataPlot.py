# importing module
from pandas import *
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

def filter_alpha_beta(fs,wind_len, lower_alpha=0.5, upper_alpha=4, lower_beta=25, upper_beta=30, r_or_l=1, plot=1):
    freq_step = fs / wind_len
    alpha_band = (int(lower_alpha / freq_step), int(upper_alpha / freq_step))
    beta_band = (int(lower_beta / freq_step), int(upper_beta / freq_step))

    right_data = list(data.loc[:, 'AF8']- data.loc[:, 'TP10'])
    left_data = list(data.loc[:, 'AF7']-data.loc[:, 'TP9'])
    right_data2 = list(data2.loc[:, 'AF8']- data2.loc[:, 'TP10'])
    left_data2 = list(data2.loc[:, 'AF7']-data2.loc[:, 'TP9'])
    right_fft = np.fft.rfft(right_data)
    left_fft = np.fft.rfft(left_data)

    r_alpha_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    r_alpha_freq[alpha_band[0]: alpha_band[1] + 1] = right_fft[alpha_band[0]: alpha_band[1] + 1]

    l_alpha_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    l_alpha_freq[alpha_band[0]: alpha_band[1] + 1] = left_fft[alpha_band[0]: alpha_band[1] + 1]

    r_beta_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    r_beta_freq[beta_band[0]: beta_band[1] + 1] = right_fft[beta_band[0]: beta_band[1] + 1]

    l_beta_freq = np.zeros(int(wind_len / 2) + 1, dtype="complex_")
    l_beta_freq[beta_band[0]: beta_band[1] + 1] = left_fft[beta_band[0]: beta_band[1] + 1]

    r_alpha = np.fft.irfft(r_alpha_freq)
    l_alpha = np.fft.irfft(l_alpha_freq)
    r_beta = np.fft.irfft(r_beta_freq)
    l_beta = np.fft.irfft(l_beta_freq)
    r_peaks, _ = signal.find_peaks(r_alpha,width=45)
    r_peaks2, _ = signal.find_peaks(-r_alpha,width=45)
    l_peaks, _ = signal.find_peaks(l_alpha,height=80)
    l_peaks2, _ = signal.find_peaks(-l_alpha, height=100)
    lowerarr = []
    upperarr = []
    for i in range(r_peaks.size-1):
        for j in range(r_peaks2.size):
            if r_peaks[i]<r_peaks2[j]<r_peaks[i+1]:
                if np.std(r_alpha[r_peaks[i]:r_peaks2[j]]) < 150:
                    lowerarr.append(r_alpha[r_peaks2[j]])
                    upperarr.append(r_alpha[r_peaks[i]])
                break
            elif r_peaks[i+1]<r_peaks2[j]:
                break
    calbLowerTH = np.mean(lowerarr)
    calbUpperTH = np.mean(upperarr)
    # mqttClient.publish("/calibrate/minTH",calbLowerTH)
    # mqttClient.publish("/calibrate/maxTH",calbUpperTH)
    print("min= ",calbLowerTH)
    print("max= ",calbUpperTH)
    # print(r_alpha[r_peaks[0]],r_alpha[r_peaks2[1]])
    # print("STD= ",np.std(r_alpha[r_peaks[0]:r_peaks2[1]]))
    
        # r_alpha, l_alpha, r_beta, l_beta = self.filter_alpha_beta(lower_alpha=0.5, upper_alpha=4, lower_beta=4.5, upper_beta=8)
        # r_data = list(self.data.loc[:, "Right"])
        # l_data = list(self.data.loc[:, "Left"])
    # plot original window
    if plot:
        fig, ax = plt.subplots(2, 1)
        # plt.figure(fig,figsize=(15,6))
        if r_or_l:
            ax[0].plot(right_data)
            ax[0].set_title("Right Data")
            ax[1].plot(r_alpha)
            ax[1].set_title("FFT Data")
            # ax[1].plot(r_alpha)
            ax[1].plot(r_peaks, r_alpha[r_peaks], "x")
            ax[1].plot(r_peaks2, r_alpha[r_peaks2], "o")
            # ax[1].set_title("Delta")
            # ax[1].axhline(y = 100, color = 'r', linestyle = '--')
            # ax[1].axhline(y = -50, color = 'g', linestyle = '--')
            # ax[2].plot(r_beta)
            # ax[2].set_title("Theta")
        else:
            ax[0].plot(left_data)
            ax[0].set_title("Left Data")
            ax[1].plot(left_data2)
            ax[1].set_title("Left Data")
            # ax[1].plot(l_alpha)
            # # ax[1].plot(l_peaks, l_alpha[l_peaks], "x")
            # # ax[1].plot(l_peaks2, l_alpha[l_peaks2], "o")
            # ax[1].set_title("Delta")
            # ax[1].axhline(y = 80, color = 'r', linestyle = '--')
            # ax[1].axhline(y = -50, color = 'g', linestyle = '--')
            # # ax[2].plot(l_beta)
            # ax[2].set_title("Beta")
        plt.show()
    

# reading CSV file
data = read_csv("E:/Graduation_Project/Smart-Home-System-controlled-by-EEG/Data/left&right/look_right_1.csv")
data2 = read_csv("E:/Graduation_Project/Smart-Home-System-controlled-by-EEG/Data/left&right/look_left_1.csv")
tp9_1 = np.array(list(data.loc[:, 'TP9']))
af7_1 = np.array(list(data.loc[:, 'AF7']))
af8_1 = np.array(list(data.loc[:, 'AF8']))
tp10_1 = np.array(list(data.loc[:, 'TP10']))
tp9_2 = np.array(list(data2.loc[:, 'TP9']))
af7_2 = np.array(list(data2.loc[:, 'AF7']))
af8_2 = np.array(list(data2.loc[:, 'AF8']))
tp10_2 = np.array(list(data2.loc[:, 'TP10']))
# fig, ax = plt.subplots(2, 1)
# ax[0].plot(tp9_1)
# ax[0].plot(af7_1)
# ax[0].plot(af8_1)
# ax[0].plot(tp10_1)
# ax[0].set_title("look right Data")
# ax[1].plot(tp9_2)
# ax[1].plot(af7_2)
# ax[1].plot(af8_2)
# ax[1].plot(tp10_2)
# ax[1].set_title("look left Data")

fig, ax = plt.subplots(4, 1)
ax[0].plot(tp9_1)
ax[0].set_title("TP9 Data right")
ax[1].plot(af7_1)
ax[1].set_title("AF7 Data right")
ax[2].plot(af8_1)
ax[2].set_title("AF8 Data right")
ax[3].plot(tp10_1)
ax[3].set_title("TP10 Data right")

fig2, ax2 = plt.subplots(4, 1)
ax2[0].plot(tp9_2)
ax2[0].set_title("TP9 Data left")
ax2[1].plot(af7_2)
ax2[1].set_title("AF7 Data left")
ax2[2].plot(af8_2)
ax2[2].set_title("AF8 Data left")
ax2[3].plot(tp10_2)
ax2[3].set_title("TP10 Data left")

plt.show()
# datatest = np.array(list(data.loc[:, 'TP9']))
# stddata = np.std(datatest)
# fftdata = np.fft.rfft(datatest)
# feqstep = 255/1300
# band = np.zeros(750,dtype="complex_")
# # band[int(10/feqstep):int(50/feqstep)] = fftdata[int(10/feqstep):int(50/feqstep)]
# band = fftdata
# reconstructed = np.fft.irfft(band)
# checkfft = np.fft.fft(reconstructed)
# # maxindex = np.array(fftdata[1:200]).argmax()
# # print(maxindex)
# # for d in fftdata:
# #     print(abs(d))
# # plt.plot(fftdata[0:200])
# # plt.plot(datatest)
# plt.plot(checkfft)
# plt.show()

# left_data = list(data.loc[:, 'AF7']-data.loc[:, 'TP9'])
# plt.plot(left_data)
# plt.show()
# filter_alpha_beta(256,1300)
# converting column data to list
# TP10 = data['TP10'].tolist()
# # timeStamps = data['timestamps'].tolist
# timeStamps = np.array(TP10)

# plt.figure(figsize=(15,6))
# plt.plot(TP10)
# plt.show()

# peaks, _ = signal.find_peaks(rData,height=60)
# peaks2, _ = signal.find_peaks(-rData, height=200)
# properties["prominences"], properties["widths"]
# (array([1.495, 2.3  ]), array([36.93773946, 39.32723577]))
# plt.plot(rData)
# plt.plot(peaks, rData[peaks], "x")
# plt.plot(peaks2, rData[peaks2], "o")
# plt.vlines(x=peaks, ymin=timeStamps[peaks] - properties["prominences"],
#            ymax = timeStamps[peaks], color = "C1")
# plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
#            xmax=properties["right_ips"], color = "C1")
# plt.show()

# print(AF7)
