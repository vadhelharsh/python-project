import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(12, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 16)
ax.axis('off')

# Define colors
box_color = '#E3F2FD'
arrow_color = '#1976D2'
text_color = '#333333'

# Define box positions and labels
boxes = [
    (5, 15, "User Enters URL"),
    (5, 13.5, "Web Browser"),
    (5, 12, "OS Cache"),
    (5, 10.5, "Recursive Resolver\n(ISP/Google DNS)"),
    (5, 9, "Root DNS Server"),
    (5, 7.5, "TLD DNS Server\n(.com, .org)"),
    (5, 6, "Authoritative DNS Server"),
    (5, 4.5, "Returns IP Address"),
    (5, 3, "Web Browser Connects\nto Web Server"),
    (5, 1.5, "Website Appears")
]

# Create boxes
for x, y, label in boxes:
    # Create rounded rectangle
    box = FancyBboxPatch(
        (x-1.8, y-0.4), 3.6, 0.8,
        boxstyle="round,pad=0.1",
        facecolor=box_color,
        edgecolor='#1976D2',
        linewidth=2
    )
    ax.add_patch(box)
    
    # Add text
    ax.text(x, y, label, ha='center', va='center', 
            fontsize=10, fontweight='bold', color=text_color)

# Create arrows between boxes
arrow_positions = [
    (5, 14.6, 5, 13.9),  # URL to Browser
    (5, 13.1, 5, 12.4),  # Browser to OS Cache
    (5, 11.6, 5, 10.9),  # OS Cache to Recursive
    (5, 10.1, 5, 9.4),   # Recursive to Root
    (5, 8.6, 5, 7.9),    # Root to TLD
    (5, 7.1, 5, 6.4),    # TLD to Authoritative
    (5, 5.6, 5, 4.9),    # Authoritative to IP
    (5, 4.1, 5, 3.4),    # IP to Browser Connect
    (5, 2.6, 5, 1.9)     # Connect to Website
]

for x1, y1, x2, y2 in arrow_positions:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Add side annotations
side_notes = [
    (8.5, 12, "Checks local\nDNS cache", 'left'),
    (8.5, 10.5, "Provided by ISP or\nthird-party service", 'left'),
    (8.5, 9, "Returns Top-Level\nDomain server", 'left'),
    (8.5, 7.5, "Returns authoritative\nserver address", 'left'),
    (8.5, 6, "Has actual IP\nof domain", 'left')
]

for x, y, note, align in side_notes:
    ax.text(x, y, note, ha=align, va='center', 
            fontsize=9, style='italic', color='#666666')
    
    # Add connecting lines
    if align == 'left':
        ax.plot([6.8, 8.2], [y, y], '--', color='#999999', alpha=0.7, lw=1)

# Add title
ax.text(5, 15.8, 'DNS Resolution Process', ha='center', va='center', 
        fontsize=16, fontweight='bold', color=text_color)

# Add subtitle
ax.text(5, 0.5, 'How a Domain Name Gets Resolved to an IP Address', 
        ha='center', va='center', fontsize=12, style='italic', color='#666666')

plt.tight_layout()
plt.show()

# Optional: Save the figure
# plt.savefig('dns_resolution_diagram.png', dpi=300, bbox_inches='tight')