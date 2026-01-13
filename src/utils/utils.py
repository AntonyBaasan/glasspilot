def comma_list_parser(raw_value: str) -> list[str]:
    """Converts a comma-separated string into a list of stripped strings."""
    # Split the raw string by commas and strip leading/trailing whitespace from each item
    return [item.strip() for item in raw_value.split(",")]
