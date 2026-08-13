import json
import os
import requests

# Dictionary mapping Vue project slugs to their Facebook Page details
BOT_CONFIGURATIONS = {
    "alien-romance": {
        "page_id": "ThisAlienRomance",
        "token_env": "ALIEN_ROMANCE_BOT_TOKEN"
    },
    "waifu": {
        "page_id": "ThisWaifuDoesNotExist", 
        "token_env": "WAIFU_BOT_PAGE_TOKEN"
    },
    "cat": {
        "page_id": "ThisCatDoesNotExistBot", 
        "token_env": "CAT_BOT_PAGE_TOKEN"
    }
}

JSON_OUTPUT_PATH = "public/posts.json"

def fetch_recent_posts(page_id: str, access_token: str, limit: int = 5) -> list:
    """Fetch recent posts for a specific Facebook Page using Graph API."""
    url = f"https://graph.facebook.com/v19.0/{page_id}/published_posts"
    params = {
        'access_token': access_token,
        'fields': 'id,message,created_time,full_picture,permalink_url',
        'limit': limit
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json().get('data', [])
        
        formatted_posts = []
        for item in data:
            formatted_posts.append({
                'id': item.get('id'),
                'date': item.get('created_time', '')[:10],
                'content': item.get('message', 'No text content'),
                'image': item.get('full_picture', None),
                'url': item.get('permalink_url', '#')
            })
        return formatted_posts

    except Exception as e:
        print(f"Error fetching posts for {page_id}: {e}")
        return []

def update_bot_json(target_slug: str = None):
    """
    Updates public/posts.json. 
    If target_slug is provided, only updates that specific bot.
    If target_slug is None, updates all configured bots.
    """
    # Load existing JSON if it exists to avoid overwriting unrelated bot data
    existing_data = {}
    if os.path.exists(JSON_OUTPUT_PATH):
        try:
            with open(JSON_OUTPUT_PATH, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = {}

    configs_to_run = (
        {target_slug: BOT_CONFIGURATIONS[target_slug]} 
        if target_slug and target_slug in BOT_CONFIGURATIONS 
        else BOT_CONFIGURATIONS
    )

    for slug, config in configs_to_run.items():
        token = os.getenv(config["token_env"])
        if not token:
            print(f"Skipping '{slug}': Environment variable '{config['token_env']}' is not set.")
            continue
            
        print(f"Syncing posts for '{slug}'...")
        posts = fetch_recent_posts(config["page_id"], token)
        existing_data[slug] = posts

    # Ensure the public directory exists and save
    os.makedirs(os.path.dirname(JSON_OUTPUT_PATH), exist_ok=True)
    with open(JSON_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=2)
        
    print(f"Updated {JSON_OUTPUT_PATH} successfully!")

if __name__ == "__main__":
    # When run directly from terminal, sync all configured bots
    update_bot_json()