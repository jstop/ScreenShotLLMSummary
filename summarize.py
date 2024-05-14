import sys
from openai import OpenAI

client = OpenAI()

data = sys.stdin.read()

# Test/Debug lines
#print("Input:\n\n")
#print(data)

prompts = {
    "summarize": "The following text was extracted from a screen capture and may have a strange pattern do to the positioning of words on the screen. Can you explain what you think could be going on based on the text provided?\n\n"
}

prompt = f"{prompts['summarize']}"

summary_response = client.chat.completions.create(model="gpt-4-turbo-2024-04-09",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt},
      {"role": "system", "content": "Of course! Please provide the text that you'd like me to analyze."},
      {"role": "system", "content": data},
    ]
)

# Test/Debug lines
#print("\n\nSummary:\n\n")
print(summary_response.choices[0].message.content)

