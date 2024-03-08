import matplotlib.pyplot as plt
import numpy as np

# Criando dados para os gráficos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Criando os gráficos
plt.figure(figsize=(12, 4))

# Gráfico 1
plt.subplot(1, 3, 1)
plt.plot(x, y1)
plt.title('Gráfico 1: Seno')

# Gráfico 2
plt.subplot(1, 3, 2)
plt.plot(x, y2)
plt.title('Gráfico 2: Cosseno')

# Gráfico 3
plt.subplot(1, 3, 3)
plt.plot(x, y3)
plt.title('Gráfico 3: Tangente')

# Exibindo os gráficos
plt.tight_layout()
plt.show()
