def build_prompt(product_name, description, platform, tone, temperature):
    prompt = f"""
You are an expert copywriter.

Create a {platform} marketing copy for the following product.

Product Name:
{product_name}

Product Description:
{description}

Tone:
{tone}

Temperature:
{temperature}

Requirements:
- Make it engaging.
- Keep the tone consistent.
- Add emojis if suitable.
- End with a strong call-to-action.
"""

    return prompt
    