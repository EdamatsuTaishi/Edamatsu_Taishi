import matplotlib.pyplot as plt

# IIT example not shown in the lecture note:
# Independent alarms vs connected alarms

systems = [
    "Independent\nalarms",
    "Connected\nalarms"
]

integrated_information = [0.1, 1.0]

plt.figure(figsize=(6, 4))
plt.bar(systems, integrated_information)

plt.ylabel("Example integrated information")
plt.title("IIT Example: Independent vs Connected Alarm Systems")

plt.ylim(0, 1.2)

for i, value in enumerate(integrated_information):
    plt.text(i, value + 0.03, str(value), ha="center")

plt.tight_layout()
plt.show()