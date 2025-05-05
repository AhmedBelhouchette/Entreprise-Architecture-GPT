# import networkx as nx
# import matplotlib.pyplot as plt

# # Create a directed graph
# G = nx.DiGraph()

# # Add nodes
# nodes = range(1, 6)  # Example nodes
# G.add_nodes_from(nodes)

# # Add edges (relationships)
# edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
# G.add_edges_from(edges)

# # Use a force-directed layout
# pos = nx.spring_layout(G, seed=42, k=0.5)  # k controls node spacing

# # Draw the graph
# plt.figure(figsize=(8, 6))
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12, font_weight="bold", arrows=True)
# plt.show()
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
from networkx.drawing.nx_agraph import graphviz_layout

# Create a directed graph
G = nx.DiGraph()

# Add nodes categorized by layer
motivation_nodes = [
    "Utilisateurs",
    "Collaboration efficace",
    "Améliorer la gestion de projets",
    "Projets livrés à temps",
    "Intégration avec d'autres outils",
]
business_nodes = [
    "Chef de projet",
    "Membre de l'équipe",
    "Création de projet",
    "Assignation de tâches",
    "Tableau de bord analytique",
    "Notifications temps réel",
]
application_nodes = [
    "Application SaaS TeamFlow",
    "Gestion des projets",
    "Interface utilisateur",
    "Service de chat intégré",
    "Données de projet",
]
technology_nodes = ["Serveur cloud", "Service de sauvegarde", "Réseau de communication"]

# Combine all nodes
all_nodes = motivation_nodes + business_nodes + application_nodes + technology_nodes
G.add_nodes_from(all_nodes)

# Add edges (relationships)
edges = [
    ("Utilisateurs", "Collaboration efficace"),
    ("Collaboration efficace", "Améliorer la gestion de projets"),
    ("Améliorer la gestion de projets", "Projets livrés à temps"),
    ("Projets livrés à temps", "Intégration avec d'autres outils"),
    ("Chef de projet", "Membre de l'équipe"),
    ("Membre de l'équipe", "Création de projet"),
    ("Création de projet", "Assignation de tâches"),
    ("Assignation de tâches", "Tableau de bord analytique"),
    ("Tableau de bord analytique", "Notifications temps réel"),
    ("Application SaaS TeamFlow", "Gestion des projets"),
    ("Gestion des projets", "Interface utilisateur"),
    ("Interface utilisateur", "Service de chat intégré"),
    ("Service de chat intégré", "Données de projet"),
    ("Serveur cloud", "Service de sauvegarde"),
    ("Service de sauvegarde", "Réseau de communication"),
    ("Réseau de communication", "Données de projet"),
]
G.add_edges_from(edges)

# **Use Graphviz hierarchical layout**
pos = graphviz_layout(G, prog="dot")  # 'dot' makes it layered

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    edge_color="gray",
    node_size=3000,
    font_size=10,
    font_weight="bold",
    arrows=True,
)
plt.show()
