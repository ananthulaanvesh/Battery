def calculate_pack(cell_voltage, cell_capacity, series, parallel):
    pack_voltage = cell_voltage * series
    pack_capacity = cell_capacity * parallel
    pack_energy = pack_voltage * pack_capacity / 1000  # kWh

    return {
        "voltage": pack_voltage,
        "capacity": pack_capacity,
        "energy": pack_energy
    }