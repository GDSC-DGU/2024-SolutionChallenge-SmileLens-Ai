from openai import OpenAI
import base64

client = OpenAI(api_key='[API_KEY_넣기]')

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# image_path = "C:/Users/CILab/Desktop/sample/gojisu.jpg"
# image_path="C:/Users/CILab/Desktop/sample/name.jpg"
image_path="C:/Users/CILab/Desktop/sample/product.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

# GPT 모델에 메시지 보내기
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "이 제품설명서를 요약해서 알려줘! 노인분들이 이해할 수 있도록 쉽고 정확하게"
                    # "text": "이 이미지를 한국어로 요약해서 표로 이쁘게 만들어줘. 사람들이 관심있을만한 자료는 표로도 만들어줘. 이미지에서 확인하지말고 글에 내용이 포함이 되어야해"
                    #"text": "이 이미지를 한국어로 요약헤서 표로 이쁘게 만들어줘. 금액, 납부기한, 지로번호는 꼭 포함해줘."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=500
)

answer = response.choices[0].message.content
print(answer)
