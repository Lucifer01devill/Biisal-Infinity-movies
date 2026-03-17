import logging
import asyncio
from pyrogram import Client, filters
from info import ADMINS
from database.users_chats_db import db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='group_reset.log',
    filemode='a'
)

@Client.on_message(filters.command("resetallgrpsdata") & filters.user(ADMINS))
async def reset_all_groups_data(client, message):
    groups_cursor = await db.get_all_chats()  # Async cursor to all groups
    count = 0
    failed = 0

    total_groups = await db.total_chat_count()

    # Send initial status message
    status_msg = await message.reply_text(
        f"♻️ Resetting all group settings...\nProcessed: 0/{total_groups}\n✅ Success: 0\n❌ Failed: 0"
    )

    async for grp in groups_cursor:
        grp_id = grp["id"]
        try:
            # Reset to default settings
            await db.update_settings(grp_id, db.default)
            logging.info(f"✅ Reset settings for group ID: {grp_id}")
            count += 1
        except Exception as e:
            logging.error(f"❌ Failed to reset settings for group ID: {grp_id} | Error: {e}")
            failed += 1

        # Update status message
        await status_msg.edit_text(
            f"♻️ Resetting all group settings...\n"
            f"Processed: {count + failed}/{total_groups}\n"
            f"✅ Success: {count}\n"
            f"❌ Failed: {failed}"
        )

        await asyncio.sleep(0.1)  # Prevent DB flooding

    # Final update
    await status_msg.edit_text(
        f"✅ Reset complete!\n"
        f"Total groups processed: {total_groups}\n"
        f"✅ Success: {count}\n"
        f"❌ Failed: {failed}"
    )