# ═══════════════════════════════════════════════════════
#  character.py — Abstract base class (OOP: Abstraction,
#                 Encapsulation, Magic Methods)
# ═══════════════════════════════════════════════════════

from abc import ABC, abstractmethod
from data import MAX_HP, MIN_DAMAGE, BOLD, RESET, GREEN, YELLOW, RED


class Character(ABC):
    """
    Abstract base class for all characters in the game.
    Demonstrates:
      - Abstraction  : abc.ABC + @abstractmethod
      - Encapsulation: _private attributes with @property accessors
      - Magic Methods: __str__, __repr__
    """

    def __init__(self, name: str, hp: int, attack_power: int):
        self._name: str         = name
        self._hp: int           = hp
        self._max_hp: int       = hp
        self._attack_power: int = attack_power

    # ── properties (encapsulation) ───────────────────────
    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, value)

    @property
    def max_hp(self) -> int:
        return self._max_hp

    @max_hp.setter
    def max_hp(self, value: int) -> None:
        self._max_hp = max(1, value)

    @property
    def attack_power(self) -> int:
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value: int) -> None:
        self._attack_power = max(1, value)

    # ── abstract methods (must be overridden) ────────────
    @abstractmethod
    def attack(self, target: "Character") -> int:
        """Deal damage to target. Returns damage dealt."""
        pass

    @abstractmethod
    def get_style_name(self) -> str:
        """Return the name of this character's fighting style."""
        pass

    # ── concrete shared methods ──────────────────────────
    def defend(self, incoming: int, reduction: int) -> int:
        """Reduce incoming damage by reduction. Returns final damage taken."""
        taken = max(MIN_DAMAGE, incoming - reduction)
        self._hp = max(0, self._hp - taken)
        return taken

    def heal(self, amount: int = 9999) -> int:
        """Restore HP up to max. Returns amount actually healed."""
        before   = self._hp
        self._hp = min(self._max_hp, self._hp + amount)
        return self._hp - before

    def full_heal(self) -> None:
        """Restore HP to full maximum."""
        self._hp = self._max_hp

    def is_alive(self) -> bool:
        return self._hp > 0

    def hp_bar(self, length: int = 20) -> str:
        filled = int((self._hp / self._max_hp) * length)
        bar    = "█" * filled + "░" * (length - filled)
        ratio  = self._hp / self._max_hp
        color  = GREEN if ratio > 0.5 else YELLOW if ratio > 0.25 else RED
        return f"{color}[{bar}]{RESET} {self._hp}/{self._max_hp}"

    # ── magic methods ────────────────────────────────────
    def __str__(self) -> str:
        return f"{BOLD}{self._name}{RESET} (HP: {self._hp}/{self._max_hp})"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self._name!r}, "
            f"hp={self._hp}, "
            f"attack_power={self._attack_power})"
        )
