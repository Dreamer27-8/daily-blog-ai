# ✅ Install the Gemini SDK (do this once)
!pip install google-generativeai --quiet

# ✅ Import libraries
import google.generativeai as genai
import requests
from datetime import datetime

# ✅ Set your Gemini API key
genai.configure(api_key="AIzaSyA5AK6OCnJa5Fn7Pkn4JL3vSeEij5zcxv8")

# ✅ Use the correct free Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Prompt for blog post generation
prompt = """
Write a blog post on today's trending Indian and international news.
Focus on Indian market, economy, politics, global impact.
Use engaging title, bullet points, and make it clear for readers.
"""

# ✅ Generate blog content
response = model.generate_content(prompt)
content = response.text
print("✅ Blog content generated!\n")
print(content)
print("\n\n---\n\n")

# ✅ WordPress credentials
site_url = "https://nextgenearnings.in"
username = "rakeshvetkuri27@gmail.com"
application_password = "hKjn qKEY SedX yfz4 ELgO 7mAn"

# ✅ Prepare blog post details
today = datetime.now().strftime("%Y-%m-%d")
title = f"Top News Headlines - {today}"

# ✅ WordPress API endpoint
api_url = f"{site_url}/wp-json/wp/v2/posts"

# ✅ Data to send
data = {
    "title": title,
    "content": content,
    "status": "publish"
}

# ✅ Send POST request to WordPress
response = requests.post(api_url, auth=(username, application_password), json=data)

# ✅ Show result
if response.status_code == 201:
    print("✅ Blog post published successfully!")
    print("🔗 Post URL:", response.json().get("link"))
else:
    print("❌ Failed to publish blog post")
    print("Status Code:", response.status_code)
    print("Response:", response.text)

