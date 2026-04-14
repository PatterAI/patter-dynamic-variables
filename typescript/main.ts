/**
 * Per-call prompt personalization with dynamic variable substitution.
 * Usage: npx tsx main.ts
 */

import { Patter } from "getpatter";
import dotenv from "dotenv";
dotenv.config({ path: "../.env" });

const phone = new Patter({
  mode: "local",
  openaiKey: process.env.OPENAI_API_KEY!,
  twilioSid: process.env.TWILIO_ACCOUNT_SID!,
  twilioToken: process.env.TWILIO_AUTH_TOKEN!,
  phoneNumber: process.env.TWILIO_PHONE_NUMBER!,
  webhookUrl: process.env.WEBHOOK_URL!,
});

const CUSTOMERS: Record<string, Record<string, string>> = {
  "+14155551234": { customerName: "Alice Chen", accountNumber: "AC-78901", planTier: "Enterprise" },
  "+14155555678": { customerName: "Bob Martinez", accountNumber: "AC-45678", planTier: "Starter" },
};

const agent = phone.agent({
  systemPrompt: `You are a personal account manager for {customerName}.
Their account number is {accountNumber} and their plan is {planTier}.
Greet them by name and help with billing questions.`,
  firstMessage: "Hi {customerName}! Thanks for calling. How can I help?",
  variables: { customerName: "Valued Customer", accountNumber: "unknown", planTier: "Free" },
});

async function main(): Promise<void> {
  await phone.serve({
    agent,
    port: 8000,
    onCallStart: async (data) => {
      const caller = data.caller as string;
      const customer = CUSTOMERS[caller];
      if (customer) {
        console.log(`Known caller ${caller} -> ${customer.customerName}`);
        return { variables: customer };
      }
    },
  });
}

main();
