import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers.tokenization_utils_base import BatchEncoding
from PIL import Image
import logging
from typing import Optional, Dict, Any, Union
from config import MODEL_NAME, MAX_LENGTH, NUM_BEAMS, TEMPERATURE

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CaptionModel:
    """Handles the Salesforce BLIP model for image captioning."""
    
    def __init__(self):
        self.model_name = MODEL_NAME
        self.max_length = MAX_LENGTH
        self.num_beams = NUM_BEAMS
        self.temperature = TEMPERATURE
        self.processor: Optional[BlipProcessor] = None
        self.model: Optional[BlipForConditionalGeneration] = None
        self.device: Optional[str] = None
        self._load_model()
    
    def _load_model(self):
        """Load the BLIP model and processor."""
        try:
            logger.info(f"Loading BLIP model: {self.model_name}")
            
            # Determine device
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            logger.info(f"Using device: {self.device}")
            
            # Load processor and model
            self.processor = BlipProcessor.from_pretrained(self.model_name)  # type: ignore
            
            if self.device == "cuda":
                self.model = BlipForConditionalGeneration.from_pretrained(
                    self.model_name,
                    torch_dtype=torch.float16,
                    device_map="auto"
                )
            else:
                self.model = BlipForConditionalGeneration.from_pretrained(
                    self.model_name,
                    torch_dtype=torch.float32
                )
                # Move model to device
                if hasattr(self.model, 'to'):
                    self.model.to(self.device)  # type: ignore
            
            # Set model to evaluation mode
            self.model.eval()
            
            logger.info("BLIP model loaded successfully!")
            
        except Exception as e:
            logger.error(f"Error loading BLIP model: {e}")
            raise
    
    def generate_caption(self, image: Image.Image) -> Optional[str]:
        """
        Generate a detailed caption for the given image.
        
        Args:
            image: PIL Image object
            
        Returns:
            Generated caption string or None if failed
        """
        try:
            if self.processor is None or self.model is None:
                logger.error("Model or processor not loaded")
                return None

            # Prepare inputs
            logger.info(f"Processing image: {image.size} {image.mode}")
            
            # For BLIP, we need to provide a text prompt for conditional generation
            text_prompt = "a photography of"
            
            inputs: Union[BatchEncoding, Dict[str, Any]] = self.processor(
                images=image,
                text=text_prompt,
                return_tensors="pt"
            )

            # Move inputs to device
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Extract required inputs with proper type checking
            input_ids = inputs.get("input_ids")
            pixel_values = inputs.get("pixel_values")
            attention_mask = inputs.get("attention_mask")
            
            # Log the available keys for debugging
            logger.info(f"Available input keys: {list(inputs.keys())}")
            
            # Validate that required inputs are present
            if pixel_values is None:
                logger.error("Required input pixel_values is missing")
                return None
            
            # Generate caption with optimized parameters for detailed descriptions
            with torch.no_grad():
                if input_ids is not None:
                    # Conditional generation with text prompt
                    outputs = self.model.generate(
                        input_ids=input_ids,
                        pixel_values=pixel_values,
                        attention_mask=attention_mask,
                        max_length=self.max_length,
                        num_beams=self.num_beams,
                        temperature=self.temperature,
                        do_sample=True,
                        top_p=0.9,
                        repetition_penalty=1.5,
                        length_penalty=1.0,
                        early_stopping=True
                    )
                else:
                    # Unconditional generation (no text prompt)
                    outputs = self.model.generate(
                        pixel_values=pixel_values,
                        max_length=self.max_length,
                        num_beams=self.num_beams,
                        temperature=self.temperature,
                        do_sample=True,
                        top_p=0.9,
                        repetition_penalty=1.5,
                        length_penalty=1.0,
                        early_stopping=True
                    )

            # Decode the generated caption
            tokenizer = getattr(self.processor, "tokenizer", None)
            if tokenizer is None:
                logger.error("Processor does not have a tokenizer attribute")
                return None
            caption = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Clean up the caption
            caption = self._clean_caption(caption)
            logger.info(f"Generated caption: {caption}")
            return caption
            
        except Exception as e:
            logger.error(f"Error generating caption: {e}")
            return None
    
    def _clean_caption(self, caption: str) -> str:
        """
        Clean and format the generated caption.
        
        Args:
            caption: Raw caption string
            
        Returns:
            Cleaned caption string
        """
        # Remove extra whitespace
        caption = " ".join(caption.split())
        
        # Capitalize first letter
        if caption:
            caption = caption[0].upper() + caption[1:]
        
        # Add period if missing
        if caption and not caption.endswith(('.', '!', '?')):
            caption += "."
        
        return caption
    
    def get_model_info(self) -> dict:
        """Get information about the loaded model."""
        return {
            "model_name": self.model_name,
            "device": self.device,
            "max_length": self.max_length,
            "num_beams": self.num_beams,
            "temperature": self.temperature
        } 