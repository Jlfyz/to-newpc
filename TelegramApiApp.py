from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputChannel, InputUser
from telethon.errors.rpcerrorlist import UsernameInvalidError, UserNotMutualContactError
from time import sleep
from telethon.errors.rpcerrorlist import UserIdInvalidError
import asyncio
import telethon.sync
api_id = 428227
api_hash = '18c9cd90e3b44de1f7f323d8af49ec6b'
phone_number = '+380675141407'
client = TelegramClient('Go_on', api_id, api_hash).start()


async def main():
    await client.connect()
    if not await client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))
    channel = await client.get_entity('https://t.me/qwertyuiop1234567890')  #channel_ id https://t.me/bloXrouteLabsCommunity
    users_in_channel = await client.get_participants('https://t.me/qwertyuiop1234567890')  #channel id or https://t.me/ncent
    print(users_in_channel)

    def is_in_group(username):
        if username in users_in_channel:
            return True
        else:
            return False

    with open('im.txt', 'r') as f:  # file with list of usernames
        for line in f:
            print(line)
            tmp = line[1:].replace('\n', '')
            print(tmp)
            try:
                user = client.get_input_entity(tmp)  # (ResolveUsernameRequest(tmp))
                print(user)
            except UsernameInvalidError as err:
                print(err)
                continue
            if user:
                try:
                    sleep(301)
                    client.invoke(InviteToChannelRequest(InputChannel(channel.id, channel.access_hash),
                                                                [InputUser(user.user_id, user.access_hash)]))
                except UserNotMutualContactError as err:
                    print(err)
                except UserIdInvalidError as err:
                    print(err)
            else:
                continue
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
"""@BevzenkoA
@BobbyReggieB
@IevgeniiaKobets
@LarsMathiasRoth
@OlaSebastianSelby
@Tetiana92713958
@Volodym81570905
@Serhii88849557
@LEVINEW_QUINN
@e1ectromind 
@AndreiStefanIo1
@EricAdamPaulFrankenius
@AlfieJackson_Potter
@Prebensen2
@Knutsen79922074
@milkytwilight
@zacharynicholson
@GindemoAnton
@Marsh09331591
@Marsh09331591
@Walters97894779
@benebi
@Austin03120466
@Gdenargi
@oskar_marcus
@xMac73
@skateordie2
@barcelonaman
@lovenastyamuch
@dancetojoydivision
@Chamber31368162
@rep19
@JimmyPe91684253
@rep18
@reppo19
@rusrus82
@grant_grant
@newstuff13
@linamyakinina
@cryptogalaxy8
@Oleksii_Andrieiev
@bestby13
@proteinpoint
@scrooge13
@Kristya18
@caption1313
@Brynjar96952253
@Oliver10802973
@DavidGustav9"""