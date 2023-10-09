from dataclasses import dataclass

@dataclass
class Recipe:
    id: int
    name: str
    ingredients: list
    instructions: str
    dietary_preferences: list
    skill_level: str
