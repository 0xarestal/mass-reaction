import aiohttp
import asyncio
from colorama import Fore

async def send_reaction(token, channel_id, message_id, emoji):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
    headers = {
        "Authorization": "Bot " + token
    }
    async with aiohttp.ClientSession() as session:
        async with session.put(url, headers=headers) as response:
            if response.status == 204:
                print(Fore.GREEN + f"Reacted with token: {token}")
            else:
                print(Fore.BLUE + f"Failed with token: {token}, Status Code: {response.status}")

async def main():
    with open("tokens.txt", "r") as file:
        tokens = [line.strip() for line in file]

    channel_id = input(Fore.CYAN + "Channel ID -> ")
    message_id = input(Fore.CYAN + "Message ID -> ")
    emoji = input(Fore.CYAN + "Paste the emoji -> ")

    tasks = []
    for token in tokens:
        task = send_reaction(token, channel_id, message_id, emoji)
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
