
import math
import matplotlib.pyplot as plt

states = ["00", "01", "10", "11"]

# Whole effect repertoire:
# the future units must be opposite.
p_whole = [0.0, 0.5, 0.5, 0.0]

# Partitioned repertoire:
# after cutting A and B, each unit is independently 0 or 1 with probability 1/2.
q_cut = [0.25, 0.25, 0.25, 0.25]

def kl_divergence(p, q):
    """Compute D_KL(p || q) in bits."""
    total = 0.0
    for pi, qi in zip(p, q):
        if pi > 0:
            total += pi * math.log2(pi / qi)
    return total

phi = kl_divergence(p_whole, q_cut)

x = range(len(states))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - width/2 for i in x], p_whole, width, label="Whole repertoire p")
plt.bar([i + width/2 for i in x], q_cut, width, label="Cut repertoire q")

plt.xticks(list(x), states)
plt.ylim(0, 0.65)
plt.xlabel("Future state $(A_{t+1}, B_{t+1})$")
plt.ylabel("Probability")
plt.title("IIT toy example: anti-synchrony is lost by cutting the system")
plt.legend()

for i, value in enumerate(p_whole):
    plt.text(i - width/2, value + 0.02, str(value), ha="center")
for i, value in enumerate(q_cut):
    plt.text(i + width/2, value + 0.02, str(value), ha="center")

plt.figtext(
    0.5,
    0.01,
    rf"$\phi^{{\pi}}_{{eff}} = D_{{KL}}(p \parallel q) = {phi:.1f}$ bit. "
    r"The whole specifies $A_{t+1} \ne B_{t+1}$, but the cut parts do not.",
    ha="center",
    fontsize=10,
)

plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.show()
