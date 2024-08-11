import requests
from celery import shared_task
from .models import GeneratedImage
import base64
from django.core.files.base import ContentFile

STABILITY_API_URL = 'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image'
STABILITY_API_KEY = 'sk-fVY3pS7dXeVHlnNc83VWTW33wowvp2RmmroBWpzgDlkZeppL'

@shared_task
def generate_image_task(text_input):
    headers = {
        'Authorization': f'{STABILITY_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "sampler": "K_DPM_2_ANCESTRAL",
        "samples": 1,
        "steps": 30,
        "text_prompts": [
            {
                "text": text_input,
                "weight": 1
            }
        ]
    }
    response = requests.post(STABILITY_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        artifacts = response_data.get('artifacts', [])
        
        if artifacts:
            base64_image = artifacts[0].get('base64')
            if base64_image:
                # Decode the base64 image
                image_data = base64.b64decode(base64_image)

                # Create a ContentFile object for storing the image in Django's file system
                image_name = f"{text_input.replace(' ', '_')}.png"
                image_file = ContentFile(image_data, name=image_name)

                # Save the image to the database
                GeneratedImage.objects.create(text_input=text_input, image=image_file)
                return image_name
            else:
                print("No base64 image data found in response.")
        else:
            print("No artifacts found in response.")
    else:
        # Log the error for debugging purposes
        print(f"Error: {response.status_code} - {response.text}")

    return None
