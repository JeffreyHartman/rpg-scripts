import random
from . import random_event

SCENE_ADJUSTMENT_TABLE = [
    (1, "Remove a Character"),
    (2, "Add a Character"),
    (3, "Reduce/Remove an Activity"),
    (4, "Increase an Activity"),
    (5, "Remove an Object"),
    (6, "Add an Object"),
    (7, "Make 2 Adjustments"),
    (8, "Make 2 Adjustments"),
    (9, "Make 2 Adjustments"),
    (10, "Make 2 Adjustments")
]

def generate_scene_check(chaos_factor: int) -> str:
    """Generate a scene check result based on chaos factor."""
    die_roll = random.randint(1, 10)
    result = _check_scene(chaos_factor, die_roll)
    
    # If scene is altered or interrupted, add an adjustment
    if result == "Interrupt Scene!":
        event = random_event.generate_random_event()
        return f"Scene Check: {result} ({die_roll})\n{event}"
    if result == "Altered Scene!":
        adjustment = _generate_scene_adjustment()
        return f"Scene Check: {result} ({die_roll})\n{adjustment}"
    
    return f"Scene Check: {result} ({die_roll})"

def _generate_scene_adjustment() -> str:
    """Generate a scene adjustment."""
    die_roll = random.randint(1, 10)
    for pos, result in SCENE_ADJUSTMENT_TABLE:
        if die_roll == pos:
            return f"Scene Adjustment: {result}"
    return "Scene Adjustment: Invalid Roll"  # Should never happen with 1-10 roll

def _check_scene(chaos_factor: int, die_roll: int) -> str:
    """Internal function to determine scene check result."""
    if die_roll <= chaos_factor:
        return "Interrupt Scene!" if die_roll % 2 == 0 else "Altered Scene!"
    return "Normal Scene"
