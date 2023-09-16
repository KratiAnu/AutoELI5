#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import requests
openai.api_type = "azure"
openai.api_base = ""
openai.api_version = ""
openai.api_key = ""

response = openai.Completion.create(
  engine="gpt-35-turbo",
  prompt="""You are a generative AI Bot, which explains topics in simple 4 steps. Each step is described in detail each sentence must end with a full stop. 

Also specify how can it be represented by images and if images are possible for each step.
For Example:
##START
Topic: Water Cycle
Explanation: 
1. Evaporation: The water cycle begins with the sun's energy heating up water in rivers, lakes, oceans, and even puddles. As the water heats up, it turns into water vapor or steam and rises into the atmosphere.
2. Condensation: In the atmosphere, the water vapor cools down and condenses into tiny water droplets or ice crystals. These tiny droplets come together to form clouds.
3. Precipitation: When the water droplets in clouds become too heavy to stay suspended, they fall to the ground as precipitation. Precipitation can take various forms, such as rain, snow, sleet, or hail, depending on temperature conditions.
4. Collection: Precipitation that falls on the land flows into rivers, streams, and eventually into lakes and oceans, or it may be absorbed into the ground. This collected water then becomes available for various uses, including drinking, irrigation, and supporting ecosystems. Some of it also evaporates again, continuing the cycle.

Image Info: Info
1. Evaporation: Picture of rivers, streams, and lakes receiving water from precipitation.
2. Condensation: A diagram showing water flowing into underground aquifers.
3. Precipitation: Image of people using collected water for various purposes like drinking, irrigation, and agriculture.
4. Collection: Illustration of some collected water evaporating from surface bodies back into the atmosphere.
##END

##START
Topic: Gravity
Explanation:
1. Attraction of Masses: Gravity is the force of attraction that exists between any two objects with mass. The larger the mass of an object, the stronger its gravitational pull.
2. Inverse Square Law: Gravity follows the inverse square law, which means that the force of gravity weakens with distance. As objects move farther apart, the gravitational force between them decreases rapidly.
3. Center of Mass: Gravity acts as if it originates from the center of mass of an object. In the case of the Earth, gravity pulls objects toward its center, which is why things fall towards the ground.
4. Universal Force: Gravity is a universal force that affects all objects with mass. It is responsible for keeping celestial bodies like planets in orbit around the Sun and the Moon in orbit around Earth.

Image Info: Info
1. Attraction of Masses: A figure showing two objects (e.g., two balls) with arrows pointing toward each other, representing the force of gravity pulling them together.
2. Inverse Square Law: A figure comparing two objects of different sizes or masses, with one having a stronger gravitational pull. This could be shown by larger arrows or lines representing gravity.
3. Center of Mass: Earth with a falling object toward its center.
4. Universal Force: Earth, Moon, and Sun with connecting arrows showing their gravitational relationship.
##END

##START
Topic: Solar System
Explanation:
""",
  temperature=1,
  max_tokens=300,
  top_p=0,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["##END"])


# print the response    
print(response.choices[0]['text'])
output = response.choices[0]['text'].split('\n')

#print(output)

final_output = []
image_output = []
img_out = False

for a in output:
    if(a is None or len(a.split(': '))<2):
       continue
    if(a.split(': ')[1]=='Info'):
        img_out = True
    if(img_out):
        image_output.append(a.split(': ')[1])
    else:
        final_output.append(a.split(': ')[1])

print(final_output)
print("---------------------------break--------------------------------------------")
image_output.pop(0)
print(image_output)

cur = 0

for img_prompt in image_output:
    img_response = openai.Image.create(
    prompt='Draw the figure with no text labels ' + img_prompt,
    size='512x512',
    n=1)

    image_url = img_response["data"][0]["url"]
    print(image_url)
    cur+=1

    img_data = requests.get(image_url).content
    with open('image_name' + str(cur) + 'ss'+'.jpg', 'wb') as handler:
        handler.write(img_data)




#dall-E
#get the images now
