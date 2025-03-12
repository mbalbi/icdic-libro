import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import minimize_scalar
from scipy.integrate import quad

# Set up the figure with three subplots
fig, axs = plt.subplots(3, 1, figsize=(5, 6))
plt.subplots_adjust(hspace=0.4)

# Define credible interval percentage
credible_interval = 0.85  # 95% credible interval

# Function to find highest density interval (HDI)
def find_hdi(pdf_func, cdf_func, x_range, credible_interval=0.95, precision=1000):
    x_vals = np.linspace(x_range[0], x_range[1], precision)
    pdf_vals = np.array([pdf_func(x) for x in x_vals])
    
    # Sort points by density
    sorted_indices = np.argsort(pdf_vals)[::-1]  # Descending order
    sorted_x = x_vals[sorted_indices]
    sorted_pdf = pdf_vals[sorted_indices]
    
    # Find cumulative probability
    cumulative_prob = np.zeros_like(sorted_pdf)
    for i in range(len(sorted_x)):
        # For each point, add its contribution to the CDF
        # Approximating using the bin width
        bin_width = (x_range[1] - x_range[0]) / precision
        cumulative_prob[i] = sorted_pdf[i] * bin_width
    
    cum_sum = np.cumsum(cumulative_prob)
    # Normalize to account for discretization errors
    cum_sum = cum_sum / cum_sum[-1]
    
    # Find the threshold where we reach the desired credible interval
    threshold_idx = np.argmin(np.abs(cum_sum - credible_interval))
    threshold_density = sorted_pdf[threshold_idx]
    
    # All points with density above this threshold are in the HDI
    hdi_mask = pdf_vals >= threshold_density
    
    # Find contiguous regions (this works for unimodal and some multimodal distributions)
    hdi_regions = []
    in_region = False
    start_idx = 0
    
    for i in range(len(x_vals)):
        if hdi_mask[i] and not in_region:
            # Start of a new region
            in_region = True
            start_idx = i
        elif not hdi_mask[i] and in_region:
            # End of a region
            in_region = False
            hdi_regions.append((x_vals[start_idx], x_vals[i-1]))
    
    # If the last region extends to the end of the array
    if in_region:
        hdi_regions.append((x_vals[start_idx], x_vals[-1]))
    
    return hdi_regions, threshold_density

# 1. Normal Distribution
mu, sigma = 0, 1
x_normal = np.linspace(-4, 4, 1000)
pdf_normal = stats.norm.pdf(x_normal, mu, sigma)

# Define normal PDF and CDF functions
def normal_pdf(x):
    return stats.norm.pdf(x, mu, sigma)

def normal_cdf(x):
    return stats.norm.cdf(x, mu, sigma)

# Find HDI for normal
hdi_regions_normal, threshold_normal = find_hdi(normal_pdf, normal_cdf, [-4, 4], credible_interval)

# Plot normal distribution
axs[0].plot(x_normal, pdf_normal, 'C0-', label='Normal Distribution')
# Shade HDI regions
for region in hdi_regions_normal:
    mask = (x_normal >= region[0]) & (x_normal <= region[1])
    axs[0].fill_between(x_normal, pdf_normal, where=mask, alpha=0.5, color='C0')
    # axs[0].axvline(region[0], color='r', linestyle='--')
    # axs[0].axvline(region[1], color='r', linestyle='--')
# Draw the threshold density line
# axs[0].axhline(threshold_normal, color='green', linestyle=':', label='Density Threshold')
# axs[0].set_title('Normal Distribution with Highest Density Interval')
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

def triangular_cdf(x):
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        return 2*x - x**2

x_triangular = np.linspace(0, 1, 1000)
pdf_triangular = [triangular_pdf(x) for x in x_triangular]

# Find HDI for triangular
hdi_regions_triangular, threshold_triangular = find_hdi(triangular_pdf, triangular_cdf, [0, 1], credible_interval)

# Plot triangular distribution
axs[1].plot(x_triangular, pdf_triangular, 'C1-', label='Left Triangular Distribution')
# Shade HDI regions
for region in hdi_regions_triangular:
    mask = (x_triangular >= region[0]) & (x_triangular <= region[1])
    axs[1].fill_between(x_triangular, pdf_triangular, where=mask, alpha=0.5, color='C1')
    # axs[1].axvline(region[0], color='r', linestyle='--')
    # axs[1].axvline(region[1], color='r', linestyle='--')
# Draw the threshold density line
# axs[1].axhline(threshold_triangular, color='green', linestyle=':', label='Density Threshold')
# axs[1].set_title('Left Triangular Distribution with Highest Density Interval')
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

# Find HDI for bimodal
hdi_regions_bimodal, threshold_bimodal = find_hdi(bimodal_pdf, bimodal_cdf, [-4, 4],
                                                  credible_interval)

# Plot bimodal distribution
axs[2].plot(x_bimodal, pdf_bimodal, 'C2', label='Bimodal Distribution')
# Shade HDI regions
for region in hdi_regions_bimodal:
    mask = (x_bimodal >= region[0]) & (x_bimodal <= region[1])
    axs[2].fill_between(x_bimodal, pdf_bimodal, where=mask, alpha=0.5, color='C2')
    # axs[2].axvline(region[0], color='r', linestyle='--')
    # axs[2].axvline(region[1], color='r', linestyle='--')
# Draw the threshold density line
# axs[2].axhline(threshold_bimodal, color='green', linestyle=':', label='Density Threshold')
# axs[2].set_title('Bimodal Distribution with Highest Density Interval')
# axs[2].legend()
axs[2].set_xlabel('x')
axs[2].set_xlim([-4, 4])
axs[2].set_ylim([0, 0.45])
axs[2].grid(True, alpha=0.3)

# Add overall title
# fig.suptitle(f'{credible_interval*100:.0f}% Highest Density Intervals for Different Distributions', 
#              fontsize=16, y=0.98)

# Print the HDI regions for each distribution
print(f"Normal distribution HDI: {hdi_regions_normal}")
print(f"Left triangular distribution HDI: {hdi_regions_triangular}")
print(f"Bimodal distribution HDI: {hdi_regions_bimodal}")

plt.tight_layout()
plt.show()