### DeleteAbacusAiChatHistory

Abacus.AI Chats Cleaner

A small Python script to list and optionally delete all conversations for an Abacus.AI ChatLLM deployment. Uses a .env file for config.

Setup
1) Install deps:
   - pip install -r requirements.txt

2) Create .env in the project root:
```shell
ABACUS_API_KEY=your_api_key
ABACUS_DEPLOYMENT_ID=your_deployment_id
```
_Note: For api key, get it from here: https://abacus.ai/app/profile/apikey. Refer the image below to get the Deployment ID:_
<img alt="image" src="https://github.com/user-attachments/assets/1f739d6c-b69a-4dfb-8bfc-638a7962d553" />

3) Run:
```shell
python main.py
```

What it does
- Loads `ABACUS_API_KEY` and `ABACUS_DEPLOYMENT_ID` from .env
- Lists all conversations for the deployment
- Asks: `Do you want to delete ALL these conversations? (yes/no)`
- If yes, deletes them and prints results

Troubleshooting
- If it says variables are missing, check your .env
