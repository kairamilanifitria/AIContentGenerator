import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY


def openAIQuery(query):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=query,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Sorry, you beat the AI this time'
    else:
        answer = 'Sorry, you beat the AI this time'

    return answer 