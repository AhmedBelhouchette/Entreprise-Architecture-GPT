import json
import xml.etree.ElementTree as ET

# Function to create a shape in Draw.io
def create_shape(parent, element_id, value, x, y, width=120, height=60, style=""):
    shape = ET.SubElement(parent, "mxCell", id=element_id, value=value, style=style, vertex="1")
    ET.SubElement(shape, "mxGeometry", x=str(x), y=str(y), width=str(width), height=str(height))
    return shape

# Function to create a connection in Draw.io
def create_connection(parent, connection_id, source, target, style=""):
    connection = ET.SubElement(parent, "mxCell", id=connection_id, style=style, edge="1", source=source, target=target)
    ET.SubElement(connection, "mxGeometry", relative="1")
    return connection

# ... (rest of the code remains the same)

# Function to map ArchiMate types to Draw.io styles
def get_style_for_element(element_type):
    styles = {
        # Motivation Layer
        "Stakeholder": "shape=ellipse;whiteSpace=wrap;html=1;",
        "Driver": "shape=rhombus;whiteSpace=wrap;html=1;",
        "Goal": "shape=ellipse;whiteSpace=wrap;html=1;",
        # Business Layer
        "Business Actor": "shape=rectangle;whiteSpace=wrap;html=1;",
        "Business Process": "rounded=1;whiteSpace=wrap;html=1;",
        "Business Service": "shape=rectangle;whiteSpace=wrap;html=1;",
        # Application Layer
        "Application Component": "shape=rectangle;whiteSpace=wrap;html=1;",
        "Application Service": "shape=rectangle;whiteSpace=wrap;html=1;",
        # Technology Layer
        "Node": "shape=rectangle;whiteSpace=wrap;html=1;",
        "Device": "shape=rectangle;whiteSpace=wrap;html=1;",
        # Default style
        "default": "shape=rectangle;whiteSpace=wrap;html=1;",
    }
    return styles.get(element_type, styles["default"])

# Function to map relationships to Draw.io styles
def get_style_for_relationship(relationship_type):
    styles = {
        "Composition": "endArrow=block;html=1;",
        "Aggregation": "endArrow=open;html=1;",
        "Assignment": "endArrow=classic;html=1;",
        "Influence": "endArrow=oval;html=1;",
        "Association": "endArrow=none;html=1;",
        "default": "endArrow=classic;html=1;",
    }
    return styles.get(relationship_type, styles["default"])

# Main function to convert JSON to Draw.io XML
def json_to_drawio(json_data, output_file="output.drawio"):
    # Parse JSON
    data = json.loads(json_data)

    # Create the root XML structure
    mxfile = ET.Element("mxfile", version="1.0", encoding="UTF-8")
    diagram = ET.SubElement(mxfile, "diagram", name="Page-1", id="12345")
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1050", dy="522", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169")
    root = ET.SubElement(mxGraphModel, "root")

    # Add root cells
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    # Track positions and IDs
    x, y = 100, 100
    element_positions = {}  # Stores positions of elements for connections

    # Add elements from JSON
    for layer in data["layers"]:
        for element in layer["elements"]:
            # Create a shape for each element
            style = get_style_for_element(element["type"])
            create_shape(root, element["id"], element["name"], x, y, style=style)
            element_positions[element["id"]] = (x, y)
            x += 150  # Adjust position for the next element

        # Add relationships
        for relationship in layer.get("element-relationship", []):
            # Example: Connect the first two elements in the layer
            if len(layer["elements"]) >= 2:
                source = layer["elements"][0]["id"]
                target = layer["elements"][1]["id"]
                style = get_style_for_relationship(relationship)
                create_connection(root, f"conn_{source}_{target}", source, target, style=style)

    # Save the XML to a .drawio file
    tree = ET.ElementTree(mxfile)
    tree.write(output_file, encoding="UTF-8", xml_declaration=True)

    print(f"Draw.io file '{output_file}' created successfully!")

# Example JSON data

json_data = '''
{
    "layers": [
        {
            "layer": "business",
            "elements": [
                {"id": "1", "type": "Business Actor", "name": "Customer", "description": "End user of the system"},
                {"id": "2", "type": "Business Process", "name": "Order Processing", "description": "Handles customer orders"}
            ],
            "element-relationship": ["Assignment"]
        },
        {
            "layer": "application",
            "elements": [
                {"id": "3", "type": "Application Component", "name": "Order Management System", "description": "Manages orders"}
            ],
            "element-relationship": ["Serving"]
        }
    ]
}
'''

# Convert JSON to Draw.io
json_to_drawio(json_data)