<p align="center">
  <img src="https://raw.githubusercontent.com/PatterAI/Patter/main/docs/patter-logo-banner.svg" alt="Patter" width="300" />
</p>

# Patter: Dynamic Variables

Per-call prompt personalization with `{variable}` placeholder substitution in system prompts and first messages.

> Part of the [Patter](https://github.com/PatterAI/Patter) Voice AI SDK.

## Prerequisites

- [Twilio](https://www.twilio.com/) account with a phone number
- [OpenAI](https://platform.openai.com/) API key with Realtime access

## Quick Start

### Python

```bash
cd python
cp ../.env.example .env   # fill in your keys
pip install -r requirements.txt
python main.py
```

### TypeScript

```bash
cd typescript
cp ../.env.example .env   # fill in your keys
npm install
npx tsx main.ts
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | OpenAI API key with Realtime access |
| `TWILIO_ACCOUNT_SID` | Yes | Twilio account SID |
| `TWILIO_AUTH_TOKEN` | Yes | Twilio auth token |
| `TWILIO_PHONE_NUMBER` | Yes | Your Twilio phone number (E.164) |
| `WEBHOOK_URL` | No | Public URL for webhooks (auto-tunneled if omitted) |

## What This Demonstrates

- **`variables` in `agent()`** — define default placeholder values when creating an agent
- **`{placeholder}` syntax** — use `{customer_name}`, `{account_number}`, etc. in system prompts and first messages
- **`on_call_start` returning variable overrides** — dynamically swap variables per caller at runtime
- **Per-caller personalization** — look up caller info from a database and inject it into the conversation

## How It Works

1. Define an agent with `{variable}` placeholders in the system prompt and first message
2. Provide default values via the `variables` parameter
3. When a call comes in, `on_call_start` looks up the caller in a database
4. If found, return `{"variables": {...}}` to override defaults for that specific call
5. Patter substitutes all placeholders before the conversation begins

## Next Steps

- [Inbound Agent](https://github.com/PatterAI/patter-inbound-agent) — minimal inbound voice agent
- [Custom LLM](https://github.com/PatterAI/patter-custom-llm) — bring your own LLM
- [Production Setup](https://github.com/PatterAI/patter-production) — full production configuration
- [Full documentation](https://docs.getpatter.com)
- [All templates](https://github.com/PatterAI/Patter#templates)

## License

MIT
