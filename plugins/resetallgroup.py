import logging
from pyrogram import Client, filters
from info import (
    ADMINS, SHORTENER_WEBSITE, SHORTENER_API, SHORTENER_WEBSITE2, SHORTENER_API2,
    SHORTENER_WEBSITE3, SHORTENER_API3, IMDB_TEMPLATE, TUTORIAL, TUTORIAL2, TUTORIAL3,
    FILE_CAPTION, LOG_VR_CHANNEL
)
from database.users_chats_db import db
import asyncio

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='group_reset.log',  # Logs will be saved to this file
    filemode='a'
)

@Client.on_message(filters.command("resetallgrpsdata") & filters.user(ADMINS))
async def reset_all_groups_data(client, message):
    groups_cursor = db.get_all_chats()  # Get all groups from DB
    count = 0
    failed = 0

    async for grp in groups_cursor:
        grp_id = grp["id"]
        try:
            await save_group_settings(grp_id, 'shortner', SHORTENER_WEBSITE)
            await save_group_settings(grp_id, 'api', SHORTENER_API)
            await save_group_settings(grp_id, 'shortner_two', SHORTENER_WEBSITE2)
            await save_group_settings(grp_id, 'api_two', SHORTENER_API2)
            await save_group_settings(grp_id, 'shortner_three', SHORTENER_WEBSITE3)
            await save_group_settings(grp_id, 'api_three', SHORTENER_API3)
            await save_group_settings(grp_id, 'template', IMDB_TEMPLATE)
            await save_group_settings(grp_id, 'tutorial', TUTORIAL)
            await save_group_settings(grp_id, 'tutorial_two', TUTORIAL2)
            await save_group_settings(grp_id, 'tutorial_three', TUTORIAL3)
            await save_group_settings(grp_id, 'caption', FILE_CAPTION)
            await save_group_settings(grp_id, 'log', LOG_VR_CHANNEL)
            
            logging.info(f"✅ Successfully reset settings for group ID: {grp_id}")
            count += 1
        except Exception as e:
            logging.error(f"❌ Failed to reset settings for group ID: {grp_id} | Error: {e}")
            failed += 1
        
        await asyncio.sleep(0.1)  # Avoid flooding DB

    await message.reply_text(
        f"✅ Reset default settings in {count} groups.\n❌ Failed in {failed} groups."
    )