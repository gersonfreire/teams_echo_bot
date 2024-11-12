from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes

class CustomBotFrameworkAdapter(BotFrameworkAdapter):
    async def process_activity(self, activity, auth_header, logic):
        try:
            # Bypass Authorization check for local testing
            if auth_header == "Bypass":
                return await logic(TurnContext(self, activity))
            return await super().process_activity(activity, auth_header, logic)
        except Exception as e:
            print(f"Error in process_activity: {e}")
            # raise e

# Create adapter
adapter_settings = BotFrameworkAdapterSettings("YOUR_BOT_APP_ID", "YOUR_BOT_APP_PASSWORD")
adapter = CustomBotFrameworkAdapter(adapter_settings)

# Define bot logic
async def on_message(context: TurnContext):
    if context.activity.type == ActivityTypes.message:
        await context.send_activity(f"You said: {context.activity.text}")

# Set up web server
async def messages(req):
    try:
        body = await req.json()
        activity = Activity().deserialize(body)
        auth_header = req.headers.get("Authorization", "")

        # Bypass Authorization check for local testing
        if not auth_header:
            print("Warning: Authorization token not supplied. Bypassing for local testing.")
            auth_header = "Bypass"

        async def aux_func(turn_context):
            await on_message(turn_context)

        await adapter.process_activity(activity, auth_header, aux_func)
        return web.Response(status=200)
    except Exception as e:
        print(f"Error processing activity: {e}")
        return web.Response(status=500, text=str(e))

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=3978)