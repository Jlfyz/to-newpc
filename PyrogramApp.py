from pyrogram import Client
from pyrogram.api import functions, types
from pyrogram.api.errors import (
    BadRequest, Flood, InternalServerError,
    SeeOther, Unauthorized, UnknownError
)
app = Client(
    "my_account",
    api_id=428227,
    api_hash='18c9cd90e3b44de1f7f323d8af49ec6b'
)
app.start()
try:
    app.send(
        functions.channels.InviteToChannel(
            channel=app.resolve_peer('Try group'),  # ID or Username
            users=[
                app.resolve_peer('@GindemoAnton')
                # app.resolve_peer('@BobbyReggieB'),
                # app.resolve_peer('@IevgeniiaKobets'),
            ]
        )
    )
    print('end')
except BadRequest as err:
    print(err)
except Flood as err:
    print(err)
except InternalServerError as err:
    print(err)
except SeeOther as err:
    print(err)
except Unauthorized as err:
    print(err)
except UnknownError as err:
    print(err)
