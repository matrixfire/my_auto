'''
testing:
接口地址：https://vip-hk-s1.zeabur.app
APIkey：sk-TDF6zgxVQqAfYNYuE2Eb3334F13d4d9780594dAa6eF364C5

my_paid = "sk-G4C6rzryzKe7fzUN2c65553694454dD9915eC1DeDb0fA128"

gpt-4-1106-preview

dall-e-3

'''

from openai import OpenAI
import pyperclip as p
import time

def chat_gpt_openai_old(content):
    api_key = 'sk-G4C6rzryzKe7fzUN2c65553694454dD9915eC1DeDb0fA128'
    api_base = 'https://vip-hk-s1.zeabur.app/v1'

    client = OpenAI(api_key=api_key, base_url=api_base)

    rsp = client.chat.completions.create(
        model='gpt-4-1106-preview',
        messages=[
            {"role": "user", "content": content}
        ],
        temperature=0,
        stream=True,
        timeout=600
    )
    
    text = ''
    for chunk in rsp:
        if chunk.choices[0].finish_reason is None and chunk.choices[0].delta.content is not None:
            text += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    
    return text



def chat_gpt_openai(content, conversation_history=[]):
    # API key for authentication
    api_key = 'sk-G4C6rzryzKe7fzUN2c65553694454dD9915eC1DeDb0fA128'
    # Base URL for the OpenAI API endpoint
    api_base = 'https://vip-hk-s1.zeabur.app/v1'
    
    # Initialize the OpenAI client with the API key and base URL
    client = OpenAI(api_key=api_key, base_url=api_base)
    
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": content})
    
    # Limit the context to the last few messages if necessary
    # This can be adjusted based on the length of conversation you want to keep
    context_to_send = conversation_history[-10:]  # Keep only the last 10 messages in the context
    
    # Make a request to the OpenAI API to generate a response
    rsp = client.chat.completions.create(
        model='gpt-4-1106-preview',  # Model to use for generating the response
        messages=context_to_send,  # Context (conversation history) to send with the request
        temperature=0,  # Temperature setting for response generation (0 = deterministic)
        # max_tokens=50,  # Limit the response to 50 tokens to save API quota
        stream=True,  # Stream the response as it is generated
        timeout=600  # Timeout setting for the request (in seconds)
    )
    
    text = ''  # Initialize an empty string to hold the response text
    for chunk in rsp:
        # Check if the response chunk is still being generated and has content
        if chunk.choices[0].finish_reason is None and chunk.choices[0].delta.content is not None:
            text += chunk.choices[0].delta.content  # Append the content to the response text
            print(chunk.choices[0].delta.content, end="")  # Print the content as it is received
    
    # Add the assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": text})
    
    return text, conversation_history  # Return the response text and updated conversation history

conversation_history = []  # Initialize an empty conversation history

# Example interaction
response, conversation_history = chat_gpt_openai("Hello, My name is Bill, how are you?", conversation_history)
print("\nResponse:", response)

time.sleep(5)
# Another interaction
response, conversation_history = chat_gpt_openai("Can you write me an email express you wanna connect with me on linkedin?", conversation_history)
print("\nResponse:", response)


p.copy(response)






import requests

def send_chat_completion(api_key, message_content):
    url = "https://api.deepbricks.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "user",
                "content": message_content
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Example usage
api_key = "sk-NpvUEGWHfd45VYyaOXwhWA40xZsHCrOg98SbdKleI4BJv320"
message = "Hello!"
response = send_chat_completion(api_key, message)
print(response)

















# content = '''
# I want you to act as my friend. 
# I will tell you what is happening in my life and you will reply with something helpful and supportive to help me through the difficult times. Do not write any explanations, just reply with the advice/supportive words, which reply you limited words within 30 words at most. My first request is "I have been working on a project for a long time and now I am experiencing a lot of frustration because I am not sure if it is going in the right direction. 
# Please help me stay positive and focus on the important things."

# '''
# content = "Can u tell me more ?"
# answer = chat_gpt_openai(content)
# print(answer)

# p.copy(answer)













'''
按量计费费用 = 分组倍率 × 模型倍率 × （提示token数 + 补全token数 × 补全倍率）/ 500000 （单位：美元）
The fee based on usage = Group Rate × Model Rate × (Prompt token count + Completion token count × Completion Rate) / 500,000 (unit: US dollars).

group_rate = 1
model_rate = {
    "gpt-3.5-turbo": 0.75,
    "gpt-3.5-turbo-0301": 0.75,
    "gpt-3.5-turbo-0613": 0.75,
    "gpt-3.5-turbo-1106": 0.5,
    "gpt-3.5-turbo-16k": 1.5,
    "gpt-3.5-turbo-16k-0613": 1.5,
    "gpt-3.5-turbo-instruct": 0.75,
    "gpt-4": 15,
    "gpt-4-0314": 15,
    "gpt-4-0613": 15,
    "gpt-4-1106-preview": 5,
    "gpt-4-32k": 30,
    "gpt-4-32k-0314": 30,
    "gpt-4-32k-0613": 30,
    "gpt-4-vision-preview": 5
}


completion_rate = {
    "gpt-3.5-turbo": 3,
    "gpt-3.5-turbo-0125": 3,
    "gpt-3.5-turbo-0301": 3,
    "gpt-3.5-turbo-0613": 3,
    "gpt-3.5-turbo-1106": 3,
    "gpt-3.5-turbo-16k": 1.33,
    "gpt-3.5-turbo-16k-0613": 1.3333,
    "gpt-3.5-turbo-instruct": 1.3333,
    "gpt-3.5-turbo-instruct-0914": 1.3333,
    "gpt-4": 2,
    "gpt-4-0125-preview": 3,
    "gpt-4-0314": 2,
    "gpt-4-0613": 2,
    "gpt-4-1106-preview": 3,
    "gpt-4-32k": 2,
    "gpt-4-32k-0314": 2,
    "gpt-4-32k-0613": 2,
    "gpt-4-turbo-preview": 3,
    "gpt-4-vision-preview": 3,
}




'''