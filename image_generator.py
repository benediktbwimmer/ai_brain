import requests

def generate_image(text):
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': text,
        },
        headers={'api-key': 'YOUR_API_KEY'}
    )
    return response.json()

# Elaborate text prompts to generate images for
texts = [
    "The future of technology transforming lives",
    "Chatbot with AI understanding users better",
    "A person having a meaningful conversation with an AI chatbot",
    "AI chatbot dynamically generating context based on user's conversation history",
    "A person asking the right questions to an AI and getting the best possible answers",
]

image_urls = []

for text in texts:
    result = generate_image(text)
    if result.get('output_url'):
        image_urls.append(result['output_url'])
        print(f"Generated image for '{text}': {result['output_url']}")
    else:
        print(f"Failed to generate image for '{text}'")

print("\nGenerated image URLs:")
for url in image_urls:
    print(url)
