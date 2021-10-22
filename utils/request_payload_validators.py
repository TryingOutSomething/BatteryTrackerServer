def is_within_valid_battery_range(battery_level: str) -> bool:
    if not battery_level.isdigit():
        return False

    return 0 <= int(battery_level) <= 100


def is_empty_field(field: str) -> bool:
    return not field or not field.strip()
