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

3) Run:
```shell
python main.py
```

What it does
- Loads `ABACUS_API_KEY` (get from https://abacus.ai/app/profile/apikey) and `ABACUS_DEPLOYMENT_ID` from .env
- Lists all conversations for the deployment
- Asks: `Do you want to delete ALL these conversations? (yes/no)`
- If yes, deletes them and prints results

Troubleshooting
- If it says variables are missing, check your .env