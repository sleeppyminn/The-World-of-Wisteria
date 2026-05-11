# ═══════════════════════════════════════════════════════
#  data.py — All game constants, styles, story, items
# ═══════════════════════════════════════════════════════

# ── ANSI COLORS ─────────────────────────────────────────
RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
CYAN    = "\033[36m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
MAGENTA = "\033[35m"
WHITE   = "\033[37m"
BLUE    = "\033[34m"

# ── CONSTANTS ────────────────────────────────────────────
MAX_HP          = 100
EXP_PER_LEVEL   = 50        # exp needed to level up
LEVEL_HP_BONUS  = 15        # HP increase per level-up
LEVEL_ATK_BONUS = 3         # ATK increase per level-up
MIN_DAMAGE      = 1
TRAIN_CAP       = 5

# ── CLANS ────────────────────────────────────────────────
CLAN_POOL = {
    # ── Common ───────────────────────────────────────────
    "Yamamoto":    {"rarity": "Common",    "stats": (2,  2,  3)},
    "Suzuki":      {"rarity": "Common",    "stats": (3,  1,  3)},
    "Hasegawa":    {"rarity": "Common",    "stats": (2,  3,  2)},
    "Nakamura":    {"rarity": "Common",    "stats": (1,  2,  4)},
    "Inoue":       {"rarity": "Common",    "stats": (3,  2,  2)},
    "Fujiwara":    {"rarity": "Common",    "stats": (2,  1,  4)},
    # ── Uncommon ─────────────────────────────────────────
    "Kaneki":      {"rarity": "Uncommon",  "stats": (3,  4,  3)},
    "Nakahara":    {"rarity": "Uncommon",  "stats": (4,  3,  3)},
    "Takada":      {"rarity": "Uncommon",  "stats": (3,  3,  4)},
    "Terauchi":    {"rarity": "Uncommon",  "stats": (4,  2,  4)},
    # ── Rare ─────────────────────────────────────────────
    "Haganezuka":  {"rarity": "Rare",      "stats": (5,  4,  6)},
    "Kanamori":    {"rarity": "Rare",      "stats": (4,  5,  6)},
    "Kanzaki":     {"rarity": "Rare",      "stats": (5,  6,  4)},
    "Ubuyashiki":  {"rarity": "Rare",      "stats": (4,  7,  5)},
    "Urokodaki":   {"rarity": "Rare",      "stats": (6,  4,  5)},
    # ── Legendary ────────────────────────────────────────
    "Rengoku":     {"rarity": "Legendary", "stats": (7,  3,  5)},
    "Uzui":        {"rarity": "Legendary", "stats": (6,  6,  5)},
    "Hashibira":   {"rarity": "Legendary", "stats": (8,  3,  7)},
    "Agatsuma":    {"rarity": "Legendary", "stats": (5,  8,  4)},
    "Tokito":      {"rarity": "Legendary", "stats": (4,  9,  4)},
    "Tomioka":     {"rarity": "Legendary", "stats": (5,  7,  6)},
    "Kocho":       {"rarity": "Legendary", "stats": (3,  9,  5)},
    "Sabito":      {"rarity": "Legendary", "stats": (6,  6,  6)},
    "Shinazugawa": {"rarity": "Legendary", "stats": (8,  5,  6)},
    "Tamayo":      {"rarity": "Legendary", "stats": (4,  7,  7)},
    "Iguro":       {"rarity": "Legendary", "stats": (6,  7,  5)},
    "Kanroji":     {"rarity": "Legendary", "stats": (5,  7,  6)},
    # ── Mythic ───────────────────────────────────────────
    "Yoriichi":    {"rarity": "Mythic",    "stats": (14, 12, 10)},
    "Tsugikuni":   {"rarity": "Mythic",    "stats": (12, 10, 12)},
    "Kamado":      {"rarity": "Mythic",    "stats": (10, 10, 11)},
    "Himejima":    {"rarity": "Mythic",    "stats": (10, 8,  14)},
    # ── Secret ───────────────────────────────────────────
    "Yoo":         {"rarity": "Secret",    "stats": (15, 18, 15)},
    "Tolentino":   {"rarity": "Secret",    "stats": (17, 16, 16)},
    "Nona":        {"rarity": "Secret",    "stats": (18, 15, 17)},
}

RARITY_COLORS = {
    "Common":    WHITE,
    "Uncommon":  GREEN,
    "Rare":      CYAN,
    "Legendary": YELLOW,
    "Mythic":    MAGENTA,
    "Secret":    CYAN,
}

RARITY_WEIGHTS = {
    "Common":    40,
    "Uncommon":  25,
    "Rare":      18,
    "Legendary": 13,
    "Mythic":     4,
    "Secret":     1,
}



# ── RANKS ────────────────────────────────────────────────
SLAYER_RANKS = [
    ("Mizunoto",    0),
    ("Mizunoe",     5),
    ("Kanoto",     12),
    ("Kanoe",      22),
    ("Tsuchinoto",  35),
    ("Tsuchinoe",   51),
    ("Hinoto",     70),
    ("Hinoe",      92),
    ("Kinoto",    117),
    ("Kinoe",     145),
    ("Hashira",   180),
]

DEMON_RANKS = [
    ("Lesser Demon",                   0),
    ("Demon",                          5),
    ("Intermediate Demon",            12),
    ("Advanced Demon",                22),
    ("Demon in the Twelve Kizuki",    38),
    ("Lower Six",                     60),
    ("Lower Five",                    80),
    ("Lower Four",                   100),
    ("Lower Three",                  120),
    ("Lower Two",                    145),
    ("Lower One",                    170),
    ("Upper Six",                    200),
    ("Upper Five",                   235),
    ("Upper Four",                   270),
    ("Upper Three",                  310),
    ("Upper Two",                    355),
    ("Upper One",                    405),
    ("Demon King",                   460),
]

# ── BREATHING STYLES ────────────────────────────────────
BREATHING_STYLES = [
    "Water", "Flame", "Thunder", "Wind", "Stone",
    "Insect", "Sound", "Love", "Serpent", "Mist"
]

BREATHING_FORMS = {
    "Water": [
        ("1st Form: Water Surface Slash",        2,  "A quick horizontal slash — reliable opener."),
        ("2nd Form: Water Wheel",                5,  "A spinning vertical slash — wide & powerful."),
        ("3rd Form: Flowing Dance",              4,  "Fluid movements that weave past the enemy."),
        ("4th Form: Striking Tide",              7,  "Multiple consecutive slashes in rapid flow."),
        ("5th Form: Blessed Rain After Drought", 3,  "A gentle yet precise strike — bonus END damage."),
        ("6th Form: Whirlpool",                  8,  "A twisting slash that drags the enemy inward."),
        ("7th Form: Drop Ripple Thrust",         6,  "A thrust so precise it pierces through guard."),
        ("8th Form: Waterfall Basin",            7,  "A downward slash that crashes like falling water."),
        ("9th Form: Splashing Water Flow",       6,  "High-speed repositioning — slash from every angle."),
        ("10th Form: Constant Flux",            10,  "A spiralling dragon of water — the ultimate form."),
    ],
    "Flame": [
        ("1st Form: Unknowing Fire",             3,  "A fast draw-slash — enemy rarely sees it coming."),
        ("2nd Form: Rising Scorching Sun",       6,  "An upward slash surging like a rising sun."),
        ("3rd Form: Blazing Universe",           5,  "A spinning slash that ignites everything around."),
        ("4th Form: Blooming Flame Undulation",  8,  "A wild, unpredictable slash — high variance."),
        ("5th Form: Flame Tiger",               10,  "The mightiest flame form — devastating but tiring."),
        ("6th Form: Rengoku (Purgatory)",       13,  "The secret sixth form — burns everything in its path."),
        ("9th Form: Rengoku",                   15,  "Rengoku's personal form — a soul-scorching blaze."),
    ],
    "Thunder": [
        ("1st Form: Thunderclap and Flash",               9,  "Godspeed draw — the fastest single strike."),
        ("2nd Form: Rice Spirit",                         4,  "Rapid multi-hit strikes following the 1st Form."),
        ("3rd Form: Thunder Swarm",                       6,  "Lightning-fast slashes from every angle."),
        ("4th Form: Distant Thunder",                     5,  "A ranged slash sending a shockwave forward."),
        ("5th Form: Heat Lightning",                      7,  "A blinding burst — may stagger the enemy."),
        ("6th Form: Thunderclap and Flash — Sixfold",    13,  "Six godspeed bursts in an instant."),
        ("7th Form: Thunderclap and Flash — Godspeed",   17,  "Beyond human limits — the pinnacle of Thunder Breathing."),
    ],
    "Wind": [
        ("1st Form: Dust Whirlwind Cutter",      5,  "Slashes released in a single rotation."),
        ("2nd Form: Claws — Fleeting",           6,  "Double strike — each slash curves like a talon."),
        ("3rd Form: Clear Storm Wind Tree",      5,  "Calm, centered slashes in perfect stillness."),
        ("4th Form: Rising Dust Storm",          7,  "An upward slash that sends the enemy airborne."),
        ("5th Form: Cold Mountain Wind",         6,  "A wide horizontal slash — sweeps all in range."),
        ("6th Form: Black Wind Mountain Mist",   8,  "A spinning slash shrouded in darkness and wind."),
        ("7th Form: Gale — Sudden Gusts",        9,  "Violent random slashes — unpredictable fury."),
        ("8th Form: Primary Gale Slash",        10,  "A single devastating burst of compressed wind."),
        ("9th Form: Idaten Typhoon",            11,  "A spinning, rising gale that obliterates guards."),
    ],
    "Stone": [
        ("1st Form: Serpentinite Bipolar",               6,  "A dual slash with tremendous weight behind it."),
        ("2nd Form: Upper Smash",                        7,  "A crushing downward strike with full body force."),
        ("3rd Form: Stone Skin",                         4,  "A defensive form — greatly reduces incoming damage."),
        ("4th Form: Volcanic Rock — Rapid Conquest",     9,  "A burst of heavy rapid blows."),
        ("5th Form: Arcs of Justice",                   12,  "Seven simultaneous arcing slashes — Stone's pinnacle."),
    ],
    "Insect": [
        ("Butterfly Dance: Caprice",                        5,  "Flowing dance-like slashes coated in poison."),
        ("Dance of the Bee Sting: True Flutter",            7,  "A single pierce — injects potent venom."),
        ("Dance of the Dragonfly: Compound Eye",            6,  "Rapid strikes from impossible angles."),
        ("Dance of the Centipede: Hundred-Legged Zigzag",   9,  "Dozens of lightning-fast venomous hits."),
        ("Dance of the Butterfly: Light and Dark",         11,  "The ultimate insect form — poison clouds everything."),
    ],
    "Sound": [
        ("1st Form: Roar",                       6,  "A thunderous slash that disorients the target."),
        ("2nd Form: Constant Resounding Slash",  7,  "Rapid slashes that create a wall of sound."),
        ("3rd Form: String Performance",         5,  "A precision strike aimed at a weak point."),
        ("4th Form: Reverberation Slash",        8,  "A slash that echoes — hits twice."),
        ("5th Form: Banshee Scream",            11,  "A full-body explosion of sound — stuns everything nearby."),
    ],
    "Love": [
        ("1st Form: Flailing Waltz",             5,  "Unpredictable wide swings — difficult to read."),
        ("2nd Form: Love Pangs",                 6,  "Diagonal slashes that strike pressure points."),
        ("3rd Form: Catlove Shower",             7,  "Rapid barrage of graceful scratching strikes."),
        ("4th Form: Crush",                      9,  "A spinning downward slam with maximum force."),
        ("5th Form: Swoon Love",                10,  "A mesmerising dash-slash — leaves enemy stunned."),
        ("6th Form: Cat-Legged Winds of Love",  12,  "Mitsuri's personal form — twists the blade beyond limits."),
    ],
    "Serpent": [
        ("1st Form: Winding Serpent Slash",              5,  "A twisting slash that curves around defences."),
        ("2nd Form: Venom Fangs of the Narrow Head",     6,  "A rapid thrust that mimics a snake's strike."),
        ("3rd Form: Coil Choke",                         7,  "A wrapping slash that constricts the enemy."),
        ("4th Form: Twin-Headed Reptile",                8,  "Two simultaneous slashes from opposite angles."),
        ("5th Form: Slithering Serpent",                11,  "The body moves like a serpent — strikes from everywhere."),
    ],
    "Mist": [
        ("1st Form: Low Clouds, Distant Haze",   5,  "A disorienting weaving slash through the mist."),
        ("2nd Form: Eight-Layered Mist",         6,  "Eight rapid slashes — each one harder to track."),
        ("3rd Form: Scattering Mist Slash",      6,  "A wide slash that splinters into many directions."),
        ("4th Form: Shifting Flow Slash",        7,  "Flow with the enemy's movement — redirect and strike."),
        ("5th Form: Sea of Clouds and Haze",     8,  "An enveloping misty swirl of relentless slashes."),
        ("6th Form: Lunar Dispersing Mist",      9,  "A moonlit slash that scatters as it hits."),
        ("7th Form: Obscuring Clouds",          12,  "Muichiro's personal form — completely unreadable."),
    ],
}

# ── BLOOD DEMON ARTS ────────────────────────────────────
BLOOD_ARTS = {
    "Spiderweb Cutting Thread": [
        ("Cutting Thread Rotation",          5,  "Spinning webs of razor thread slice everything around you."),
        ("Cutting Thread — Cross Formation", 7,  "Threads cross in an X — impossible to dodge cleanly."),
        ("Cutting Thread — Long Slash",      6,  "A single thread fired at blinding range."),
        ("Cutting Thread — Cage",            9,  "Threads surround the enemy completely — no escape."),
        ("Ensnaring Net",                   11,  "A web of threads tightens around the target, shredding on contact."),
    ],
    "Blood Sickle": [
        ("Rotating Sickle Slash",            5,  "A spinning arc of razor blood-sickles."),
        ("Flying Blood Sickle",              7,  "Blood hardens into blades and launches at speed."),
        ("Winding Sickle",                   6,  "A curved sickle that follows the target around corners."),
        ("Piercing Blood",                   9,  "Concentrated blood spikes fired in rapid succession."),
        ("Scattering Sickle Barrage",       12,  "Hundreds of blood-sickles launched simultaneously."),
    ],
    "Obi Sash Manipulation": [
        ("Obi Sash Whip",                    4,  "A lashing strike with an extending sash of flesh."),
        ("Obi Entrapment",                   6,  "The sash wraps around the enemy — constricting."),
        ("Cutting Sash",                     7,  "The sash hardens to a blade edge and slashes."),
        ("Sash Barrage",                     9,  "Multiple sash ends strike from all directions at once."),
        ("Pulling Obi — Full Absorption",   12,  "The sash pulls the enemy in and crushes on impact."),
    ],
    "Destructive Death": [
        ("Compass Needle",                   5,  "Shockwaves fired from strikes — a ranged crushing force."),
        ("Annihilation Type",                8,  "A series of accelerating punches building toward a burst."),
        ("Torchlight Flash",                 7,  "Shockwave released in a spinning kick — wide spread."),
        ("Disorder",                        10,  "Rapid disorienting combination of shockwave strikes."),
        ("Eight Layered Demon Core",        14,  "A compressed shockwave from the core of the body — devastating."),
    ],
    "Moon Breathing": [
        ("1st Form: Dark Moon, Evening Palace",    6,  "A crescent slash that extends unnaturally far."),
        ("2nd Form: Pearl Flower Moongazing",      8,  "Multiple crescent slashes released simultaneously."),
        ("5th Form: Moon Spirit Calamitous Eddy",  9,  "A vortex of crescent slashes that drags the enemy in."),
        ("9th Form: Waning Moonswaths",           11,  "Dozens of crescent blades released in a spreading arc."),
        ("16th Form: Moonbow, Half Moon",         15,  "An overwhelming burst of crescent blades — the pinnacle form."),
    ],
    "Biokinesis": [
        ("Whip Strike",                      5,  "An arm extends unnaturally and whips at blinding speed."),
        ("Shockwave Stomp",                  7,  "A stomp releases a shockwave through the ground."),
        ("Cellular Barrage",                 8,  "The body fires countless hardened cells as projectiles."),
        ("Darkness Slash",                   9,  "Black blood hardens into blades that erupt outward."),
        ("Shifting Form — Final Shape",      14,  "Full body mutation — a monstrous true form unleashed."),
    ],
}

DEMON_ART_STYLES = list(BLOOD_ARTS.keys())

# ── CUSTOM BREATHING TEMPLATE ───────────────────────────
CUSTOM_BREATHING_TEMPLATE = {
    "forms": [
        ("1st Form: {name}'s Opening Strike",  6,  "A form born from your own instinct — the first step."),
        ("2nd Form: {name}'s Flowing Edge",    8,  "A fluid continuation — your body moves on its own."),
        ("3rd Form: {name}'s Convergence",     9,  "All energy focused into a single devastating point."),
        ("4th Form: {name}'s Fracture",       11,  "A form that breaks limits — power beyond training."),
        ("5th Form: {name}'s True Breath",    13,  "The pinnacle of your personal style."),
    ],
    "ultimate": (
        "{name}'s Breath — Absolute Silence",
        22,
        "You still the world. One breath. One strike. Everything ends.",
    ),
}

# ── ITEMS ────────────────────────────────────────────────
ITEMS = {
    "Wisteria Herb":    {"desc": "A medicinal herb. Restores 25 HP.",        "type": "heal",   "value": 25},
    "Corps Ration":     {"desc": "Standard field ration. Restores 40 HP.",   "type": "heal",   "value": 40},
    "Crimson Elixir":   {"desc": "Restores 70 HP. Smells of iron.",          "type": "heal",   "value": 70},
    "Full Recovery":    {"desc": "Rare tonic. Fully restores HP.",           "type": "heal",   "value": 9999},
    "Sharpening Stone": {"desc": "+5 ATK for next battle.",                  "type": "atk_up", "value": 5},
    "Iron Ration":      {"desc": "+10 END permanently.",                     "type": "end_up", "value": 10},
    "Speed Scroll":     {"desc": "+3 SPD permanently.",                      "type": "spd_up", "value": 3},
    "Muzan's Shard":    {"desc": "A fragment of Muzan. +5 STR permanently.", "type": "str_up", "value": 5},
}

SHOP_STOCK  = ["Wisteria Herb", "Corps Ration", "Crimson Elixir", "Sharpening Stone"]
SHOP_PRICES = {
    "Wisteria Herb": 15,
    "Corps Ration":  25,
    "Crimson Elixir": 45,
    "Sharpening Stone": 30,
}

# ── MISSIONS ─────────────────────────────────────────────
SLAYER_HQ_MISSIONS = [
    {"title": "Rescue at Kushi Village",
     "briefing": "Villagers report a demon picking off travellers on the eastern road. Eliminate it.",
     "enemy": "Road Demon",       "hp": 45,  "atk": 9,  "gold": 12, "exp": 20, "kills": 1,
     "drop": ("Wisteria Herb",    0.45)},
    {"title": "The Stolen Children",
     "briefing": "Three children vanished from Hino Town. A demon has been sighted near the river.",
     "enemy": "River Stalker",    "hp": 65,  "atk": 13, "gold": 20, "exp": 30, "kills": 1,
     "drop": ("Corps Ration",     0.35)},
    {"title": "Merchant Escort",
     "briefing": "A merchant caravan was ambushed. The demon is still in the area. Drive it off.",
     "enemy": "Ambush Demon",     "hp": 80,  "atk": 15, "gold": 28, "exp": 40, "kills": 2,
     "drop": ("Sharpening Stone", 0.25)},
    {"title": "The Haunted Inn",
     "briefing": "Guests at the Fuji Inn have been disappearing. A strong demon has nested inside.",
     "enemy": "Nest Demon",       "hp": 100, "atk": 18, "gold": 38, "exp": 55, "kills": 2,
     "drop": ("Crimson Elixir",   0.20)},
    {"title": "Temple Infestation",
     "briefing": "A temple west of the capital has been seized. Multiple priests killed.",
     "enemy": "Temple Warden",    "hp": 130, "atk": 21, "gold": 50, "exp": 70, "kills": 3,
     "drop": ("Speed Scroll",     0.15)},
    {"title": "The Corps Traitor",
     "briefing": "A former slayer turned demon has been sighted. The Corps wants them dealt with quietly.",
     "enemy": "Fallen Slayer",    "hp": 160, "atk": 25, "gold": 70, "exp": 90, "kills": 4,
     "drop": ("Muzan's Shard",    0.10)},
]

DEMON_HQ_MISSIONS = [
    {"title": "The Wandering Prey",
     "briefing": "A lone traveller walks the mountain pass at night. Weak. Easy. Feed.",
     "enemy": "Frightened Traveller",  "hp": 30,  "atk": 5,  "gold": 10, "exp": 20, "kills": 1,
     "drop": ("Wisteria Herb",    0.30)},
    {"title": "Slayer Patrol",
     "briefing": "A junior slayer patrols the eastern forest. Destroy them before they report in.",
     "enemy": "Junior Slayer",         "hp": 55,  "atk": 11, "gold": 18, "exp": 30, "kills": 1,
     "drop": ("Corps Ration",     0.30)},
    {"title": "The Bold Village",
     "briefing": "A village has set wisteria traps. Make an example. Break their courage.",
     "enemy": "Village Guard Captain", "hp": 75,  "atk": 14, "gold": 26, "exp": 40, "kills": 2,
     "drop": ("Sharpening Stone", 0.25)},
    {"title": "Rival Demon",
     "briefing": "Another demon is encroaching on your territory. Muzan expects you to handle it.",
     "enemy": "Rival Demon",           "hp": 100, "atk": 17, "gold": 36, "exp": 55, "kills": 2,
     "drop": ("Crimson Elixir",   0.20)},
    {"title": "The Hashira's Student",
     "briefing": "A Hashira's top student is hunting in your region. End them before they bloom.",
     "enemy": "Hashira's Apprentice",  "hp": 135, "atk": 22, "gold": 55, "exp": 70, "kills": 3,
     "drop": ("Speed Scroll",     0.15)},
    {"title": "Muzan's Test",
     "briefing": "Muzan has sent a demon to assess your power. Prove yourself — or be consumed.",
     "enemy": "Muzan's Assessor",      "hp": 165, "atk": 26, "gold": 75, "exp": 90, "kills": 4,
     "drop": ("Muzan's Shard",    0.10)},
]

# ── STORY ────────────────────────────────────────────────
SLAYER_STORY = [
    # ─────────────────────────────────────────────────────
    #  CHAPTER 1
    # ─────────────────────────────────────────────────────
    {
        "rank": "Mizunoe", "title": "CHAPTER 1 — THE FIRST NIGHT",
        "lines": [
            "Your first mission: a village west of the mountains.",
            "Families have gone missing. Livestock found drained dry.",
            "You arrive at dusk. The air reeks of blood.",
            "From the shadows steps a pale figure — Hairo, a Lower Demon.",
            '"You smell of a slayer. How quaint." it sneers.',
            "This is your first real test.",
        ],
        "boss": "Hairo — Lower Demon", "boss_hp": 60, "boss_atk": 10, "exp": 60,
        "victory_lines": [
            "Hairo disintegrates in the first light of dawn.",
            "The villagers emerge from hiding, trembling with relief.",
            "A child hands you a small carved wooden sword.",
            '"Thank you," she whispers. "Please don\'t stop fighting."',
            "You pocket the carving. You won't stop.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 2
    # ─────────────────────────────────────────────────────
    {
        "rank": "Kanoe", "title": "CHAPTER 2 — THE TSUZUMI MANSION",
        "lines": [
            "Three slayers went missing near the Tsuzumi Mansion.",
            "The Corps sends you to investigate.",
            "When you arrive, the mansion is alive — walls breathing,",
            "hallways shifting, floors twisting beneath your feet.",
            "Inside, you find a demon with a drum fused to its body.",
            "Each beat warps the room. Every strike reshapes reality.",
            '"You are not welcome here," the drum-demon growls.',
            "You recognise him from the Corps files — Kyogai.",
            "Once a writer. Once human. Now something the world forgot.",
        ],
        "boss": "Kyogai — Drum Demon", "boss_hp": 90, "boss_atk": 14, "exp": 80,
        "victory_lines": [
            "The mansion shatters as Kyogai crumbles to ash.",
            "Scrolls of his old writing flutter to the ground.",
            "They are beautiful — tragic proof he was once human.",
            "You collect them. Some things deserve to be remembered.",
            "The Corps promotes you. Your name is spreading.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 3
    # ─────────────────────────────────────────────────────
    {
        "rank": "Tsuchinoe", "title": "CHAPTER 3 — MOUNT NATAGUMO",
        "lines": [
            "Mount Natagumo. A mountain no one returns from.",
            "Slayers sent ahead have been twisted into puppets —",
            "their bodies controlled by threads finer than silk.",
            "The Spider Family lurks here. A nest of demons",
            "who pretend to be a family but know nothing of love.",
            "Rui — the youngest, the most dangerous — watches from above.",
            "He controls the others with threads and fear.",
            "The eldest son — Father Spider — steps into your path first.",
            '"Every thread I pull makes them dance," he laughs.',
            '"Let me see how you move."',
        ],
        "boss": "Father Spider — Mount Natagumo", "boss_hp": 130, "boss_atk": 18, "exp": 100,
        "victory_lines": [
            "The threads go slack. Slayers collapse, free at last.",
            "Some don't make it. You carry their wisteria badges home.",
            "Tanjiro Kamado was here too — you caught a glimpse of him.",
            "Something about his Sun Breathing mark unnerves even the demons.",
            "Master Kagaya receives you personally at the Ubuyashiki estate.",
            '"You grieve properly," he says softly. "That makes you strong."',
            "You are promoted to Hinoe. The demons are beginning to fear your name.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 4 — MUGEN TRAIN (multi-stage)
    # ─────────────────────────────────────────────────────
    {
        "rank": "Kinoe", "title": "CHAPTER 4 — THE MUGEN TRAIN",
        "multi_stage": True,
        "stages": [
            {
                "label": "STAGE 1 — THE SLEEPING PASSENGERS",
                "lines": [
                    "The Mugen Train. Forty passengers. No survivors in months.",
                    "Flame Hashira Rengoku Kyojuro boards with you.",
                    "His laugh fills the carriage like warm firelight.",
                    '"UMAI!" he bellows at his bento. You can\'t help but smile.',
                    "But the passengers are already asleep — one by one.",
                    "Enmu, Lower Moon One, has fused his flesh into the train itself.",
                    "Dream minions slither through the carriages,",
                    "weaving nightmares and severing life-threads in the dark.",
                    "You shake yourself awake. The train rocks violently.",
                    "Enmu's human cultists emerge from the shadows.",
                ],
                "boss": "Enmu's Dream Minions", "boss_hp": 110, "boss_atk": 16,
                "victory_lines": [
                    "The cultists crumble. The sleeping passengers stir.",
                    "But you feel it — the train itself is alive.",
                    "Somewhere deep in the engine, something massive breathes.",
                ],
            },
            {
                "label": "STAGE 2 — ENMU'S TRUE BODY",
                "lines": [
                    "You fight your way to the locomotive.",
                    "Enmu's body is enormous — he has merged with the train.",
                    "Flesh wraps the iron. Eyes open across every carriage wall.",
                    '"Sleep. Sleep and dream of nothing," he whispers.',
                    "Rengoku appears beside you, cape billowing in the wind.",
                    '"I will protect the passengers — you take his neck. GO!"',
                ],
                "boss": "Enmu — Lower Moon One (True Body)", "boss_hp": 170, "boss_atk": 22,
                "victory_lines": [
                    "Enmu disintegrates, crying that he only wanted to dream.",
                    "The train derails in a thunderclap of steel and steam.",
                    "Forty passengers. All alive.",
                    "Rengoku stands atop the wreckage, breathing hard but smiling.",
                    '"Well done. You fought like a true slayer."',
                    "For one moment — the world is quiet.",
                    "Then the ground shakes.",
                ],
            },
            {
                "label": "STAGE 3 — AKAZA (HIDDEN BOSS)",
                "lines": [
                    "Something drops from the sky and craters the earth beside the train.",
                    "A figure rises from the dust — lean, pale, covered in tattoos,",
                    "radiating a pressure that makes the air itself flinch.",
                    "Akaza. Upper Moon Three.",
                    "He looks at Rengoku and smiles — the smile of a man",
                    "who has ended the lives of countless Hashira.",
                    '"Flame Hashira. You\'re strong. I want a real fight."',
                    "Rengoku steps forward. You step with him.",
                    '"Outsider," Akaza says, glancing at you cold. "This is none of your concern."',
                    "But you raise your blade anyway.",
                    "",
                    "Rengoku fights with everything — Ninth Form: Purgatory burns the sky.",
                    "But Akaza regenerates every wound instantly.",
                    "You watch Rengoku's light begin to dim.",
                    "",
                    "  ─── Dawn is one minute away. ───",
                    "  [ What do you do? ]",
                    "  [1] FIGHT — charge Akaza alongside Rengoku",
                    "  [2] HOLD  — protect Rengoku's wounds and survive until dawn",
                ],
                "boss": "Akaza — Upper Moon Three", "boss_hp": 240, "boss_atk": 28,
                "choice": True,
                "victory_lines": [
                    "Dawn breaks across the wreckage.",
                    "Akaza retreats into the shadows — he cannot face the sun.",
                    '"You are strong," he says as he vanishes. "But not enough."',
                    "Rengoku stands. His wounds are deep. His smile is not.",
                    '"Don\'t make that face," he says quietly.',
                    '"A Hashira who can\'t protect the passengers is no Hashira at all."',
                    "He grips your shoulder. His hand is warm despite everything.",
                    '"Set your heart ablaze."',
                    "Those are his last words.",
                    "He does not make it to sunrise.",
                    "",
                    "The grief doesn't paralyse you. It lights you on fire.",
                ],
                "rengoku_saved_lines": [
                    "The sun crests the horizon. Akaza screams and vanishes.",
                    "Rengoku is alive — barely. He holds your hand.",
                    '"You bought me those seconds," he says. "I won\'t waste them."',
                    "He survives. He will carry this night forever.",
                    "And so will you.",
                ],
            },
        ],
        "lines": [], "boss": "", "boss_hp": 0, "boss_atk": 0, "exp": 200,
        "victory_lines": [],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 5 — ENTERTAINMENT DISTRICT (multi-stage)
    # ─────────────────────────────────────────────────────
    {
        "rank": "Hashira", "title": "CHAPTER 5 — ENTERTAINMENT DISTRICT",
        "multi_stage": True,
        "stages": [
            {
                "label": "STAGE 1 — DAKI OF THE UPPER MOONS",
                "lines": [
                    "Yoshiwara. The Entertainment District. Lanterns, music, silk.",
                    "And underneath it all — something foul.",
                    "Sound Hashira Uzui Tengen has gone undercover.",
                    "Three of his wives have vanished.",
                    "You follow the screams to the deepest quarter of the district.",
                    "A woman stands in the lantern light, beautiful and furious.",
                    "Her obi sash uncoils — razor-edged, hungry.",
                    '"You\'re looking for someone?" Daki says. "How unfortunate."',
                    "She is Upper Moon Six. She has killed seven Hashira.",
                    "Her flesh is regenerating before your eyes.",
                ],
                "boss": "Daki — Upper Moon Six", "boss_hp": 180, "boss_atk": 24,
                "victory_lines": [
                    "Daki's head separates from her shoulders.",
                    "She should dissolve. She doesn't.",
                    "Instead — she screams. A child's scream.",
                    "And the ground erupts.",
                ],
            },
            {
                "label": "STAGE 2 — GYUTARO'S EMERGENCE",
                "lines": [
                    "Something tears free from Daki's back — a withered, grinning figure.",
                    "Gyutaro — the true Upper Moon Six.",
                    "Daki was always just his extension. His beloved little sister.",
                    "He looks at her wounds and his smile dies entirely.",
                    '"You hurt my sister."',
                    "His blood sickles materialise from the air —",
                    "coated in lethal poison, curving impossibly around corners.",
                    "Uzui Tengen arrives in a burst of sound and golden light.",
                    '"Not alone, kid," he grins, though he\'s already bleeding badly.',
                    "You fight together. The district burns around you.",
                ],
                "boss": "Gyutaro — True Upper Moon Six", "boss_hp": 230, "boss_atk": 27,
                "victory_lines": [
                    "Both heads fall at once — it was the only way.",
                    "Gyutaro and Daki dissolve together, arguing even at the very end.",
                    "In their last moments, they are simply a brother and a sister.",
                    "Uzui Tengen collapses, laughing despite everything.",
                    '"Flamboyant victory," he declares. "Obviously."',
                    "The district slowly stops burning.",
                    "Uzui's three wives emerge from hiding — alive.",
                    "Dawn comes pink and quiet over Yoshiwara.",
                ],
            },
        ],
        "lines": [], "boss": "", "boss_hp": 0, "boss_atk": 0, "exp": 180,
        "victory_lines": [],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 6 — SWORDSMITH VILLAGE
    # ─────────────────────────────────────────────────────
    {
        "rank": "Hashira", "title": "CHAPTER 6 — THE SWORDSMITH VILLAGE",
        "lines": [
            "The Swordsmith Village — hidden, sacred, secret no longer.",
            "Upper Moon Four and Five have infiltrated its borders.",
            "Hantengu and Gyokko — ancient demons who've lived centuries.",
            "Mist Hashira Muichiro Tokito fights alone against Gyokko.",
            "You arrive to find the village burning.",
            "Love Hashira Mitsuri Kanroji holds the line against Hantengu.",
            "His clones multiply with every strike — each one a different emotion.",
            "Joy. Sorrow. Anger. Pleasure.",
            "You face the true body hidden among the chaos.",
        ],
        "boss": "Hantengu — Upper Moon Four", "boss_hp": 220, "boss_atk": 26, "exp": 160,
        "victory_lines": [
            "Dawn breaks. Hantengu dissolves as sunlight reaches him.",
            "Mitsuri collapses with a smile. 'We did it.'",
            "Muichiro's memories have returned — he is finally whole.",
            "The village survived. The swordsmiths live.",
            "Kagaya summons all Hashira. The final battle is approaching.",
            "The Dimensional Infinity Fortress will rise.",
            "Every Hashira prepares. You prepare.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 7 — HASHIRA TRAINING (multi-stage)
    # ─────────────────────────────────────────────────────
    {
        "rank": "Hashira", "title": "CHAPTER 7 — HASHIRA TRAINING",
        "multi_stage": True,
        "stages": [
            {
                "label": "TRIAL I — HIMEJIMA'S BOULDER HALL",
                "lines": [
                    "Stone Hashira Gyomei Himejima does not speak at first.",
                    "He simply points at a boulder the size of a small building.",
                    "You have heard what this training does to people.",
                    "Three slayers quit before noon on the first day.",
                    "Gyomei rings his prayer beads and says only one thing.",
                    '"Pain is the teacher. Your will is the student."',
                    "You survive day one. Barely.",
                    "By day seven — you move the boulder.",
                ],
                "boss": "Gyomei's Training Phantom", "boss_hp": 100, "boss_atk": 18,
                "victory_lines": [
                    "Gyomei nods — a single, slow nod.",
                    "Coming from him, that is higher praise than any words.",
                    "Your endurance and core strength have fundamentally changed.",
                ],
            },
            {
                "label": "TRIAL II — SANEMI'S WIND GAUNTLET",
                "lines": [
                    "Wind Hashira Shinazugawa Sanemi does not believe in gentleness.",
                    '"Most of you will die in the Fortress," he says pleasantly.',
                    "He sets ninety wooden training dolls on you simultaneously.",
                    "You cannot block. There is no blocking here.",
                    "Only movement. Only breath. Only survival.",
                    "On the third day, Sanemi spars with you directly.",
                    "He holds nothing back.",
                ],
                "boss": "Sanemi — Wind Hashira (Sparring)", "boss_hp": 130, "boss_atk": 22,
                "victory_lines": [
                    "You land a single clean hit on Sanemi.",
                    "He stops. Looks at you. Almost grins.",
                    '"Not terrible," he says.',
                    "You have never felt more capable in your life.",
                ],
            },
            {
                "label": "TRIAL III — TOMIOKA'S FINAL TEST",
                "lines": [
                    "Water Hashira Tomioka Giyu trains you last.",
                    "He says almost nothing for the first three days.",
                    "On the fourth day he asks you one question.",
                    '"Why do you fight?"',
                    "Whatever you answer — he nods, barely.",
                    "Then he draws his blade.",
                    "This is not a spar. This is a conversation in steel.",
                    "Answer him with everything you have.",
                ],
                "boss": "Tomioka — Water Hashira (Final Trial)", "boss_hp": 150, "boss_atk": 24,
                "victory_lines": [
                    "Tomioka sheathes his sword.",
                    '"You have the breath now," he says. "Use it."',
                    "The Hashira Training is complete.",
                    "Every muscle in your body knows something it didn't before.",
                    "You stand at the threshold of your absolute limit.",
                    "Beyond it — the Infinity Fortress waits.",
                ],
            },
        ],
        "lines": [], "boss": "", "boss_hp": 0, "boss_atk": 0, "exp": 220,
        "victory_lines": [],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 8 — FINAL DAWN (7 stages)
    # ─────────────────────────────────────────────────────
    {
        "rank": "Hashira", "title": "CHAPTER 8 — FINAL DAWN",
        "multi_stage": True,
        "stages": [
            {
                "label": "STAGE 1 — KAIGAKU (WITH ZENITSU)",
                "lines": [
                    "The Infinity Fortress swallows the night sky.",
                    "Muzan raises it from the earth and it folds inward —",
                    "a labyrinth of infinite rooms rearranging themselves endlessly.",
                    "You and Zenitsu Agatsuma land in the same corridor.",
                    "Zenitsu is shaking. He is always shaking.",
                    "Then from the dark steps Kaigaku — Thunder Breathing, corrupted.",
                    "He was Zenitsu's senior. They shared the same master.",
                    "Now he is Upper Moon Six, drenched in Muzan's blood.",
                    '"You still breathe like a coward, Zenitsu."',
                    "",
                    "  [ Continue together — or let Zenitsu face his demon alone? ]",
                    "  [1] Fight alongside Zenitsu",
                    "  [2] Step back — this is Zenitsu's battle to win",
                ],
                "boss": "Kaigaku — Corrupted Upper Moon Six", "boss_hp": 180, "boss_atk": 24,
                "choice": True,
                "victory_lines": [
                    "Kaigaku is struck by Zenitsu's Seventh Form —",
                    "a technique their master always believed Zenitsu would develop.",
                    "Kaigaku dissolves, understanding nothing to the end.",
                    "Zenitsu stands in the aftermath, still shaking —",
                    "but now the shaking is grief, not fear.",
                    '"I did it, sensei," he whispers to no one.',
                    "The Fortress shifts. You move deeper in.",
                ],
            },
            {
                "label": "STAGE 2 — AKAZA (WITH TOMIOKA)",
                "lines": [
                    "The corridor opens into a vast empty chamber.",
                    "Tomioka Giyu is already there — bleeding but standing.",
                    "Akaza faces him, fists raised, completely calm.",
                    '"Water Hashira. You\'re not enough alone."',
                    "He notices you. Something flickers in his eyes.",
                    '"You were on the Mugen Train. You remember me."',
                    "You do. You remember everything.",
                    "Tomioka glances at you. A silent agreement.",
                    "You fight together.",
                ],
                "boss": "Akaza — Upper Moon Three", "boss_hp": 250, "boss_atk": 28,
                "victory_lines": [
                    "Akaza falters. His regeneration is finally slowing.",
                    "For the first time, something like doubt crosses his face.",
                    "A memory surfaces — a girl. A father. A life before demons.",
                    "He stops fighting. He looks at his own hands.",
                    '"Koyuki..." he says softly.',
                    "He does not regenerate the final wound.",
                    "Akaza dissolves in the dark, finally at peace.",
                    "Tomioka says nothing. But he bows his head.",
                ],
            },
            {
                "label": "STAGE 3 — DOMA (WITH INOSUKE & KANAO)",
                "lines": [
                    "Ice. Everywhere — ice.",
                    "Doma, Upper Moon Two, has shaped the chamber into a frozen cathedral.",
                    "Inosuke Hashibira and Kanao Tsuyuri are already fighting him.",
                    "Doma is smiling. He is always smiling.",
                    '"I love all of you," he says pleasantly, as he attacks.',
                    "His ice fans scatter deadly cold pollen through the air.",
                    "Kanao moves with the precision of a Flower Breathing master.",
                    "Inosuke moves with pure raging instinct.",
                    "And Doma keeps smiling.",
                    "Join them. Break that smile.",
                ],
                "boss": "Doma — Upper Moon Two", "boss_hp": 270, "boss_atk": 26,
                "victory_lines": [
                    "Doma is poisoned from the inside — Shinobu's final gift.",
                    "He dissolves, still unable to understand why people love each other.",
                    '"Is that what grief feels like?" he asks at the very end.',
                    "He almost sounds like he wanted to know.",
                    "Inosuke stands over the dissolving ice, chest heaving.",
                    '"We got him," Kanao says quietly.',
                    "Above you — the Fortress shudders. Kokushibo stirs.",
                ],
            },
            {
                "label": "STAGE 4 — KOKUSHIBO (WITH MUICHIRO, SANEMI, GYOMEI & GENYA)",
                "lines": [
                    "The highest chamber. Cold. Ancient. Absolutely still.",
                    "Kokushibo — Upper Moon One — stands at the centre.",
                    "He is six hundred years old.",
                    "He was once human. He was once Yoriichi's twin brother.",
                    "He chose to become a demon because he feared death.",
                    "And now he cannot remember what living felt like.",
                    "Muichiro Tokito faces him — last of the Tsugikuni bloodline.",
                    "Sanemi and Genya fight at his side. Gyomei anchors the room.",
                    "Kokushibo raises his Moon Breathing blade.",
                    "The crescent slashes that follow are beyond counting.",
                    "You step into the storm alongside all of them.",
                ],
                "boss": "Kokushibo — Upper Moon One", "boss_hp": 300, "boss_atk": 30,
                "victory_lines": [
                    "Kokushibo falls.",
                    "In his final moments he sees what he sacrificed —",
                    "a life, a brother, a sunrise he will never witness again.",
                    '"I wanted to surpass you," he says to Yoriichi\'s memory.',
                    "His six hundred years dissolve into the dark.",
                    "Muichiro does not survive the battle.",
                    "Neither does Genya.",
                    "Sanemi kneels over his brother and does not move for a long time.",
                    "Gyomei weeps. This is not weakness.",
                    "This is what it costs.",
                ],
            },
            {
                "label": "STAGE 5 — MUZAN: DAWN APPROACH",
                "lines": [
                    "The Fortress unravels. Muzan stands at its core.",
                    "He has absorbed Tamayo's drug and Nezuko's sunlight immunity.",
                    "He is transforming. His body has always been his greatest weapon.",
                    "What stands before you now is something entirely new.",
                    "Every surviving slayer converges. Battered. Bleeding. But here.",
                    '"So many of you," Muzan says. "And still — not enough."',
                    "He attacks with everything he has.",
                    "Hold him. The sun is coming.",
                ],
                "boss": "Muzan — First Evolved Form", "boss_hp": 250, "boss_atk": 30,
                "victory_lines": [
                    "Muzan is slowed. The drug is working.",
                    "But he mutates further — growing larger, more grotesque.",
                    "The slayers are exhausted. The sun is forty minutes away.",
                    "You must keep him here. No matter what.",
                ],
            },
            {
                "label": "STAGE 6 — MUZAN: DEMON SPIDER FORM",
                "lines": [
                    "Muzan's body reshapes itself into something inhuman.",
                    "Spider-like. Massive. Radiating cellular destruction in waves.",
                    "His cells are weaponised — every touch degrades your body.",
                    "Gyomei Himejima is the last slayer still at full force.",
                    "He roars like a mountain collapsing and charges.",
                    "You fight at his side. Every second is a second closer to dawn.",
                    "The horizon is beginning to lighten.",
                ],
                "boss": "Muzan — Demon Spider Form", "boss_hp": 300, "boss_atk": 32,
                "victory_lines": [
                    "Gyomei drives the killing blow with both hands —",
                    "a swing that shakes the earth beneath you.",
                    "Muzan's form shatters. He is retreating underground.",
                    "You have minutes. Chase him.",
                ],
            },
            {
                "label": "STAGE 7 — MUZAN: THE LAST SUNRISE",
                "lines": [
                    "Muzan bursts from the earth one final time.",
                    "The sun is rising. He knows it. He does not run.",
                    "He turns and faces you — just you.",
                    "The Hashira are down. The slayers are down.",
                    "And Muzan — for the first time in a thousand years —",
                    "looks at something and does not see prey.",
                    '"You," he says. "You are still standing."',
                    "Your blade rises. The sun is almost up.",
                ],
                "boss": "Muzan Kibutsuji — Demon King", "boss_hp": 350, "boss_atk": 33,
                "victory_lines": [
                    "The first ray of sunlight touches Muzan's skin.",
                    "He burns. Slowly. Completely.",
                    "And then — silence.",
                    "No more demons will be born. No more families will be taken.",
                    "You sheathe your blade for the last time.",
                    "Somewhere far away, a child is sleeping safely.",
                    "That is enough.",
                    "",
                    "  ✦  YOU HAVE CLEARED THE DEMON SLAYER PATH  ✦",
                    "",
                    "  But there is one more chapter waiting for you...",
                ],
            },
        ],
        "lines": [], "boss": "", "boss_hp": 0, "boss_atk": 0, "exp": 300,
        "victory_lines": [],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 9 — DEMON KING (secret ending)
    # ─────────────────────────────────────────────────────
    {
        "rank": "Hashira", "title": "CHAPTER 9 — DEMON KING",
        "lines": [
            "In his final moment, Muzan did something no one expected.",
            "He looked at you — the last one standing — and smiled.",
            "Not in defeat. In recognition.",
            '"You remind me of myself," he said.',
            "His blood entered you before the sun finished him.",
            "It should have killed you.",
            "It didn't.",
            "",
            "You wake up in darkness. The sun has set.",
            "The hunger is distant — like an echo in another room.",
            "You are still you. Barely.",
            "But something ancient lives in your blood now.",
            "",
            "  [ What do you choose? ]",
            "  [1] RESIST — burn Muzan's blood out and remain human",
            "  [2] ACCEPT — become what the demons feared you were all along",
        ],
        "boss": "Muzan's Will — Within You", "boss_hp": 200, "boss_atk": 25,
        "choice_type": "demon_king",
        "exp": 100,
        "victory_lines": [
            "The blood burns away. You remain human.",
            "The sun rises on a world without demons.",
            "And you — just a person, standing in the light.",
            "It's enough. It's more than enough.",
            "",
            "  ✦  TRUE ENDING — HUMANITY PRESERVED  ✦",
        ],
        "demon_king_lines": [
            "You stop fighting the blood. You let it in.",
            "The hunger grows. Then it quiets.",
            "You are not Muzan. You never were.",
            "But you are something new.",
            "A demon with a slayer's memory. A king with a human heart.",
            "The night is yours now.",
            "What you do with it — that's the only question left.",
            "",
            "  ✦  DEMON KING ENDING — THE NIGHT REMEMBERS YOU  ✦",
        ],
    },
]

DEMON_STORY = [
    # ─────────────────────────────────────────────────────
    #  CHAPTER 1
    # ─────────────────────────────────────────────────────
    {
        "rank": "Demon", "title": "CHAPTER 1 — YOUR FIRST HUNT",
        "lines": [
            "  ╔══════════════════════════════════════════╗",
            "  ║     BEFORE YOU WERE A DEMON...           ║",
            "  ╚══════════════════════════════════════════╝",
            "",
            "  A farmhouse. Rain on the roof. Someone cooking.",
            "  A name you used to answer to. A face you used to see",
            "  every morning in the river's reflection.",
            "  Gone. All of it — gone.",
            "",
            "You remember being human. Barely.",
            "The hunger is a roar that drowns everything else.",
            "A village glows in the valley below. Easy prey.",
            "But a slayer waits there — young, inexperienced, shaking.",
            "He draws his blade anyway. Brave, for a human.",
            '"Demon! I\'ll take your head!" he shouts.',
            "You almost feel sorry for him.",
        ],
        "boss": "Rookie Slayer", "boss_hp": 50, "boss_atk": 8, "exp": 60,
        "victory_lines": [
            "The slayer retreats into the night, defeated.",
            "You fed well. The hunger quiets — for now.",
            "But as dawn approaches, something unexpected surfaces.",
            "A memory. A name. Someone you used to love.",
            "You push it down. Demons don't have memories.",
            "...Do they?",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 2
    # ─────────────────────────────────────────────────────
    {
        "rank": "Intermediate Demon", "title": "CHAPTER 2 — MUZAN'S NOTICE",
        "lines": [
            "  ╔══════════════════════════════════════════╗",
            "  ║     IN THE DEPTHS OF THE INFINITY CASTLE ║",
            "  ╚══════════════════════════════════════════╝",
            "",
            "  Torches that burn without heat. Corridors that stretch",
            "  in directions that shouldn't exist. And at the centre of it all",
            "  — a silence so complete it has weight.",
            "",
            "A messenger finds you in the dark — another demon.",
            "Pale, slick, smelling of something ancient.",
            '"Muzan-sama has heard of you," it whispers.',
            '"He offers more blood. More power. More of everything."',
            "The Dimensional Infinity Fortress parts for you.",
            "Muzan does not look at you when you arrive.",
            "He simply extends one pale hand.",
            '"Drink," he says. "And become something worthy of my attention."',
            "You hesitate one breath.",
            "Then you drink.",
        ],
        "boss": "Muzan's Gatekeeper", "boss_hp": 100, "boss_atk": 15, "exp": 80,
        "victory_lines": [
            "The Gatekeeper crumbles. Muzan nods — barely.",
            "The blood burns through you like liquid fire.",
            "You are no longer a stray demon.",
            "You have a place in Muzan's design now.",
            "And the Demon Slayer Corps has just put your name on their list.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 3
    # ─────────────────────────────────────────────────────
    {
        "rank": "Lower Six", "title": "CHAPTER 3 — THE TWELVE KIZUKI",
        "lines": [
            "  ╔══════════════════════════════════════════╗",
            "  ║  THE GATHERING OF THE TWELVE KIZUKI      ║",
            "  ╚══════════════════════════════════════════╝",
            "",
            "  Twelve demons. Each one having survived for decades or centuries.",
            "  Their Muzan blood glows through their eyes like heated iron.",
            "  The air between them is sharp enough to cut.",
            "",
            "The Infinity Fortress assembles the Twelve Kizuki.",
            "You stand among demons that have lived for centuries.",
            "Lower Moons watch you with jealousy and contempt.",
            "Then Muzan kills three of them without expression.",
            '"Weak things disgust me," he says.',
            "He looks at you. His eyes are not eyes — they are something older.",
            '"I am giving you an opportunity. Do not waste it."',
            "A Lower Moon challenges your right to stand here.",
            "You will answer with blood.",
        ],
        "boss": "Lower Moon Rival", "boss_hp": 140, "boss_atk": 20, "exp": 100,
        "victory_lines": [
            "The Lower Moon dissolves at your feet.",
            "Muzan says nothing. He does not need to.",
            "Your position in the Twelve Kizuki is cemented.",
            "The other demons give you space now — out of fear.",
            "That night you dream of sunlight. You don't know why.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 4
    # ─────────────────────────────────────────────────────
    {
        "rank": "Upper Three", "title": "CHAPTER 4 — THE CORPS CLOSES IN",
        "lines": [
            "  ╔══════════════════════════════════════════╗",
            "  ║  SOMEWHERE ON THE EASTERN ROAD...        ║",
            "  ╚══════════════════════════════════════════╝",
            "",
            "  Three figures move through the forest at speed.",
            "  They have tracked you across four provinces.",
            "  Their uniforms are the Corps standard — black, silver trim.",
            "  Their eyes are the eyes of people who have nothing left to lose.",
            "",
            "They send three Kinoe-rank slayers after you.",
            "The best the Corps has below Hashira.",
            "You let them find you.",
            "The youngest hesitates when she sees your face.",
            '"You were human once," she says. Not a question.',
            "You say nothing. The eldest one charges.",
            "Somewhere in the back of your mind — a name.",
            "A name you buried long ago.",
        ],
        "boss": "Kinoe Slayer — Blade of the Corps", "boss_hp": 180, "boss_atk": 24, "exp": 130,
        "victory_lines": [
            "They retreat into the forest, broken but alive.",
            "You let them go. You don't know why.",
            "The youngest one looks back once before she disappears.",
            "Something about her eyes — they remind you of the name you buried.",
            "That night, for the first time in years, you dream of being warm.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 5
    # ─────────────────────────────────────────────────────
    {
        "rank": "Upper One", "title": "CHAPTER 5 — MUZAN'S FURY",
        "lines": [
            "  ╔══════════════════════════════════════════╗",
            "  ║  THE DIMENSIONAL INFINITY FORTRESS       ║",
            "  ╚══════════════════════════════════════════╝",
            "",
            "  The fortress rearranges itself around you as you walk.",
            "  Corridors fold. Stairways invert.",
            "  You have been summoned. You already know it will not be pleasant.",
            "",
            "Muzan summons you alone.",
            "The air in the Dimensional Infinity Fortress is stale with power.",
            "He killed three Upper Moons last month for failure.",
            "His eyes find yours.",
            '"You have been letting slayers escape," he says quietly.',
            "The room has no air.",
            '"That is not a weakness I can afford to tolerate."',
            "He sends his finest enforcer to remind you who you serve.",
            "Prove your loyalty — or be unmade.",
        ],
        "boss": "Kokushibo — Upper Moon One", "boss_hp": 250, "boss_atk": 28, "exp": 160,
        "victory_lines": [
            "Kokushibo falls — for the first time in his ancient life.",
            "He looks at you with something almost like respect.",
            '"You have his eyes," Kokushibo whispers before dissolving.',
            '"Yoriichi\'s eyes."',
            "You have no answer for that.",
            "You are now the strongest demon alive.",
            "Only Muzan stands above you.",
            "And Muzan is afraid — though he would never show it.",
        ],
    },
    # ─────────────────────────────────────────────────────
    #  CHAPTER 6
    # ─────────────────────────────────────────────────────
    {
        "rank": "Demon King", "title": "CHAPTER 6 — THE CHOICE",
        "lines": [
            "  ╔════════════════════════════════════════════╗",
            "  ║  THE FINAL BATTLE. THE CRUMBLING FORTRESS  ║",
            "  ╚════════════════════════════════════════════╝",
            "",
            "  The Hashira have broken through.",
            "  Muzan — cornered for the first time in a thousand years —",
            "  stands in the wreckage of his own fortress.",
            "  His composure is perfect. His eyes are not.",
            "",
            "The Infinity Fortress falls.",
            "Muzan is cornered — truly, finally cornered.",
            "He turns to you. His last Upper Moon.",
            '"Destroy them," he commands. "All of them."',
            "You look at the slayers across the battlefield.",
            "The young one is there — the one with your sister's eyes.",
            "She's bleeding. Still standing.",
            "Tanjiro Kamado stands beside her — marked by the Sun.",
            "Muzan's voice rises. 'I SAID DESTROY THEM.'",
            "Your blade is in your hand.",
            "",
            "  [ Who are you pointing it at? ]",
        ],
        "boss": "Muzan Kibutsuji — The First Demon", "boss_hp": 280, "boss_atk": 28, "exp": 200,
        "choice_type": "demon_final",
        "victory_lines": [
            "Muzan's scream tears through the fortress as you drive your blade into him.",
            "He dissolves — slowly, disbelievingly.",
            '"I was yours," you say. "Not anymore."',
            "The sun rises. Its light touches your skin.",
            "You expect to burn. You don't.",
            "Muzan's death has broken the curse.",
            "The young slayer lowers her blade.",
            '"I don\'t know who you were," she says. "But thank you."',
            "You close your eyes. You say your sister's name aloud — for the first time in decades.",
            "",
            "  ✦  YOU HAVE CLEARED THE DEMON PATH  ✦",
        ],
        "demon_continues_lines": [
            "You raise your blade against the slayers.",
            "The young one with your sister's eyes watches you come.",
            "She doesn't run.",
            "After the battle, you return to Muzan.",
            "He looks at you. He almost smiles.",
            '"Good," he says. "Now you are useful."',
            "But as you stand in the dark fortress alone,",
            "you think of the name you've been burying for years.",
            "You think of her face.",
            "And you wonder if you've lost something",
            "that can never be found again.",
            "",
            "  ✦  DEMON KING ENDING — THE NIGHT REMEMBERS YOU  ✦",
        ],
    },
]

FINAL_SELECTION_ENEMIES = [
    {"name": "Enslaved Demon",     "hp": 50,  "atk": 9},
    {"name": "Mutated Speed Demon", "hp": 70,  "atk": 12},
    {"name": "Wisteria Evader",    "hp": 60,  "atk": 10},
    {"name": "Hand Demon",         "hp": 100, "atk": 16},
]

# ── NICHIRIN SWORDS ──────────────────────────────────────
# rarity weights: Common 45, Uncommon 30, Rare 15, Legendary 8, Mythical 3
NICHIRIN_SWORD_WEIGHTS = {
    "Common": 45, "Uncommon": 30, "Rare": 15, "Legendary": 8, "Mythical": 3,
}

NICHIRIN_SWORD_RARITY_COLORS = {
    "Common":    WHITE,
    "Uncommon":  GREEN,
    "Rare":      CYAN,
    "Legendary": YELLOW,
    "Mythical":  MAGENTA,
}

NICHIRIN_SWORDS = {
    "Crimson Red":   {"desc": "A blade that bursts into flame. Associated with the Flame Hashira.",
                      "bonus": "STR +3",         "stat": ("str", 3),  "owner": "Rengoku Kyojuro",
                      "rarity": "Rare"},
    "Deep Blue":     {"desc": "Cold and calm as still water. Associated with the Water Hashira.",
                      "bonus": "END +3",         "stat": ("end", 3),  "owner": "Tomioka Giyu",
                      "rarity": "Uncommon"},
    "Yellow":        {"desc": "Crackling with lightning. Associated with the Thunder Hashira.",
                      "bonus": "SPD +3",         "stat": ("spd", 3),  "owner": "Agatsuma Zenitsu",
                      "rarity": "Uncommon"},
    "Jade Green":    {"desc": "Sharp as wind. Associated with the Wind Hashira.",
                      "bonus": "STR +2, SPD +1", "stat": ("str", 2),  "stat2": ("spd", 1),
                      "owner": "Shinazugawa Sanemi", "rarity": "Common"},
    "Gray":          {"desc": "Heavy and unbreakable. Associated with the Stone Hashira.",
                      "bonus": "END +4",         "stat": ("end", 4),  "owner": "Himejima Gyomei",
                      "rarity": "Rare"},
    "Pale Pink":     {"desc": "Slender and flexible. Associated with the Love Hashira.",
                      "bonus": "SPD +2, END +1", "stat": ("spd", 2),  "stat2": ("end", 1),
                      "owner": "Kanroji Mitsuri", "rarity": "Common"},
    "Lavender Blue": {"desc": "Mist-like and elusive. Associated with the Mist Hashira.",
                      "bonus": "SPD +4",         "stat": ("spd", 4),  "owner": "Tokito Muichiro",
                      "rarity": "Uncommon"},
    "Amber":         {"desc": "Coated in deadly poison. Associated with the Insect Hashira.",
                      "bonus": "END +2, STR +1", "stat": ("end", 2),  "stat2": ("str", 1),
                      "owner": "Kocho Shinobu",  "rarity": "Common"},
    "Indigo Gray":   {"desc": "Twists like a serpent mid-strike. Associated with the Serpent Hashira.",
                      "bonus": "STR +2, SPD +2", "stat": ("str", 2),  "stat2": ("spd", 2),
                      "owner": "Iguro Obanai",   "rarity": "Uncommon"},
    "Black":         {"desc": "Absorbs all light. Extremely rare — its meaning is unknown.",
                      "bonus": "STR +3, SPD +2", "stat": ("str", 3),  "stat2": ("spd", 2),
                      "owner": "Kamado Tanjiro", "rarity": "Mythical"},
    "Scarlet":       {"desc": "Burns with a fierce crimson heat — a blade of pure will.",
                      "bonus": "STR +4",         "stat": ("str", 4),  "owner": "Marisse Tolentino",
                      "rarity": "Legendary"},
    "Pure White":    {"desc": "A blade so pale it seems to vanish in sunlight.",
                      "bonus": "SPD +3, END +1", "stat": ("spd", 3),  "stat2": ("end", 1),
                      "owner": "Min Sun Yoo",    "rarity": "Legendary"},
    "Amethyst":      {"desc": "A shimmering edge that strikes with the precision of a needle and the weight of a mountain — chosen by the calm amidst the storm.",
                      "bonus": "STR +2, END +3", "stat": ("str", 2),  "stat2": ("end", 3),
                      "owner": "Hugh Frayre",    "rarity": "Legendary"},
    "Pink":          {"desc": "A blade that radiates warmth and overwhelming force — chosen by the rarest of souls.",
                      "bonus": "STR +4, END +4", "stat": ("str", 4),  "stat2": ("end", 4),
                      "owner": "Andrew Nona",    "rarity": "Mythical"},
}

# ── DEMON SLAYER MARK ────────────────────────────────────
MARK_DESCRIPTIONS = {
    "Water":   "A flowing wave crest appears on your cheek — Tomioka's mark, reborn in you.",
    "Flame":   "A flame pattern blazes across your forehead — Rengoku's fire lives on.",
    "Thunder": "A lightning bolt crackles from your temple — the mark of true speed.",
    "Wind":    "A gale spiral appears on your shoulder — the breath of a tempest.",
    "Stone":   "A stone-crack pattern covers your fist — immovable, unbreakable.",
    "Insect":  "A butterfly wing mark blooms on your neck — poison runs deeper now.",
    "Sound":   "A sound wave pattern marks your jaw — every strike resonates.",
    "Love":    "A flower mark blooms on your collarbone — grace beyond limits.",
    "Serpent": "Scales appear along your cheekbone — the serpent sees everything.",
    "Mist":    "A mist swirl drifts across your brow — you vanish before their eyes.",
}
