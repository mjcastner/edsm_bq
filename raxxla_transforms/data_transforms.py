import json


# TODO(mjcastner): Update all long lists of record statements to be sorted
# TODO(mjcastner): Add proper stackdriver logging


def transform_bodies(raw_bodies_json):
    raw_bodies_json = raw_bodies_json.rstrip(',')
    raw_bodies_json = raw_bodies_json.lstrip(' ')
    raw_bodies_json = str(raw_bodies_json)

    if raw_bodies_json == '[' or raw_bodies_json == ']':
        return
    else:
        raw_bodies_json = json.loads(raw_bodies_json)

        # Assemble belts
        belts = []
        raw_belts = raw_bodies_json.get('belts', None)

        if raw_belts:
            for raw_belt_record in raw_belts:
                belt_record = {
                    'name': raw_belt_record.get('name', None),
                    'type': raw_belt_record.get('type', None),
                    'outer_radius': raw_belt_record.get('outerRadius', None),
                    'inner_radius': raw_belt_record.get('innerRadius', None),
                    'mass': raw_belt_record.get('mass', None),
                }
                belts.append(belt_record)

        # Assemble characteristics
        characteristics = {
            'atmosphere_type': raw_bodies_json.get('atmosphereType', None),
            'absolute_magnitude': raw_bodies_json.get('absoluteMagnitude', None),
            'age': raw_bodies_json.get('age', None),
            'main_star': raw_bodies_json.get('isMainStar', None),
            'scoopable': raw_bodies_json.get('isScoopable', None),
            'distance': raw_bodies_json.get('distanceToArrival', None),
            'gravity': raw_bodies_json.get('gravity', None),
            'radius': raw_bodies_json.get('radius', None),
            'surface_temperature': raw_bodies_json.get('surfaceTemperature', None),
            'landable': raw_bodies_json.get('isLandable', None),
            'terraforming_state': raw_bodies_json.get('terraformingState', None),
            'volcanism': raw_bodies_json.get('volcanismType', None),
            'earth_masses': raw_bodies_json.get('earthMasses', None),
            'surface_pressure': raw_bodies_json.get('surfacePressure', None),
            'luminosity': raw_bodies_json.get('luminosity', None),
            'solar_masses': raw_bodies_json.get('solarMasses', None),
            'solar_radius': raw_bodies_json.get('solarRadius', None),
            'spectral_class': raw_bodies_json.get('spectralClass', None),
            'reserve_level': raw_bodies_json.get('reserveLevel', None),
        }

        # Assemble composition
        composition = []
        solid_composition = raw_bodies_json.get('solidComposition', None)
        atmosphere_composition = raw_bodies_json.get('atmosphereComposition', None)
        
        # TODO(mjcastner): Replace dict unpack with get()
        if solid_composition:
            for element, percentage in solid_composition.iteritems():
                composition_record = {
                    'element': element,
                    'percentage': percentage,
                    'type': 'Solid'
                }
                composition.append(composition_record)

        # TODO(mjcastner): Replace dict unpack with get()
        if atmosphere_composition:
            for element, percentage in atmosphere_composition.iteritems():
                composition_record = {
                    'element': element,
                    'percentage': percentage,
                    'type': 'Atmosphere'
                }
                composition.append(composition_record)

        # Assemble materials
        materials = []
        materials_raw = raw_bodies_json.get('materials', None)

        # TODO(mjcastner): Replace dict unpack with get()
        if materials_raw:
            for material, percentage in materials_raw.iteritems():
                material_record = {
                    'name': material,
                    'percentage': percentage
                }
                materials.append(material_record)

        # Assemble orbit
        orbit = {
            'axial_tilt': raw_bodies_json.get('axialTilt', None),
            'orbital_inclination': raw_bodies_json.get('orbitalInclination', None),
            'orbital_period': raw_bodies_json.get('orbitalPeriod', None),
            'rotational_period': raw_bodies_json.get('rotationalPeriod', None),
            'periapsis': raw_bodies_json.get('argOfPeriapsis', None),
            'orbital_eccentricity': raw_bodies_json.get('orbitalEccentricity', None),
            'semi_major_axis': raw_bodies_json.get('semiMajorAxis', None),
            'tidally_locked': raw_bodies_json.get('rotationalPeriodTidallyLocked', None),
        }

        # Assemble parents
        parents = []
        parents_raw = raw_bodies_json.get('parents', None)

        # TODO(mjcastner): Replace dict unpack with get()
        if parents_raw:
            for parent_record_raw in parents_raw:
                for parent_type, parent_id in parent_record_raw.iteritems():
                    parent_record = {
                        'type': parent_type,
                        'system_relative_id': parent_id
                    }
                    parents.append(parent_record)

        # Assemble rings
        rings = []
        raw_rings = raw_bodies_json.get('rings', None)

        if raw_rings:
            for raw_ring_record in raw_rings:
                ring_record = {
                    'name': raw_ring_record.get('name', None),
                    'type': raw_ring_record.get('type', None),
                    'outer_radius': raw_ring_record.get('outerRadius', None),
                    'inner_radius': raw_ring_record.get('innerRadius', None),
                    'mass': raw_ring_record.get('mass', None),
                }
                rings.append(ring_record)

        row = {
            'system_id': raw_bodies_json.get('systemId64', None),
            'id': raw_bodies_json.get('id64', None),
            'system_relative_id': raw_bodies_json.get('bodyId', None),
            'name': raw_bodies_json.get('name', None),
            'type': raw_bodies_json.get('type', None),
            'sub_type': raw_bodies_json.get('subType', None),
            'updated': raw_bodies_json.get('updateTime', None),
            'characteristics': characteristics,
            'composition': composition,
            'materials': materials,
            'orbit': orbit,
            'parents': parents,
            'belts': belts,
            'rings': rings,
        }

        return row


def transform_population(raw_population_json):
    raw_population_json = raw_population_json.rstrip(',')
    raw_population_json = raw_population_json.lstrip(' ')
    raw_population_json = str(raw_population_json)

    if raw_population_json == '[' or raw_population_json == ']':
        return
    else:
        raw_population_json = json.loads(raw_population_json)

        # Assemble controlling faction
        controlling_faction = {
            'id': raw_population_json.get('controllingFaction', {}).get('id', None),
            'name': raw_population_json.get('controllingFaction', {}).get('name', None),
            'allegiance': raw_population_json.get('controllingFaction', {}).get('allegiance', None),
            'government': raw_population_json.get('controllingFaction', {}).get('government', None),
            'player_faction': raw_population_json.get('controllingFaction', {}).get('isPlayer', None),
        }

        # Assemble factions
        factions = []
        raw_factions = raw_population_json.get('factions', None)

        if raw_factions:
            for raw_faction_record in raw_factions:
                
                # Assemble faction states
                states = []
                active_states = raw_faction_record.get('activeStates', None)
                pending_states = raw_faction_record.get('pendingStates', None)
                recovering_states = raw_faction_record.get('recoveringStates', None)

                for raw_state in [active_states, pending_states, recovering_states]:
                    if raw_state:
                        for raw_state_record in raw_state:
                            state_type = None
                            if raw_state == active_states:
                                state_type = 'Active'
                            elif raw_state == pending_states:
                                state_type = 'Pending'
                            elif raw_state == recovering_states:
                                state_type = 'Recovering'

                            state_record = {
                                'state': raw_state_record.get('state', None),
                                'type': state_type,
                            }
                            states.append(state_record)

                faction_record = {
                    'id': raw_faction_record.get('id', None),
                    'name': raw_faction_record.get('name', None),
                    'allegiance': raw_faction_record.get('allegiance', None),
                    'government': raw_faction_record.get('government', None),
                    'happiness': raw_faction_record.get('happiness', None),
                    'current_state': raw_faction_record.get('state', None),
                    'influence': raw_faction_record.get('influence', None),
                    'player_faction': raw_faction_record.get('isPlayer', None),
                    'states': states,
                }
                factions.append(faction_record)

        row = {
            'id': raw_population_json.get('id64', None),
            'current_state': raw_population_json.get('state', None),
            'security': raw_population_json.get('security', None),
            'population': raw_population_json.get('population', None),
            'economy': raw_population_json.get('economy', None),
            'updated': raw_population_json.get('date', None),
            'controlling_faction': controlling_faction,
            'factions': factions,
        }

        return row


def transform_powerplay(raw_powerplay_json):
    raw_powerplay_json = raw_powerplay_json.rstrip(',')
    raw_powerplay_json = raw_powerplay_json.lstrip(' ')
    raw_powerplay_json = str(raw_powerplay_json)

    if raw_powerplay_json == '[' or raw_powerplay_json == ']':
        return
    else:
        raw_powerplay_json = json.loads(raw_powerplay_json)

        row = {
            'id': raw_powerplay_json.get('id64', None),
            'allegiance': raw_powerplay_json.get('allegiance', None),
            'government': raw_powerplay_json.get('government', None),
            'power': raw_powerplay_json.get('power', None),
            'power_state': raw_powerplay_json.get('powerState', None),
        }

        return row


def transform_stations(raw_station_json):
    raw_station_json = raw_station_json.rstrip(',')
    raw_station_json = raw_station_json.lstrip(' ')
    raw_station_json = str(raw_station_json)

    if raw_station_json == '[' or raw_station_json == ']':
        return
    else:
        raw_station_json = json.loads(raw_station_json)

        # Assemble services field
        services = raw_station_json.get('otherServices', None)
        market = raw_station_json.get('haveMarket', False)
        outfitting = raw_station_json.get('haveOutfitting', False)
        shipyard = raw_station_json.get('haveShipyard', False)

        if market:
            services.append('Market')
        elif outfitting:
            services.append('Outfitting')
        elif shipyard:
            services.append('Shipyard')

        # Assemble factions record
        faction = {
            'id': raw_station_json.get('controllingFaction', {}).get('id', None),
            'name': raw_station_json.get('controllingFaction', {}).get('name', None),
            'allegiance': raw_station_json.get('allegiance', None),
        }

        # Assemble economy record
        economy = {
            'primary': raw_station_json.get('economy', None),
            'secondary': raw_station_json.get('secondEconomy', None),
        }

        # Assemble updated record
        updated = {
            'information': raw_station_json.get('updateTime', {}).get('information', None),
            'shipyard': raw_station_json.get('updateTime', {}).get('shipyard', None),
            'outfitting': raw_station_json.get('updateTime', {}).get('outfitting', None),
            'market': raw_station_json.get('updateTime', {}).get('market', None),
        }

        # Assemble return row
        row = {
            'system_id': raw_station_json.get('systemId64', None),
            'market_id': raw_station_json.get('marketId', None),
            'id': raw_station_json.get('id', None),
            'name': raw_station_json.get('name', None),
            'type': raw_station_json.get('type', None),
            'body': raw_station_json.get('body', {}).get('name', None),
            'distance': raw_station_json.get('distanceToArrival', None),
            'services': services,
            'controlling_faction': faction,
            'economy': economy,
            'updated': updated
        }
    
        return row


def transform_systems(raw_system_json):
    raw_system_json = raw_system_json.rstrip(',')
    raw_system_json = raw_system_json.lstrip(' ')
    raw_system_json = str(raw_system_json)

    if raw_system_json == '[' or raw_system_json == ']':
        return
    else:
        raw_system_json = json.loads(raw_system_json)

        # Assemble coordinates
        x_coords = raw_system_json.get('coords', {}).get('x', None)
        y_coords = raw_system_json.get('coords', {}).get('y', None)
        z_coords = raw_system_json.get('coords', {}).get('z', None)
        combined_coords = None

        if x_coords and y_coords and z_coords:
            combined_coords = str(x_coords) + ', ' + str(y_coords) + ', ' + str(z_coords)

        coordinates = {
            'x': x_coords,
            'y': y_coords,
            'z': z_coords,
            'coordinates': combined_coords,
        }

        row = {
            'id': raw_system_json.get('id64', None),
            'name': raw_system_json.get('name', None),
            'updated': raw_system_json.get('date', None),
            'coordinates': coordinates
        }

        return row