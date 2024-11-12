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
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    async def aux_func(turn_context):
        await on_message(turn_context)

    # raise PermissionError("Required Authorization token was not supplied")
    # await adapter.process_activity(activity, auth_header, aux_func)
    return web.Response(status=200)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=3978)