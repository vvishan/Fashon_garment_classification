def parse_caption(caption:str) -> dict:
    caption = caption.lower()
    attrs = {}
    colors = ["red", "blue", "black", "white", "green", "yellow", "pink", "brown", "gray", "purple", "striped"]
    types = ["shirt", "tshirt", "dress", "jacket", "coat", "pants", "jeans", "skirt", "shorts", "sweater"]
    styles = ["casual", "formal", "sport", "street", "vintage", "elegant", "modern"]
    materials = ["cotton", "denim", "leather", "wool", "silk", "linen", "polyester"]
    patterns = ["striped", "checked", "floral", "plain", "printed", "polka", "patterned"]

    # Extract attributes
    attrs["color"] = next((c for c in colors if c in caption), "unknown")
    attrs["type"] = next((t for t in types if t in caption), "unknown")
    attrs["style"] = next((s for s in styles if s in caption), "unknown")
    attrs["material"] = next((m for m in materials if m in caption), "unknown")
    attrs["pattern"] = next((p for p in patterns if p in caption), "unknown")

    return attrs
