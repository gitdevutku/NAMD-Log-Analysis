import matplotlib.pyplot as plt
import numpy as np

# Read the NAMD log file
with open('simul.txt', 'r', encoding='utf-16-le') as file:
    lines = file.readlines()


# Initialize lists to store data
timesteps = []
total_energies = []

# Extract data from the log file
for line in lines:
    if line.startswith("ENERGY:"):
        print(line)
        data = line.split()
        timesteps.append(int(data[1]))
        total_energies.append(float(data[4]))

# Check if data is extracted correctly
print("Timesteps:", timesteps)
print("ELECT:", total_energies)

# Convert lists to NumPy arrays
timesteps = np.array(timesteps)
total_energies = np.array(total_energies)

# Save data to .dat file
np.savetxt('bond-energy.dat', np.column_stack((timesteps, total_energies)), fmt='%d %.6f', header='TS TMPRP')

# Plotting
plt.plot(timesteps, total_energies, label='TMPRP')
plt.xlabel('TS')
plt.ylabel('TMPRP')
plt.title('TS : TMPRP')
plt.legend()
plt.show()
