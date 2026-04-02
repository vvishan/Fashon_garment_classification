from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io
import warnings
warnings.filterwarnings("ignore")

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def classify_image(image_path) -> str:
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        raise RuntimeError(f"failed to open image:{e}")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skio_special_tokens=True)
