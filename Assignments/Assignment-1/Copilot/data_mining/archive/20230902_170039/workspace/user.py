from dataclasses import dataclass

@dataclass
class User:
    id: int
    dietary_preferences: list
    skill_level: str
