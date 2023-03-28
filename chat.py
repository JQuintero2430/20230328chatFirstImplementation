import openai

openai.api_key = "API_KEY"

while True:

    prompt = input("\nEnter a question: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          n=1,
                                          max_tokens=4000)

    print(completion.choices[0].text)
