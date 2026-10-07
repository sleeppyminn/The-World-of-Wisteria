from data import ITEMS, GREEN, YELLOW, RESET, BOLD, DIM


class Item:

    def __init__(self, name: str):
        if name not in ITEMS:
            raise ValueError(f"Unknown item: {name!r}")
        data              = ITEMS[name]
        self._name: str   = name
        self._item_type   = data["type"]
        self._effect_value= data["value"]
        self._desc: str   = data["desc"]

    @property
    def name(self) -> str:
        return self._name

    @property
    def item_type(self) -> str:
        return self._item_type

    @property
    def effect_value(self) -> int:
        return self._effect_value

    @property
    def desc(self) -> str:
        return self._desc

    def use(self, target) -> str:
        t, v = self._item_type, self._effect_value

        if t == "heal":
            healed = target.heal(v)
            return f"{GREEN}Used {self._name}. Restored {healed} HP.{RESET}"

        elif t == "atk_up":
            target.temp_atk_up += v
            return f"{GREEN}Used {self._name}. ATK +{v} for this battle!{RESET}"

        elif t == "str_up":
            target._str += v
            return f"{GREEN}Used {self._name}. STR permanently +{v}!{RESET}"

        elif t == "spd_up":
            target._spd += v
            return f"{GREEN}Used {self._name}. SPD permanently +{v}!{RESET}"

        elif t == "end_up":
            target._end += v
            return f"{GREEN}Used {self._name}. END permanently +{v}!{RESET}"

        return f"{YELLOW}Used {self._name}. Nothing happened.{RESET}"

    def __str__(self) -> str:
        return f"{BOLD}{self._name}{RESET} — {DIM}{self._desc}{RESET}"

    def __repr__(self) -> str:
        return f"Item(name={self._name!r}, type={self._item_type!r}, value={self._effect_value})"
