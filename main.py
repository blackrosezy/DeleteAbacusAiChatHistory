import os

import requests
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

# Configuration from environment
API_KEY = os.getenv("ABACUS_API_KEY", "")
DEPLOYMENT_ID = os.getenv("ABACUS_DEPLOYMENT_ID", "")
BASE_URL = "https://api.abacus.ai/api/v0"


def require_config():
    missing = []
    if not API_KEY:
        missing.append("ABACUS_API_KEY")
    if not DEPLOYMENT_ID:
        missing.append("ABACUS_DEPLOYMENT_ID")
    if missing:
        raise SystemExit(
            f"Missing required environment variable(s): {', '.join(missing)}. "
            "Create a .env file or set them in your environment."
        )


def list_conversations(deployment_id, api_key):
    """
    List all conversations for a given deployment.

    Returns:
        list: List of conversation dictionaries
    """
    url = f"{BASE_URL}/listDeploymentConversations"
    headers = {"apikey": api_key}
    params = {"deploymentId": deployment_id}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if data.get("success"):
            return data.get("result", [])
        else:
            print("Error: API returned success=false")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error listing conversations: {e}")
        return []


def delete_conversation(conversation_id, api_key):
    """
    Delete a single conversation.

    Returns:
        bool: True if successful, False otherwise
    """
    url = f"{BASE_URL}/deleteDeploymentConversation"
    headers = {"apikey": api_key}
    params = {"deploymentConversationId": conversation_id}

    try:
        response = requests.delete(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("success", False)
    except requests.exceptions.RequestException as e:
        print(f"Error deleting conversation {conversation_id}: {e}")
        return False


def main():
    require_config()
    print(f"Fetching conversations for deployment: {DEPLOYMENT_ID}")
    conversations = list_conversations(DEPLOYMENT_ID, API_KEY)

    if not conversations:
        print("No conversations found or error occurred.")
        return

    print(f"\nFound {len(conversations)} conversation(s):\n")

    # Display all conversations
    for idx, conv in enumerate(conversations, 1):
        conv_id = conv.get("deploymentConversationId")
        name = conv.get("name", "Unnamed")
        created_at = conv.get("createdAt")
        print(f"{idx}. ID: {conv_id}")
        print(f"   Name: {name}")
        print(f"   Created: {created_at}\n")

    # Ask for confirmation before deleting
    confirm = input("Do you want to delete ALL these conversations? (yes/no): ")

    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return

    # Delete all conversations
    print("\nDeleting conversations...\n")
    success_count = 0
    fail_count = 0

    for conv in conversations:
        conv_id = conv.get("deploymentConversationId")
        name = conv.get("name", "Unnamed")

        if delete_conversation(conv_id, API_KEY):
            print(f"✓ Deleted: {name} ({conv_id})")
            success_count += 1
        else:
            print(f"✗ Failed to delete: {name} ({conv_id})")
            fail_count += 1

    print("\nDeletion complete:")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {fail_count}")


if __name__ == "__main__":
    main()
