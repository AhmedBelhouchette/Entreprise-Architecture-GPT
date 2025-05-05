import base64

# Step 1: Read the .drawio file and encode it in base64
file_path = "Green_Energy_Transition.drawio"  # Path to your .drawio file

with open(file_path, "rb") as file:
    file_content = file.read()

# Base64 encode the content of the .drawio file
encoded_content = base64.b64encode(file_content).decode('utf-8')

# Step 2: Create an HTML file with embedded Draw.io iframe using base64 content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embedded ArchiMate Model in Draw.io</title>
</head>
<body>
    <h1>Embedded ArchiMate Diagram</h1>
    <p>This diagram is embedded using Draw.io Embed Mode.</p>
    
    <iframe src="https://embed.diagrams.net/?embed=1&base64={encoded_content}"
            width="100%" height="600px" frameborder="0"></iframe>
    
</body>
</html>
"""

# Step 3: Write the HTML content to an HTML file
html_file_name = 'embedded_archimate_model_drawio.html'

with open(html_file_name, 'w') as html_file:
    html_file.write(html_content)

print(f"HTML file '{html_file_name}' created successfully!")
