from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes

# Create adapter
adapter_settings = BotFrameworkAdapterSettings("YOUR_BOT_APP_ID", "YOUR_BOT_APP_PASSWORD")
adapter = BotFrameworkAdapter(adapter_settings)

# Define bot logic
async def on_message(context: TurnContext):
    if context.activity.type == ActivityTypes.message:
        await context.send_activity(f"You said: {context.activity.text}")

# Set up web server
async def messages(req):
    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    if not auth_header:
        return web.Response(status=401, text="Required Authorization token was not supplied")

    async def aux_func(turn_context):
        await on_message(turn_context)

    # PermissionError("Required Authorization token was not supplied")
    # The PermissionError is being triggered because the auth_header is empty when the Bot Framework Emulator sends a request without an Authorization token. The Bot Framework Adapter expects an Authorization token to be present in the request headers for authentication purposes. To fix this, we need to add a condition to check if the auth_header is empty and return a 401 Unauthorized response if it is. This will allow the Bot Framework Emulator to send requests without an Authorization token and receive a valid response from the bot.
    await adapter.process_activity(activity, auth_header, aux_func)
    return web.Response(status=200)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=3978)