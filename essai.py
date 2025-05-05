from openai import OpenAI
import json

system_prompt = "You are an archimate expert. Generate structured JSON output for an ArchiMate model, covering all existing layers. ONLY EXISTING LAYERS SHALL BE INCLUDED. You will receive an enterprise description from the user and you should turn it into the json format given to you."

user_prompt = "L’entreprise « FleetTrack » propose une plateforme de suivi et d’optimisation des flottes de véhicules, avec des capteurs GPS transmettant en temps réel la position et l’état des véhicules, une carte interactive pour les gestionnaires avec alertes en cas d’anomalies, un module d’optimisation des trajets basé sur le trafic et les contraintes, une application mobile pour les chauffeurs afin de recevoir des instructions et signaler des incidents, et un algorithme d’analyse des données générant des rapports pour les responsables logistiques."

client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-4o-mini",  # Use a valid model name
    temperature=0,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    functions=[
        {
            "name": "generate_archimate_model",
            "description": "Generates structured JSON data for an ArchiMate model covering multiple layers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "layers": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "layer": {
                                    "type": "string",
                                    "enum": ["motivation", "strategy", "business", "application", "technology"]
                                },
                                "elements": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string"},
                                            "type": {"type": "string"},
                                            "name": {"type": "string"},
                                            "description": {"type": "string"}
                                        },
                                        "required": ["id", "type", "name"]
                                    }
                                },
                                "element-relationship": {
                                    "type": "array",
                                    "items": {
                                        "enum":[
                                                "Composition",
                                                "Aggregation",
                                                "Assignment",
                                                "Realization",
                                                "Serving",
                                                "Access",
                                                "Influence",
                                                "Association",
                                                "Triggering",
                                                "Flow",
                                                "Specialization",
                                                "Junction"
                                                ],
                                        "properties": {
                                            "from": {"type": "string"},
                                            "to": {"type": "string"},
                                            "type": {"type": "string"}
                                        },
                                        "required": ["from", "to", "type"]
                                    }
                                }
                            },
                            "required": ["layer", "elements", "element-relationship"]
                        }
                    }
                },
                "required": ["layers"]
            }
        }
    ],
    function_call={"name": "generate_archimate_model"}  # Force the model to use the function
)

# Extract the function arguments from the response
if completion.choices[0].message.function_call:
    structured_json = completion.choices[0].message.function_call.arguments
    print(json.dumps(json.loads(structured_json), indent=4))
else:
    print("No function call found in the response.")