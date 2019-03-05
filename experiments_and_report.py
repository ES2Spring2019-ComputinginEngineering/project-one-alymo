#Step 5: Experiments and Report
#Mo Liu and Alyssa Attonito
#This section analyzes the relationship between pendulum length and period for real-world data and simulated data.

plt.subplot(2, 1, 1)
plt.plot(t, y_noisy_filt)
plt.xscale('log')
plt.yscale('log')
plt.title('log')
plt.grid(True)
