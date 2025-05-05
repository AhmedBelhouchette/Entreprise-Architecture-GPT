from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "assistant",
            "content": "You are gonna receive a project description that we are willing to extract the different archimate layers . Our main focus is the application layer. The application contains different elements. Here are all of them : The different elements include Application Component (encapsulation of modular, replaceable functionality), Application Collaboration (aggregate of elements working together for collective behavior), Application Interface (access point for application services), Application Function (automated behavior performed by a component), Application Interaction (collective behavior by multiple components), Application Process (sequence of behaviors achieving a result), Application Event (application state change), Application Service (explicitly defined exposed behavior), and Data Object (data structured for automated processing).You are not meant to use all the elements, only those you are sure of "
        },
        {
            "role": "user",
            "content":"L’entreprise « FleetTrack » propose une plateforme de suivi et d’optimisation des flottes de véhicules, avec des capteurs GPS transmettant en temps réel la position et l’état des véhicules, une carte interactive pour les gestionnaires avec alertes en cas d’anomalies, un module d’optimisation des trajets basé sur le trafic et les contraintes, une application mobile pour les chauffeurs afin de recevoir des instructions et signaler des incidents, et un algorithme d’analyse des données générant des rapports pour les responsables logistiques."
        }
    ]
)

print(completion.choices[0].message.content)
