import openai

openai.api_key = "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"

while True:

    prompt = input("\n Hazme una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(  engine="text-davinci-003",
                                            prompt=prompt,
                                            max_tokens=1000)

    print(completion.choices[0].text)