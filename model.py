from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    revision="fp16",
    use_auth_token=True  # You need Hugging Face token
).to("cuda")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    filename = "generated_image.png"
    image.save(filename)
    return filename
