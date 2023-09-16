#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import requests

openai.api_type = "azure"
openai.api_base = ""
openai.api_version = ""
openai.api_key = ""

# print the response    
img_response = openai.Image.create(
    prompt='Illustration of some collected water evaporating from surface bodies back into the atmosphere without text',
    size='256x256',
    n=2
)

image_url = img_response["data"][0]["url"]
image_url2 = img_response["data"][1]["url"]
print(image_url)
print(image_url2)


img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)



# img_response = requests.get(image_url)
# in_memory_file = io.BytesIO(img_response.content)
# im = Image.open(in_memory_file)
# im.show()




#dall-E
#get the images now




