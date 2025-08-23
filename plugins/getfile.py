from utils import temp, get_poster
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

POST_CHANNELS = list(map(int, (channel.strip() for channel in environ.get('POST_CHANNELS', '-1001808193316').split(','))))

async def send_movie_details(client, chat_id, movie_details, custom_link):
    poster = movie_details.get('poster')
    movie_title = movie_details.get('title', 'N/A')
    rating = movie_details.get('rating', 'N/A')
    genres = movie_details.get('genres', 'N/A')

    # Limit genres to 4
    if isinstance(genres, (list, tuple)):
        genres = ", ".join(map(str, genres[:4])) if genres else "N/A"

    year = movie_details.get('year', 'N/A')
    imdb_link = movie_details.get('imdb_url', '') or 'https://www.imdb.com'
    movie_type = movie_details.get('type', '').lower()

    # Detect tag type
    if "series" in movie_type:
        tag_type = "#ᴍᴏᴠɪᴇ"
    elif "movie" in movie_type:
        tag_type = "#sᴇʀɪᴇs"
    else:
        tag_type = "#ᴍᴇᴅɪᴀ"

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ✅", url=custom_link)],
        [InlineKeyboardButton("♻️ ᴛᴜᴛᴏʀɪᴀʟ ♻️", url="https://t.me/links_tutorialbypp/38")]
    ])

    caption = (
        f"✅ <u>#ɴᴇᴡ_ᴍᴇᴅɪᴀ</u> ✅ | <a href='{imdb_link}'>⭐ ɪᴍᴅʙ ɪɴғᴏ</a>\n\n"
        f"<b>🔖 𝐓𝐢𝐭𝐥𝐞 :</b> {movie_title}\n"
        f"<b>🎬 𝐆𝐞𝐧𝐫𝐞𝐬 :</b> {genres}\n"
        f"<b>⭐️ 𝐑𝐚𝐭𝐢𝐧𝐠 :</b> {rating}/10\n"
        f"<b>📆 𝐘𝐞𝐚𝐫 :</b> {year}\n\n"
        f"{tag_type}"
    )

    if poster:
        await client.send_photo(
            chat_id=chat_id,
            photo=poster,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    else:
        await client.send_message(
            chat_id=chat_id,
            text=caption,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(filters.command('getfile'))
async def getfile(client, message):
    try:
        query = message.text.split(" ", 1)
        if len(query) < 2:
            return await message.reply_text("<b>Usage:</b> /getfile <movie_name>\n\nExample: /getfile Money Heist")

        file_name = query[1].strip()
        movie_details = await get_poster(file_name)

        if not movie_details:
            return await message.reply_text(f"No results found for {file_name} on IMDB.")

        custom_link = f"https://t.me/{temp.U_NAME}?start=getfile-{file_name.replace(' ', '-').lower()}"

        # Send the movie details
        await send_movie_details(client, message.chat.id, movie_details, custom_link)

        # Ask for posting confirmation
        reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Yes", callback_data=f"post_yes_{file_name}"),
                InlineKeyboardButton("No", callback_data=f"post_no_{file_name}")
            ]
        ])
        await message.reply_text("Do you want to post this content on POST_CHANNELS?", reply_markup=reply_markup)

    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")


@Client.on_callback_query(filters.regex(r'^post_(yes|no)_'))
async def post_to_channels(client, callback_query):
    try:
        _, action, file_name = callback_query.data.split('_', 2)

        if action == "yes":
            movie_details = await get_poster(file_name)
            if not movie_details:
                return await callback_query.message.reply_text(f"No results found for {file_name} on IMDB.")

            custom_link = f"https://t.me/{temp.U_NAME}?start=getfile-{file_name.replace(' ', '-').lower()}"

            for channel_id in POST_CHANNELS:
                try:
                    await send_movie_details(client, channel_id, movie_details, custom_link)
                except Exception as e:
                    await callback_query.message.reply_text(f"Error posting to channel {channel_id}: {str(e)}")

            await callback_query.message.edit_text("✅ Movie details successfully posted to channels.")

        elif action == "no":
            await callback_query.message.edit_text("❌ Movie details will not be posted to channels.")

    except Exception as e:
        await callback_query.message.reply_text(f"Error: {str(e)}")