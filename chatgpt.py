import os
import openai
openai.api_key = "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"

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": "Friend: What have you been up to?\nMe: Watching old movies.\nMe: Did you wat"}
#   ],
#   temperature=1,
#   max_tokens=20,
#   top_p=1.0,
#   frequency_penalty=1,
#   presence_penalty=0.0,
#   stop=["You:"],
#   n=4
# )

# print(completion.choices[0].message.content)


# openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend: I was ",
  temperature=0.4,
  max_tokens=20,
  top_p=1.0,
  frequency_penalty=0,
  presence_penalty=0.0,
  stop=["You:"],
  n=4
)

# print(response.choices)

# s = [<OpenAIObject at 0x26debd470e0> JSON: {
#   "finish_reason": "stop",
#   "index": 0,
#   "logprobs": null,
#   "text": " watching an old classic, Casablanca. It was really good."
# }, <OpenAIObject at 0x26debd47270> JSON: {
#   "finish_reason": "length",
#   "index": 1,
#   "logprobs": null,
#   "text": " watching a classic film from the 1950s called \"Rebel Without a Cause\". It was really good"
# }, <OpenAIObject at 0x26debd6b0e0> JSON: {
#   "finish_reason": "stop",
#   "index": 2,
#   "logprobs": null,
#   "text": " watching a classic film noir called Double Indemnity. It was really good."
# }, <OpenAIObject at 0x26debd6b180> JSON: {
#   "finish_reason": "length",
#   "index": 3,
#   "logprobs": null,
#   "text": " watching some classic black and white films. I just finished watching Casablanca. It was really good"
# }]

output = []
for c in response.choices:
    output.append(c['text'])

print(output)