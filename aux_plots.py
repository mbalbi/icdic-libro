import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import quad

# Set up the figure with three subplots
fig, axs = plt.subplots(3, 1, figsize=(5, 6))
plt.subplots_adjust(hspace=0.4)

# Define credible interval percentage
credible_interval = 0.85  # 95% credible interval
alpha = 1 - credible_interval

# Function to find symmetric credible interval bounds
def find_symmetric_credible_interval(pdf_func, x_range, cdf_func=None):
    # If no CDF function is provided, create one using numerical integration
    if cdf_func is None:
        def cdf_func(x):
            result, _ = quad(pdf_func, x_range[0], x)
            return result
    
    # Define the function to find alpha/2 and 1-alpha/2 quantiles
    def find_quantile(p):
        # Simple binary search to find the quantile
        left, right = x_range[0], x_range[1]
        for _ in range(50):  # More iterations for better precision
            mid = (left + right) / 2
            if cdf_func(mid) < p:
                left = mid
            else:
                right = mid
        return (left + right) / 2
    
    lower_bound = find_quantile(alpha / 2)
    upper_bound = find_quantile(1 - alpha / 2)
    
    return lower_bound, upper_bound

# 1. Normal Distribution
mu, sigma = 0, 1
x_normal = np.linspace(-4, 4, 1000)
pdf_normal = stats.norm.pdf(x_normal, mu, sigma)
cdf_normal = stats.norm.cdf(x_normal, mu, sigma)

# Calculate credible interval bounds using scipy's built-in functions
lower_normal = stats.norm.ppf(alpha / 2, mu, sigma)
upper_normal = stats.norm.ppf(1 - alpha / 2, mu, sigma)

# Plot normal distribution
axs[0].plot(x_normal, pdf_normal, 'C0-', label='Normal Distribution')
axs[0].fill_between(x_normal, pdf_normal, 
                   where=((x_normal >= lower_normal) & (x_normal <= upper_normal)),
                   alpha=0.5, color='C0', label=f'{credible_interval*100:.0f}% Credible Interval')
# axs[0].axvline(lower_normal, color='r', linestyle='--')
# axs[0].axvline(upper_normal, color='r', linestyle='--')
# axs[0].set_title('Normal Distribution with Symmetric Credible Interval')
# axs[0].legend()
axs[0].set_xlim([-4, 4])
axs[0].set_ylim([0, 0.45])
axs[0].grid(True, alpha=0.3)

# 2. Left Triangular Distribution
def triangular_pdf(x):
    if 0 <= x <= 1:
        return 2 * (1 - x)
    else:
        return 0

x_triangular = np.linspace(0, 1, 1000)
pdf_triangular = [triangular_pdf(x) for x in x_triangular]

# Define CDF for triangular distribution
def triangular_cdf(x):
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        return 2*x - x**2

# Calculate credible interval bounds
lower_triangular, upper_triangular = find_symmetric_credible_interval(
    triangular_pdf, [0, 1], lambda x: triangular_cdf(x))

# Plot triangular distribution
axs[1].plot(x_triangular, pdf_triangular, 'C1-', label='Left Triangular Distribution')
axs[1].fill_between(x_triangular, pdf_triangular, 
                   where=((x_triangular >= lower_triangular) & (x_triangular <= upper_triangular)),
                   alpha=0.5, color='C1', label=f'{credible_interval*100:.0f}% Credible Interval')
# axs[1].axvline(lower_triangular, color='r', linestyle='--')
# axs[1].axvline(upper_triangular, color='r', linestyle='--')
# axs[1].set_title('Left Triangular Distribution with Symmetric Credible Interval')
# axs[1].legend()
axs[1].set_xlim([0, 1])
axs[1].set_ylim([0, 2.2])
axs[1].grid(True, alpha=0.3)

# 3. Bimodal Distribution (mixture of two normals)
def bimodal_pdf(x):
    return 0.5 * stats.norm.pdf(x, -1.5, 0.5) + 0.5 * stats.norm.pdf(x, 1.5, 0.5)

def bimodal_cdf(x):
    return 0.5 * stats.norm.cdf(x, -1.5, 0.5) + 0.5 * stats.norm.cdf(x, 1.5, 0.5)

x_bimodal = np.linspace(-4, 4, 1000)
pdf_bimodal = [bimodal_pdf(x) for x in x_bimodal]

# Calculate credible interval bounds
lower_bimodal, upper_bimodal = find_symmetric_credible_interval(
    bimodal_pdf, [-4, 4], lambda x: bimodal_cdf(x))

# Plot bimodal distribution
axs[2].plot(x_bimodal, pdf_bimodal, 'C2', label='Bimodal Distribution')
axs[2].fill_between(x_bimodal, pdf_bimodal, 
                   where=((x_bimodal >= lower_bimodal) & (x_bimodal <= upper_bimodal)),
                   alpha=0.5, color='C2', label=f'{credible_interval*100:.0f}% Credible Interval')
# axs[2].axvline(lower_bimodal, color='r', linestyle='--')
# axs[2].axvline(upper_bimodal, color='r', linestyle='--')
# axs[2].set_title('Bimodal Distribution with Symmetric Credible Interval')
# axs[2].legend()
axs[2].set_xlabel('x')
axs[2].set_xlim([-4, 4])
axs[2].set_ylim([0, 0.45])
axs[2].grid(True, alpha=0.3)

# Add overall title
# fig.suptitle(f'{credible_interval*100:.0f}% Symmetric Credible Intervals for Different Distributions', 
#              fontsize=16, y=0.98)

# Print the credible interval bounds for each distribution
print(f"Normal distribution: {lower_normal:.4f} to {upper_normal:.4f}")
print(f"Left triangular distribution: {lower_triangular:.4f} to {upper_triangular:.4f}")
print(f"Bimodal distribution: {lower_bimodal:.4f} to {upper_bimodal:.4f}")

plt.tight_layout()
plt.show()