formattt=[
    {
"name": "generate_archimate_model",
"description": "Generates structured JSON data for an ArchiMate model covering multiple layers.",
"parameters": {
    "type": "object",
    "properties": {
        "layers": {
            "type": "array",
            "items": {
                "oneOf": [
                    {
                        "title": "Motivation Layer",
                        "type": "object",
                        "properties": {
                            "layer": {"const": "motivation"},
                            "elements": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "type": {
                                            "type": "string",
                                            "enum": [
                                                "Stakeholder",
                                                "Driver",
                                                "Assessment",
                                                "Goal",
                                                "Outcome",
                                                "Principle",
                                                "Requirement",
                                                "Constraint",
                                                "Meaning",
                                                "Value",
                                            ],
                                        },
                                        "name": {"type": "string"},
                                        "description": {"type": "string"},
                                    },
                                    "required": ["id", "type", "name"],
                                },
                            },
                            "element-relationship": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties":{
                                        "from": {"type": "string"},
                                        "to": {"type": "string"},
                                        "type":{
                                            "type": "string",
                                            "enum": [
                                        "Composition",
                                        "Aggregation",
                                        "Assignment",
                                        "Influence",
                                        "Association",
                                    ]
                                        }
                                    
                                
                                }, 
                                "required": ["from", "to", "type"]
                            },
                            },
                        },
                            "required": ["layer", "elements", "element-relationship"]
                    
                    },
                    {
                        "title": "Strategy Layer",
                        "type": "object",
                        "properties": {
                            "layer": {"const": "strategy"},
                            "elements": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "type": {
                                            "type": "string",
                                            "enum": [
                                                "Resource",
                                                "Capability",
                                                "Course of Action",
                                                "Value",
                                            ],
                                        },
                                        "name": {"type": "string"},
                                        "description": {"type": "string"},
                                    },
                                    "required": ["id", "type", "name"],
                                },
                            },
                            "element-relationship": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties":{
                                        "from": {"type": "string"},
                                        "to": {"type": "string"},
                                        "type":{
                                            "type": "string",
                                            "enum": [
                                                "Composition",
                                                "Aggregation",
                                                "Assignment",
                                                "Association",
                                    ]
                                        }
                                    
                                
                                }, 
                                "required": ["from", "to", "type"]
                            },
                            },
                        },
                            "required": ["layer", "elements", "element-relationship"],
                    },
                    {
                        "title": "Business Layer",
                        "type": "object",
                        "properties": {
                            "layer": {"const": "business"},
                            "elements": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "type": {
                                            "type": "string",
                                            "enum": [
                                                "Business Actor",
                                                "Business Role",
                                                "Business Collaboration",
                                                "Business Interface",
                                                "Business Process",
                                                "Business Function",
                                                "Business Interaction",
                                                "Business Event",
                                                "Business Service",
                                                "Business Object",
                                                "Contract",
                                                "Representation",
                                                "Product",
                                            ],
                                        },
                                        "name": {"type": "string"},
                                        "description": {"type": "string"},
                                    },
                                    "required": ["id", "type", "name"],
                                },
                            },
                            "element-relationship": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties":{
                                        "from": {"type": "string"},
                                        "to": {"type": "string"},
                                        "type":{
                                            "type": "string",
                                            "enum": [
                                                "Composition",
                                                "Aggregation",
                                                "Assignment",
                                                "Serving",
                                                "Access",
                                                "Association",
                                                "Triggering",
                                                "Flow",
                                                "Specialization",
                                    ]
                                        }
                                    
                                
                                }, 
                                "required": ["from", "to", "type"]
                            },
                            },
                        },
                            "required": ["layer", "elements", "element-relationship"],
                    },
                    {
                        "title": "Application Layer",
                        "type": "object",
                        "properties": {
                            "layer": {"const": "application"},
                            "elements": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "type": {
                                            "type": "string",
                                            "enum": [
                                                "Application Component",
                                                "Application Collaboration",
                                                "Application Interface",
                                                "Application Function",
                                                "Application Interaction",
                                                "Application Process",
                                                "Application Event",
                                                "Application Service",
                                                "Data Object",
                                            ],
                                        },
                                        "name": {"type": "string"},
                                        "description": {"type": "string"},
                                    },
                                    "required": ["id", "type", "name"],
                                },
                            },
                            "element-relationship": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties":{
                                        "from": {"type": "string"},
                                        "to": {"type": "string"},
                                        "type":{
                                            "type": "string",
                                            "enum": [
                                                "Composition",
                                                "Aggregation",
                                                "Assignment",
                                                "Serving",
                                                "Access",
                                                "Association",
                                                "Triggering",
                                                "Flow",
                                                "Specialization",
                                    ]
                                        }
                                    
                                
                                }, 
                                "required": ["from", "to", "type"]
                            },
                            },
                        },
                            "required": ["layer", "elements", "element-relationship"],
                    },
                    {
                        "title": "Technology Layer",
                        "type": "object",
                        "properties": {
                            "layer": {"const": "technology"},
                            "elements": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "type": {
                                            "type": "string",
                                            "enum": [
                                                "Node",
                                                "Device",
                                                "System Software",
                                                "Technology Collaboration",
                                                "Technology Interface",
                                                "Path",
                                                "Communication Network",
                                                "Technology Function",
                                                "Technology Process",
                                                "Technology Interaction",
                                                "Technology Event",
                                                "Technology Service",
                                                "Artifact",
                                            ],
                                        },
                                        "name": {"type": "string"},
                                        "description": {"type": "string"},
                                    },
                                    "required": ["id", "type", "name"],
                                },
                            },
                            "element-relationship": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties":{
                                        "from": {"type": "string"},
                                        "to": {"type": "string"},
                                        "type":{
                                            "type": "string",
                                            "enum": [
                                                "Composition",
                                                "Aggregation",
                                                "Assignment",
                                                "Serving",
                                                "Access",
                                                "Association",
                                                "Triggering",
                                                "Flow",
                                                "Specialization",
                                    ]
                                        }
                                    
                                
                                }, 
                                "required": ["from", "to", "type"]
                            },
                            },
                        },
                            "required": ["layer", "elements", "element-relationship"],
                    },
                ]
            },
        }
    },
    "required": ["layers"],
},
}
]