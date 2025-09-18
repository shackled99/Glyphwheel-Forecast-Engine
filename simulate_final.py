import json
import numpy as np
import matplotlib.pyplot as plt


# Load JSON
with open("../data/glyphwheel_ontology_v22.json") as f:
ontology = json.load(f)


nodes = ontology['nodes']
edges = ontology['edges']


domain_colors = {
"Minoan": "#ff6b6b",
"Voynich": "#4ecdc4",
"Rongorongo": "#95e1d3",
"Minoan-Voynich": "#ffeaa7",
"M-V Fractal": "#a55eea",
"Rongo Fractal": "#a55eea"
}


# Polar spiral
fig, ax = plt.subplots(figsize=(12,12), subplot_kw={'projection':'polar'})
theta = np.linspace(0, 10*np.pi, 500)
r = np.exp(0.12*theta)
ax.plot(theta, r, 'k-', alpha=0.1)


# Node positions
node_positions = {node['id']: (np.random.rand()*2*np.pi, node['gsi']*(np.random.rand()*2+1)) for node in nodes}
for node in nodes:
ax.scatter(node_positions[node['id']][0], node_positions[node['id']][1],
s=node['gsi']*200,
color=domain_colors[node['domain']])
ax.text(node_positions[node['id']][0], node_positions[node['id']][1]*1.05,
node['label'], ha='center', va='center', fontsize=9, color='white')


# Edges
for edge in edges:
source_pos = node_positions[edge['source']]
target_pos = node_positions[edge['target']]
ax.plot([source_pos[0], target_pos[0]], [source_pos[1], target_pos[1]],
color='white', alpha=1-edge['tension'], linestyle='--', linewidth=edge['tension']*10)


ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_axis_off()
ax.set_title('Glyphwheel Final Spiral Ontology', fontsize=16, color='white', pad=20)
plt.show()