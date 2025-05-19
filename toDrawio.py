import json
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def safe_id(element_id):
    """Prefix user IDs to avoid conflicts with Draw.io's reserved IDs (0 and 1)."""
    return f"elem_{element_id}"





def get_style_for_element(element_type):
    """Map ArchiMate element types to proper Draw.io ArchiMate styles."""

    styles = {
        # Motivation Layer (purple)
        # "Stakeholder": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=stakeholder;archiType=rounded;",
        # "Driver": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=driver;archiType=oct;",
        # "Assessment": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=assessment;archiType=oct;",
        # "Goal": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=goal;archiType=oct;",
        # "Outcome": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=outcome;archiType=oct;",
        # "Principle": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=principle;archiType=oct;",
        # "Requirement": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=requirement;archiType=square;",
        # "Constraint": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=constraint;archiType=square;",
        # "Meaning": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=meaning;archiType=rounded;",
       
        # "Value": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.motivation;appType=value;archiType=square;",
        # Motivation Layer (purple with working icons)
        "Stakeholder": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=role;archiType=oct;",
        "Driver": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=driver;archiType=oct;",
        "Assessment": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=assess;archiType=oct;",
        "Goal": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=goal;archiType=oct;",
        "Outcome": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=outcome;archiType=oct;",
        "Principle": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=principle;archiType=oct;",
        "Requirement": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=requirement;archiType=oct;",
        "Constraint": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=constraint;archiType=oct;",
        "Meaning": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=meaning;archiType=oct;",
        "Value": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#CCCCFF;shape=mxgraph.archimate3.application;appType=amValue;archiType=oct;",

        # Business Layer (yellow)
        "Business Actor": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=actor;archiType=square;",
        "Business Role": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=role;archiType=square;",
        "Business Collaboration": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=collab;archiType=square;",
        "Business Interface": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=interface;archiType=square;",
        "Business Process": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=proc;archiType=rounded;",
        "Business Function": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=func;archiType=rounded;",
        "Business Interaction": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=interact;archiType=rounded;",
        "Business Event": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=event;archiType=circle;",
        "Business Service": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;",
        "Business Object": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=passive;archiType=square;",
        "Contract": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=contract;archiType=square;",
        "Representation": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=repres;archiType=square;",
        "Product": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFF99;shape=mxgraph.archimate3.application;appType=product;archiType=square;",
        # Application Layer (cyan)
        "Application Component": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=comp;archiType=square;",
        "Application Collaboration": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=collab;archiType=square;",
        "Application Interface": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=interface;archiType=square;",
        "Application Function": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=func;archiType=rounded;",
        "Application Interaction": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=interact;archiType=rounded;",
        "Application Process": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=proc;archiType=rounded;",
        "Application Event": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=event;archiType=circle;",
        "Application Service": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;",
        "Data Object": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#99ffff;shape=mxgraph.archimate3.application;appType=passive;archiType=square;",
        # Technology Layer (green)
        "Node": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=node;archiType=square;",
        "Device": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=device;archiType=square;",
        "System Software": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=sysSw;archiType=square;",
        "Technology Collaboration": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=collab;archiType=square;",
        "Technology Interface": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=interface;archiType=square;",
        "Path": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=path;archiType=rounded;",
        "Communication Network": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=netw;archiType=square;",
        "Technology Function": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=func;archiType=rounded;",
        "Technology Process": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=proc;archiType=rounded;",
        "Technology Interaction": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=interact;archiType=rounded;",
        "Technology Event": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=event;archiType=circle;",
        "Technology Service": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;",
        "Artifact": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#AFFFAF;shape=mxgraph.archimate3.application;appType=artifact;archiType=square;",
        # strategy layer
        "Resource": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#F5DEAA;shape=mxgraph.archimate3.application;appType=resource;archiType=square;",
        "Capability": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#F5DEAA;shape=mxgraph.archimate3.application;appType=capability;archiType=square;",
        "Course of Action": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#F5DEAA;shape=mxgraph.archimate3.application;appType=course;archiType=rounded;",
        "Value": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#F5DEAA;shape=mxgraph.archimate3.application;appType=value;archiType=square;",
        # Default style
        "default": "html=1;outlineConnect=0;whiteSpace=wrap;fillColor=#FFFFFF;shape=mxgraph.archimate3.rectangle;",
    }
    return styles.get(element_type, styles["default"])


def get_style_for_relationship(relationship_type):
    """Map ArchiMate relationship types to proper Draw.io ArchiMate arrow styles."""
    styles = {
        "Influence": "html=1;shape=mxgraph.archimate3.relationship;archiType=influence;",
        "Assignment": "html=1;shape=mxgraph.archimate3.relationship;archiType=assignment;",
        "Triggering": "html=1;shape=mxgraph.archimate3.relationship;archiType=triggering;",
        "Serving": "html=1;shape=mxgraph.archimate3.relationship;archiType=serving;",
        "Access": "html=1;shape=mxgraph.archimate3.relationship;archiType=access;",
        "default": "html=1;shape=mxgraph.archimate3.relationship;archiType=association;",
    }
    return styles.get(relationship_type, styles["default"])




def create_shape(parent, element_id, value, x, y, width=120, height=60, style=""):
    """Create a Draw.io shape element with proper geometry and parent."""
    shape = ET.SubElement(
        parent,
        "mxCell",
        {
            "id": element_id,
            "value": escape(value),
            "style": style,
            "vertex": "1",
            "parent": "1",  # Critical: Makes the shape visible
        },
    )
    ET.SubElement(
        shape,
        "mxGeometry",
        {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry",
        },
    )
    return shape


def create_connection(parent, connection_id, source, target, style=""):
    """Create a Draw.io connection between elements."""
    connection = ET.SubElement(
        parent,
        "mxCell",
        {
            "id": connection_id,
            "style": style,
            "edge": "1",
            "source": source,
            "target": target,
            "parent": "1",  # Critical: Makes the connection visible
        },
    )
    ET.SubElement(connection, "mxGeometry", {"relative": "1", "as": "geometry"})
    return connection


# def calculate_layout(layers,dis="dot"):
#     """Calculate optimal positions for elements using pygraphviz for better layout"""
#     layout_config = {
#         "layer_spacing": 500,  # Increased from 400
#         "node_spacing": 1000,   # Increased from 200
#         "margin": 200,
#         "node_width": 150,
#         "node_height": 75,
#     }
#     try:
#         import pygraphviz
#         HAS_PYGRAPHVIZ = True
#     except (ImportError, AttributeError):
#         HAS_PYGRAPHVIZ = False
#     all_positions = {}
#     current_y = layout_config["margin"]

#     for layer_idx, layer in enumerate(layers):
#         G = nx.DiGraph()

#         # Add nodes
#         for element in layer["elements"]:
#             G.add_node(element["id"])

#         # Add edges
#         for rel in layer.get("element-relationship", []):
#             G.add_edge(rel["from"], rel["to"])

#         # Convert to pygraphviz for better layout
#         try:
#             A = nx.nx_agraph.to_agraph(G)
#             A.graph_attr.update(
#                 rankdir="TB", splines="true", nodesep="0.5", ranksep="1.0"
#             )
#             A.node_attr.update(shape="rectangle", fixedsize="false")

#             # Use dot layout (hierarchical)
#             A.layout(prog=dis)

#             # Extract positions
#             for node in G.nodes():
#                 pos = A.get_node(node).attr["pos"]
#                 if pos:
#                     x, y = map(float, pos.split(","))
#                     # Adjust coordinates to our system
#                     adjusted_x = x + layout_config["margin"]
#                     adjusted_y = current_y + y
#                     all_positions[(layer_idx, node)] = (adjusted_x, adjusted_y)

#         except Exception as e:
#             print(
#                 f"Warning: pygraphviz layout failed, falling back to spring layout. Error: {e}"
#             )
#             # Fallback to spring layout if pygraphviz fails
#             pos = nx.spring_layout(
#                 G, k=layout_config["node_spacing"] / 50, iterations=100
#             )

#             # Normalize and scale coordinates
#             if pos:
#                 min_x = min(v[0] for v in pos.values())
#                 max_x = max(v[0] for v in pos.values())
#                 min_y = min(v[1] for v in pos.values())
#                 max_y = max(v[1] for v in pos.values())

#                 x_range = max_x - min_x if (max_x - min_x) > 0 else 1
#                 y_range = max_y - min_y if (max_y - min_y) > 0 else 1

#                 for node in pos:
#                     x = ((pos[node][0] - min_x) / x_range) * layout_config[
#                         "node_spacing"
#                     ] * (len(pos) - 1) + layout_config["margin"]
#                     y = ((pos[node][1] - min_y) / y_range) * layout_config[
#                         "node_spacing"
#                     ] + current_y
#                     all_positions[(layer_idx, node)] = (x, y)

#         current_y += layout_config["node_spacing"] + layout_config["layer_spacing"]

#     return all_positions

# The prog='dot' argument tells it which Graphviz layout engine to use.

# Here are the main ones:

# Engine	Algorithm Type	Best For
# dot	Hierarchical layout	Directed graphs, trees, DAGs
# neato	Spring (force-directed)	Undirected graphs
# fdp	Force-directed	Undirected graphs (larger)
# sfdp	Scalable force-directed	Very large undirected graphs
# twopi	Radial layout	Graphs with a central node
# circo	Circular layout	Cyclic or circular structures
import math
import networkx as nx

def calculate_layout(layers_data, engine="dot"):
    """
    Compute (x, y) positions for ArchiMate elements for draw.io visualization.

    Args:
        layers_data: List of layer dicts with 'elements' and 'element-relationship'
        engine: Ignored, for compatibility

    Returns:
        Dict with keys (layer_idx, element_id) -> (x, y)
    """
    positions = {}
    current_y = 70  # Initial margin
    
    # Layout configuration
    horizontal_spacing = 180
    vertical_spacing = 150
    margin = 70
    min_layer_height = 200
    
    for layer_idx, layer in enumerate(layers_data):
        G = nx.DiGraph()

        # Add elements
        for element in layer.get("elements", []):
            G.add_node(element["id"])

        # Add relationships
        for rel in layer.get("element-relationship", []):
            G.add_edge(rel["from"], rel["to"])

        pos = {}
        try:
            if G.number_of_nodes() > 0:
                # Determine if graph is complex
                is_complex = False
                try:
                    cycles = list(nx.simple_cycles(G))
                    if cycles:
                        is_complex = True
                except:
                    pass
                    
                if not is_complex:
                    roots = [n for n in G.nodes() if G.in_degree(n) == 0]
                    if len(roots) > 1 or any(G.out_degree(n) > 2 for n in G.nodes()):
                        is_complex = True
                
                # Select appropriate layout parameters
                if is_complex or G.number_of_nodes() > 10:
                    width = max(5.0, len(G.nodes) * 0.7)
                    vert_gap = 1.0
                else:
                    width = max(3.0, len(G.nodes) * 0.6)
                    vert_gap = 1.5
                
                # Find root nodes for hierarchy
                roots = [n for n in G.nodes() if G.in_degree(n) == 0]
                if not roots:
                    # If no root nodes found, use node with highest out_degree
                    roots = [sorted(G.nodes(), key=lambda n: G.out_degree(n), reverse=True)[0]]
                
                # For multiple roots, create a virtual root
                virtual_root_added = False
                if len(roots) > 1:
                    G.add_node("_virtual_root")
                    for r in roots:
                        G.add_edge("_virtual_root", r)
                    root = "_virtual_root"
                    virtual_root_added = True
                else:
                    root = roots[0]
                
                # Calculate hierarchical positions
                visited = set()
                pos = {}
                
                def _hierarchy_pos(G, node, left, right, vert_loc, xcenter, pos, visited):
                    pos[node] = (xcenter, vert_loc)
                    visited.add(node)
                    
                    # Get unvisited children
                    children = [n for n in G.successors(node) if n not in visited]
                    
                    if not children:
                        return pos
                    
                    # Calculate child spacing
                    dx = (right - left) / len(children)
                    dx = max(dx, width * 0.1 / max(1, len(G.nodes) - 1))  # Minimum spacing
                    
                    nextx = left
                    for child in children:
                        if child not in visited:
                            # Give more space to nodes with children
                            child_width = dx * (1 if G.out_degree(child) == 0 else 1.5)
                            pos = _hierarchy_pos(G, child, 
                                              nextx, nextx + child_width,
                                              vert_loc - vert_gap, 
                                              nextx + child_width/2,
                                              pos, visited)
                        nextx += dx
                    
                    return pos
                
                # Start hierarchy positioning from root
                pos = _hierarchy_pos(G, root, 0, width, 0, width/2, {}, visited)
                
                # Remove virtual root if added
                if virtual_root_added and "_virtual_root" in pos:
                    del pos["_virtual_root"]

            # Calculate layer dimensions
            max_y_in_layer = 0
            max_x_in_layer = 0
            
            for node in G.nodes():
                if node in pos:
                    x, y = pos[node]
                    max_y_in_layer = max(max_y_in_layer, -y)
                    max_x_in_layer = max(max_x_in_layer, x)

            # Apply positions with adjusted spacing
            for node in G.nodes():
                if node in pos:
                    x, y = pos[node]
                else:
                    # Handle any nodes not positioned by the algorithm
                    x = (len(positions) % 5) * 0.2
                    y = 0
                
                # Scale positions to actual spacing values
                adjusted_x = x * horizontal_spacing + margin
                adjusted_y = -y * vertical_spacing + current_y
                
                positions[(layer_idx, node)] = (adjusted_x, adjusted_y)

            # Calculate layer height, ensuring minimum height
            layer_height = max(
                min_layer_height,
                (max_y_in_layer + 1) * vertical_spacing
            )
            current_y += layer_height + margin

        except Exception as e:
            print(f"[Warning] Layout failed for layer {layer_idx}: {e}")

    return positions




def json_to_drawio(json_data, output_file,display="dot"):
    """Convert ArchiMate JSON to a fully valid Draw.io XML file with proper positioning."""
    data = json.loads(json_data)

    # Calculate optimized positions
    all_positions = calculate_layout(data["layers"],display)

    # Initialize Draw.io XML structure
    mxfile = ET.Element("mxfile", {"version": "1.0", "encoding": "UTF-8"})
    diagram = ET.SubElement(
        mxfile, "diagram", {"name": "ArchiMate Model", "id": "archimate_diagram"}
    )
    mxGraphModel = ET.SubElement(
        diagram,
        "mxGraphModel",
        {"dx": "1050", "dy": "522", "grid": "1", "gridSize": "10"},
    )
    root = ET.SubElement(mxGraphModel, "root")

    # Mandatory root cells (Draw.io requirement)
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})  # Default layer

    # Track element IDs (no need for manual x/y tracking)
    element_map = {}

    # Process each layer
    for layer_idx, layer in enumerate(data["layers"]):
        # Add layer label (position at the top-center of the layer)
        layer_label_id = f"label_{layer['layer'].replace(' ', '_')}"
        layer_nodes = [elem["id"] for elem in layer["elements"]]
        
        # Calculate layer label position (center of the layer)
        if layer_nodes:
            x_positions = [all_positions[(layer_idx, node)][0] for node in layer_nodes]
            layer_center_x = (min(x_positions) + max(x_positions)) / 2
            layer_top_y = min([all_positions[(layer_idx, node)][1] for node in layer_nodes]) - 80
        else:
            layer_center_x, layer_top_y = 100, 100 + (400 * layer_idx)

        create_shape(
            parent=root,
            element_id=layer_label_id,
            value=layer["layer"],
            x=layer_center_x - 100,  # Center the label
            y=layer_top_y,
            width=200,
            height=30,
            style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];",
        )

        # Add elements using calculated positions
        for element in layer["elements"]:
            elem_id = safe_id(element["id"])
            style = get_style_for_element(element["type"])
            
            # Get pre-calculated position
            pos_x, pos_y = all_positions.get((layer_idx, element["id"]), (100, 100 + (400 * layer_idx)))
            
            create_shape(
                root, 
                elem_id, 
                element["name"], 
                x=pos_x, 
                y=pos_y, 
                style=style
            )
            element_map[element["id"]] = elem_id

        # Add relationships
        for rel in layer.get("element-relationship", []):
            source_id = element_map.get(rel["from"])
            target_id = element_map.get(rel["to"])
            
            if source_id and target_id:  # Only create if both elements exist
                style = get_style_for_relationship(rel["type"])
                create_connection(
                    root, 
                    f"conn_{source_id}_{target_id}", 
                    source_id, 
                    target_id, 
                    style=style
                )

    # Save to file
    tree = ET.ElementTree(mxfile)
    tree.write(output_file, encoding="UTF-8", xml_declaration=True)
    # print(f"Draw.io file successfully generated: '{output_file}'")
    return output_file
