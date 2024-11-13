Creating a simple Microsoft Teams bot in Python that echoes user input involves several steps. Here’s a step-by-step guide to get it set up using the Microsoft Bot Framework and Azure Bot Services.

### Prerequisites

1. **Azure Account**: You’ll need an Azure account to register and host your bot.
2. **Python and Flask**: Ensure Python is installed on your machine. Flask is a lightweight web framework to handle incoming requests.

### Step 1: Set Up the Bot Framework SDK for Python

1. **Create a Python Virtual Environment**:

   ```bash
   python -m venv my_teams_bot_env
   source my_teams_bot_env/bin/activate  # On Windows, use my_teams_bot_env\Scripts\activate
   ```
2. **Install the Bot Framework SDK for Python**:

   ```bash
   pip install botbuilder-core botbuilder-schema botbuilder-integration-aiohttp
   ```

### Step 2: Create the Bot’s Code

1. **Create a `bot.py` file** with the following code. This code will create a bot that listens to incoming messages and echoes back what the user typed.

   ```python
   import os
   from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
   from botbuilder.schema import Activity
   from aiohttp import web
   from dotenv import load_dotenv

   load_dotenv()  # Load environment variables

   APP_ID = os.getenv("MICROSOFT_APP_ID")
   APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD")

   # Initialize Bot Framework Adapter
   adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
   adapter = BotFrameworkAdapter(adapter_settings)

   # Define the echo bot
   async def on_message_activity(turn_context: TurnContext):
       received_text = turn_context.activity.text
       await turn_context.send_activity(f"You said: {received_text}")

   # Set up the bot's main request handler
   async def messages(request):
       if "application/json" in request.headers["Content-Type"]:
           body = await request.json()
       else:
           return web.Response(status=415)

       activity = Activity().deserialize(body)
       auth_header = request.headers["Authorization"] if "Authorization" in request.headers else ""

       response = await adapter.process_activity(activity, auth_header, on_message_activity)
       return web.Response(status=response.status)

   app = web.Application()
   app.router.add_post("/api/messages", messages)

   if __name__ == "__main__":
       web.run_app(app, host="0.0.0.0", port=3978)
   ```
2. **Environment Variables**: Create a `.env` file in the same directory to store your Microsoft Bot credentials:

   ```plaintext
   MICROSOFT_APP_ID=your-app-id
   MICROSOFT_APP_PASSWORD=your-app-password
   ```

### Step 3: Register Your Bot on Azure

1. Go to the [Azure Portal](https://portal.azure.com/) and search for **Azure Bot**.
2. Click **Create** and fill out the bot’s details, choosing **Bot Channels Registration** as the service type.
3. After the bot is created, go to **Settings** and find **Microsoft App ID** and **Microsoft App Password**. These values go into your `.env` file under `MICROSOFT_APP_ID` and `MICROSOFT_APP_PASSWORD`.
4. Under **Channels**, add **Microsoft Teams** to your bot so that it can communicate with Teams users.

### Step 4: Run the Bot Locally

1. **Run the bot**:

   ```bash
   python bot.py
   ```
2. **Expose Your Bot with Ngrok**:

   - Microsoft Teams needs a public URL to communicate with your bot. Use **ngrok** to expose your local bot:
     ```bash
     ngrok http 3978
     ```
   - Copy the `https` URL from ngrok, which will look like `https://<ngrok-id>.ngrok.io`.
3. **Update the Messaging Endpoint in Azure**:

   - Go back to your Azure Bot configuration, and update the **Messaging endpoint** to your ngrok URL followed by `/api/messages` (e.g., `https://<ngrok-id>.ngrok.io/api/messages`).

### Step 5: Test Your Bot in Microsoft Teams

1. **Add the Bot to Microsoft Teams**:
   - Go to Microsoft Teams, click on **Apps** and search for **Developer Portal**.
   - Inside the Developer Portal, create a new app and under **Capabilities**, select **Bot**.
   - Use your Azure Bot’s App ID here and add the bot.
2. **Test the Bot**:
   - In Teams, open a chat with your bot, and it should respond with an echo of anything you type.

### Summary

You now have a working Teams bot in Python that echoes back user messages.
