import numpy as np
import matplotlib.pyplot as plt

def calculate_phi(w):
    """
    結合強度 w における統合情報量 (Phi) を計算する。
    w = 0.5 のとき完全に独立 (Phi = 0)
    w = 1.0 のとき完全に同期 (Phi = 1, 講義ノートの例1.3に相当)
    """
    # 完全に独立している場合は、KLダイバージェンスは0
    if w == 0.5:
        return 0.0
    elif w == 1.0:
        return 1.0
    
    # 実際の分布 p (結合強度 w に依存)
    # p(0,0) = w/2, p(1,1) = w/2, p(0,1) = (1-w)/2, p(1,0) = (1-w)/2
    p = np.array([w/2, (1-w)/2, (1-w)/2, w/2])
    
    # 分割後の分布 q (各ユニットの周辺分布の積、常に 1/4)
    q = np.array([0.25, 0.25, 0.25, 0.25])
    
    # KLダイバージェンス (Phi) の計算
    phi = np.sum(p * np.log2(p / q))
    return phi

# 結合強度 w を 0.5 から 1.0 まで変化させる
w_vals = np.linspace(0.5, 1.0, 100)
phi_vals = [calculate_phi(w) for w in w_vals]

# プロットの作成
plt.figure(figsize=(8, 5))
plt.plot(w_vals, phi_vals, label=r'$\phi_{eff}(m)$', color='blue', linewidth=2)
plt.title('Integrated Information $\phi$ vs. Coupling Strength $w$\n(New IIT Example for Assignment)', fontsize=12)
plt.xlabel('Coupling Strength $w$ (0.5: Independent, 1.0: Fully Correlated)', fontsize=10)
plt.ylabel('Integrated Information $\phi$ (bits)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=1.0, color='r', linestyle=':', label='Example 1.3 Max (1 bit)')
plt.legend(fontsize=10)

# 画像の保存
plt.savefig('iit_plot.png', dpi=300)
print("Plot successfully saved as 'iit_plot.png'")
plt.show()
