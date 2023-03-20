import openai

poem = """Resuma o seguinte texto em portugues: 
---
{input}
---
Este é o resumo: """

def set_openai_key():
    """Sets OpenAI key."""
    openai.api_key = "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"

class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")
        

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        
        kwargs = {
            "engine": "text-davinci-002",
            "temperature": 0.85,
            "max_tokens": 600,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["###"],
        }


        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]


        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r

    def model_prediction(self, input):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key()
        output = self.query(poem.format(input = input))
        return output