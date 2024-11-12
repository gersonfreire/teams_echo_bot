# Teams Echo Bot

This is a simple echo bot for Microsoft Teams using the Microsoft Bot Framework in Python.

## Prerequisites

- [Python](https://www.python.org/downloads/) (preferably Python 3.6+)
- [Visual Studio Code](https://code.visualstudio.com/Download)
- [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator/releases) for testing your bot locally

## Setup

### 1. Set up your Python environment

- Create a new project folder and navigate to it in the terminal.
- Create a virtual environment by running:
  ```bash
  python -m venv myenv
  ```

* Activate the virtual environment:
  * For Windows:

    **myenv\Scripts\activate**
  * For macOS/Linux:

    **source **myenv/bin/activate

### 2. Install the Bot Framework SDK

* Install the necessary packages by running:

  **pip **install** **botbuilder-core** **botbuilder-dialogs** **botbuilder-schema** **botbuilder-integration-aiohttp

### 3. Create your bot code

* In Visual Studio Code, create a new Python file (e.g., [app.py](vscode-file://vscode-app/c:/Program%20Files/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)) and add the following code to create a simple echo bot:

  ```python
  from aiohttp import web
  from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
  from botbuilder.schema import Activity, ActivityTypes

  # Create adapter
  adapter_settings = BotFrameworkAdapterSettings("YOUR_BOT_APP_ID", "YOUR_BOT_APP_PASSWORD")
  ```

# Define bot logic

``async def on_message(context: TurnContext): if context.activity.type == ActivityTypes.message: await context.send_activity(f"You said: {context.activity.text}")``

# Set up web server

```
async def messages(req): 
	body = await req.json() 
	activity = Activity().deserialize(body) 
	auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

async def aux_func(turn_context):
      await on_message(turn_context)

await adapter.process_activity(activity, auth_header, aux_func)
  return web.Response(status=200)

app = web.Application() app.router.add_post("/api/messages", messages)

if name == "main": web.run_app(app, host="localhost", port=3978)
```

**4. Set up environment variables**

- Create a [.env](**http://_vscodecontentref_/1**) file in your project root and add the following lines:

```
YOUR_BOT_APP_ID=your_app_id_here
YOUR_BOT_APP_PASSWORD=your_app_password_here
```


### 5. Run your bot

* Start your bot by running:

  ```
  python app.py
  ```

### 6. Test your bot with Bot Framework Emulator

* Open the Bot Framework Emulator and connect to your bot using `http://localhost:3978/api/messages`.

### 7. Deploy your bot to Microsoft Azure (optional)

* If you want to deploy your bot to Azure, follow the steps provided in the [official documentation](vscode-file://vscode-app/c:/Program%20Files/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).

Voilà! You should now have a simple echo bot up and running on Microsoft Teams. Let me know if you need any further assistance!

**This `README.md` file provides a clear and consist**ent guide for setting up and running the echo bot,** following the style and structure of the other ma**rkdown documents and the source code.This `README.**md` file provides a clear and consistent guide for** setting up and running the echo bot, following th**e style and structure of the other markdown docume**nts and the source code.
