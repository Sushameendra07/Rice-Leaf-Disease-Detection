"""
Disease Information Utility
Comprehensive agricultural knowledge base for Rice Leaf Diseases:
- Bacterial Leaf Blight
- Brown Spot
- Leaf Smut
"""

DISEASE_DATA = {
    "Bacterial Leaf Blight": {
        "disease_name": "Bacterial Leaf Blight",
        "scientific_name": "Xanthomonas oryzae pv. oryzae",
        "severity": "High (up to 50% yield loss in severe cases)",
        "badge_color": "#FF4D4D",
        "icon": "🍂",
        "description": (
            "Bacterial Leaf Blight (BLB) is one of the most destructive diseases affecting rice crops worldwide. "
            "It causes wilting of seedlings and yellowing and drying of leaves. It is caused by Xanthomonas oryzae pv. oryzae "
            "and spreads rapidly through irrigation water, wind-blown rain, and infected seed stock."
        ),
        "symptoms": [
            "Lesions start as water-soaked stripes on leaf margins and tips.",
            "Stripes enlarge and turn yellowish-orange with wavy margins.",
            "As lesions age, leaves turn straw-yellow, dry up, and wither.",
            "Bacterial ooze beads (milky liquid droplets) may appear on young lesions early morning.",
            "In severe infections ('kresek' phase), entire plants wilt and collapse."
        ],
        "causes": [
            "Bacterial pathogen *Xanthomonas oryzae pv. oryzae*.",
            "High relative humidity (80–100%) and warm temperatures (25–34°C).",
            "Heavy rain showers, flooding, or strong winds causing leaf abrasion.",
            "Excessive application of nitrogen fertilizers.",
            "Use of susceptible rice seed varieties."
        ],
        "treatment": [
            "Spray Copper Hydroxide or Copper Oxychloride @ 2.5g/L water.",
            "Apply Streptocycline @ 0.5g + Copper Oxychloride @ 2g per liter of water.",
            "Drain infected fields temporarily to reduce humidity around root systems.",
            "Remove and burn severely infected crop debris after harvest."
        ],
        "prevention": [
            "Plant BLB-resistant rice varieties (e.g., IR64, PR121, Improved Samba Mahsuri).",
            "Treat seeds with Streptocycline (0.1g/L) for 12 hours prior to sowing.",
            "Follow balanced NPK fertilization; avoid excess nitrogen.",
            "Maintain proper plant spacing (20cm x 15cm) to ensure airflow and sunlight penetration."
        ],
        "farming_practices": [
            "Practice crop rotation with non-host leguminous crops.",
            "Ensure clean irrigation water; avoid transferring runoff from infected fields.",
            "Keep field borders clear of weed hosts like *Leersia hexandra*."
        ]
    },
    "Brown Spot": {
        "disease_name": "Brown Spot",
        "scientific_name": "Bipolaris oryzae (Cochliobolus miyabeanus)",
        "severity": "Moderate to High (affects grain quality and germination)",
        "badge_color": "#FFA500",
        "icon": "🟤",
        "description": (
            "Brown Spot is a fungal disease that attacks both leaves and grains of rice plants. "
            "Historically associated with nutrient-deficient or degraded soils (such as during the Bengal Famine of 1943), "
            "it causes oval brown spots that diminish photosynthesis and impair grain filling."
        ),
        "symptoms": [
            "Small, oval or cylindrical sesame-seed-shaped spots on leaves.",
            "Spots have dark reddish-brown to dark brown borders with light brown or gray centers.",
            "Fully developed spots are 0.5 to 1 cm long.",
            "Infected grains develop black or dark brown spots and become unmarketable.",
            "Yellow halo often surrounds mature leaf spots."
        ],
        "causes": [
            "Fungal pathogen *Bipolaris oryzae*.",
            "Nutrient deficiency in soil, particularly Nitrogen, Potassium, and Silicon.",
            "Unfavorable moisture conditions (drought stress or poorly drained soil).",
            "Airborne fungal spores spread via wind and rain splashes."
        ],
        "treatment": [
            "Foliar spray of Mancozeb @ 2g/L or Carbendazim @ 1g/L at early onset.",
            "Spray Propiconazole (Tilt 25 EC) @ 1ml/L at boot leaf stage.",
            "Apply bio-fungicides such as *Pseudomonas fluorescens* @ 10g/L."
        ],
        "prevention": [
            "Treat seeds with Thiram or Carbendazim @ 2g/kg seed before sowing.",
            "Apply balanced fertilizer according to soil test recommendations (ensure K and Si).",
            "Improve soil organic matter with farmyard manure or green manure crops.",
            "Use certified disease-free seeds."
        ],
        "farming_practices": [
            "Correct soil acidity and micronutrient deficiencies (Zinc & Iron).",
            "Maintain optimal water level during vegetative growth stage.",
            "Destroy crop residues after harvest to minimize overwintering fungal spores."
        ]
    },
    "Leaf Smut": {
        "disease_name": "Leaf Smut",
        "scientific_name": "Entyloma oryzae",
        "severity": "Low to Moderate (generally minor unless heavily infected)",
        "badge_color": "#20B2AA",
        "icon": "🟢",
        "description": (
            "Leaf Smut is a widespread fungal disease caused by Entyloma oryzae. "
            "It usually occurs late in the growing season on mature rice leaves. While less destructive than BLB, "
            "heavy leaf smut infections cause premature leaf drying and reduced photosynthetic productivity."
        ),
        "symptoms": [
            "Small, slightly raised, black linear spots (sori) on both leaf surfaces.",
            "Spots measure 0.5 to 5 mm long and 0.5 to 1.5 mm wide.",
            "Spots remain covered by the leaf epidermis until mature.",
            "Infected leaves turn yellow at tips, dry up, and die prematurely.",
            "Ruptured spots release dark brown to black teliospores."
        ],
        "causes": [
            "Fungal pathogen *Entyloma oryzae*.",
            "High nitrogen levels combined with dense planting.",
            "Warm, humid weather late in the cropping season.",
            "Spore survival in infected leaf debris in soil."
        ],
        "treatment": [
            "Foliar application of Copper Oxychloride @ 2.5g/L water.",
            "Spray Hexaconazole 5% EC @ 2ml/L if infection spreads quickly.",
            "Usually chemical intervention is only necessary if more than 30% leaf area is affected."
        ],
        "prevention": [
            "Avoid excessive late-season nitrogen applications.",
            "Ensure recommended planting density to prevent humid microclimates.",
            "Clean fields after harvest and practice deep plowing."
        ],
        "farming_practices": [
            "Rotate rice with upland crops to break fungal spore cycles.",
            "Use tolerant rice cultivars suitable for wet season cultivation.",
            "Monitor fields regularly during the flag leaf and flowering stages."
        ]
    }
}

MODEL_BENCHMARK_DATA = {
    "CNN": {"Accuracy": 0.3478, "Precision": 0.1210, "Recall": 0.3478, "F1-Score": 0.1795, "Params": "~1.2M", "Type": "Custom Baseline CNN"},
    "MobileNetV2": {"Accuracy": 0.9565, "Precision": 0.9620, "Recall": 0.9565, "F1-Score": 0.9565, "Params": "~2.2M", "Type": "Transfer Learning (Best)"},
    "VGG16": {"Accuracy": 0.8261, "Precision": 0.8247, "Recall": 0.8261, "F1-Score": 0.8230, "Params": "~14.7M", "Type": "Transfer Learning"},
    "EfficientNetB0": {"Accuracy": 0.3043, "Precision": 0.0926, "Recall": 0.3043, "F1-Score": 0.1420, "Params": "~4.0M", "Type": "Transfer Learning"}
}
