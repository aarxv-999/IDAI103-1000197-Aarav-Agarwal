import google.generativeai as genai

genai.configure(api_key="insert_api_key_here") # <- please put your API key here
model = genai.GenerativeModel("gemini-1.5-flash")

#getting data from the user for the prompt
body_type = input("Please enter your body type: ")
style_preference = input("Please enter your style preference: ")
occasion = input("Please enter the occasion you want this outfit for: ")
gender = input("Please enter your gender (e.g., male, female, non-binary): ")

user_input = {
    "body_type": body_type,
    "style_preference": style_preference,
    "occasion": occasion,
    "gender": gender
}

prompt = (
    f"Suggest a {user_input['style_preference']} outfit for someone with a {user_input['body_type']} "
    f"body type, suitable for a {user_input['occasion']} occasion, and who identifies as {user_input['gender']}. "
    "Provide a list of outfit items, using bullet points for each item. Keep it short and concise."
    "Each item should have a concise short note of its purpose and how it contributes to the overall outfit."
    "Also, please remove the bold formatting from the response."
)

# Generate content with bullet points
response = model.generate_content(prompt)

# Output the result
print(response.text)
