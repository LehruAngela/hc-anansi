min_time = 60
max_time = 5184000
check = {
    "properties": {
        "name": {"type": "string"},
        "tags": {"type": "string"},
<<<<<<< HEAD
        "timeout": {"type": "number", "minimum": min_time, "maximum": max_time},
        "grace": {"type": "number", "minimum": min_time, "maximum": max_time},
        "nag": {"type": "number", "minimum": min_time, "maximum": max_time},
=======
        "timeout": {"type": "number", "minimum": 60, "maximum": 5184000},
        "grace": {"type": "number", "minimum": 60, "maximum": 5184000},
>>>>>>> Ft increase timeouts and grace periods #153727847 (#20)
        "channels": {"type": "string"}
    }
}
