bodies = {'fields': [
    {'name': 'system_id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'system_relative_id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'sub_type', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'updated', 'type': 'DATETIME', 'mode': 'NULLABLE'},
    {'name': 'characteristics', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'atmosphere_type', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'distance', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'age', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'absolute_magnitude', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'gravity', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'radius', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'surface_temperature', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'landable', 'type': 'BOOL', 'mode': 'NULLABLE'},
        {'name': 'main_star', 'type': 'BOOL', 'mode': 'NULLABLE'},
        {'name': 'scoopable', 'type': 'BOOL', 'mode': 'NULLABLE'},
        {'name': 'terraforming_state', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'volcanism', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'earth_masses', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'surface_pressure', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'luminosity', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'solar_masses', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'solar_radius', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'spectral_class', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'reserve_level', 'type': 'STRING', 'mode': 'NULLABLE'},
    ]},
    {'name': 'belts', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'outer_radius', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'inner_radius', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'mass', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
    ]},
    {'name': 'rings', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'outer_radius', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'inner_radius', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'mass', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
    ]},
    {'name': 'composition', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
        {'name': 'element', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'percentage', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
    ]},
    {'name': 'materials', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'percentage', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
    ]},
    {'name': 'orbit', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'axial_tilt', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'orbital_inclination', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'orbital_period', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'rotational_period', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'periapsis', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'orbital_eccentricity', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'semi_major_axis', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'tidally_locked', 'type': 'BOOL', 'mode': 'NULLABLE'},
    ]},
    {'name': 'parents', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
        {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'system_relative_id', 'type': 'INT64', 'mode': 'NULLABLE'},
    ]},
]}

population = {'fields': [
    {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'current_state', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'security', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'population', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'economy', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'updated', 'type': 'DATETIME', 'mode': 'NULLABLE'},
    {'name': 'controlling_faction', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'allegiance', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'government', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'player_faction', 'type': 'BOOL', 'mode': 'NULLABLE'},
    ]},
    {'name': 'factions', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
        {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'allegiance', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'government', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'happiness', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'current_state', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'influence', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'player_faction', 'type': 'BOOL', 'mode': 'NULLABLE'},
        {'name': 'states', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [
            {'name': 'state', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
        ]},
    ]},
]}

powerplay = {'fields': [
    {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'allegiance', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'government', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'power', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'power_state', 'type': 'STRING', 'mode': 'NULLABLE'},
]}

stations = {'fields': [
    {'name': 'system_id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'market_id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'body', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'distance', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
    {'name': 'services', 'type': 'STRING', 'mode': 'REPEATED'},
    {'name': 'controlling_faction', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'allegiance', 'type': 'STRING', 'mode': 'NULLABLE'},
    ]},
    {'name': 'economy', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'primary', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'secondary', 'type': 'STRING', 'mode': 'NULLABLE'},
    ]},
    {'name': 'updated', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'information', 'type': 'DATETIME', 'mode': 'NULLABLE'},
        {'name': 'shipyard', 'type': 'DATETIME', 'mode': 'NULLABLE'},
        {'name': 'outfitting', 'type': 'DATETIME', 'mode': 'NULLABLE'},
        {'name': 'market', 'type': 'DATETIME', 'mode': 'NULLABLE'},
    ]},
]}

systems = {'fields': [
    {'name': 'id', 'type': 'INT64', 'mode': 'NULLABLE'},
    {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
    {'name': 'updated', 'type': 'DATETIME', 'mode': 'NULLABLE'},
    {'name': 'coordinates', 'type': 'RECORD', 'mode': 'NULLABLE', 'fields': [
        {'name': 'x', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'y', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'z', 'type': 'FLOAT64', 'mode': 'NULLABLE'},
        {'name': 'coordinates', 'type': 'STRING', 'mode': 'NULLABLE'},
    ]},  
]}