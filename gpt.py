import os
import openai

# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
  """
  Sends the prompt to OpenAI's GPT-3 model and returns the generated response.
  """
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
  )
  return response.choices[0].text

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  while True:
    user_input = input("You: ")
    if user_input == "quit":
      break
    response = generate_response(user_input)
    print("Bot:", response)

