To test your Microsoft Teams bot locally using the **Microsoft Bot Framework Emulator**, you can follow these steps:

### Prerequisites

1. **Microsoft Bot Framework Emulator**: [Download and install](https://github.com/microsoft/BotFramework-Emulator/releases) the Bot Framework Emulator.

### Step 1: Run the Bot Locally

1. **Ensure your bot is running locally**:

   ```bash
   python bot.py
   ```

   This will start your bot server on `http://localhost:3978`.

### Step 2: Set Up Ngrok

Microsoft Bot Framework Emulator can communicate directly with local endpoints, but for testing with Microsoft identity services (i.e., using `MICROSOFT_APP_ID` and `MICROSOFT_APP_PASSWORD`), you need a public HTTPS URL. You can achieve this by using **ngrok**:

1. **Start ngrok** on the same port your bot is running (3978):
   ```bash
   ngrok http 3978
   ```
2. **Copy the HTTPS URL** provided by ngrok, which should look like `https://<ngrok-id>.ngrok.io`.

### Step 3: Configure the Bot Framework Emulator

1. **Open the Bot Framework Emulator**.
2. **Create a New Bot Configuration**:

   - Go to **File > Open Bot**.
   - Enter the **Bot URL** in this format:
     ```plaintext
     https://<ngrok-id>.ngrok.io/api/messages
     ```
   - If your bot is using authentication (i.e., `MICROSOFT_APP_ID` and `MICROSOFT_APP_PASSWORD`), enter these in the **Microsoft App ID** and **Microsoft App Password** fields.
3. **Connect**: Click **Connect** to initiate communication with your bot.

### Step 4: Test the Bot in the Emulator

1. Once connected, type a message in the emulator’s chat window.
2. The bot should respond by echoing the message back, following the logic defined in `bot.py`.

### Additional Notes

- **Testing Without Ngrok**: If your bot doesn’t use `MICROSOFT_APP_ID` and `MICROSOFT_APP_PASSWORD`, you can set the bot URL to `http://localhost:3978/api/messages` directly in the emulator.
- **Ngrok for HTTPS Only**: The emulator supports localhost endpoints directly if authentication is not required. Ngrok is only necessary if you need HTTPS and authentication.

By following these steps, you can test your bot’s functionality locally and make sure everything works before deploying to Teams.
