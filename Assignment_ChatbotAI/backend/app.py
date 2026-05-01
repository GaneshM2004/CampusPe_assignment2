"""
CampusPe AI Chatbot — Flask Backend
====================================
App-factory pattern.  Exposes POST /api/chat.
Supports three LLM providers via environment variables:
  • LLM_PROVIDER = groq | gemini | cohere   (default: groq)
  • LLM_API_KEY  = your API key for the chosen provider
  • LLM_MODEL    = (optional) override the default model name
"""

import os
import json
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load environment variables from the .env file
load_dotenv()


# ──────────────────────────────────────────────
# LLM provider adapters
# ──────────────────────────────────────────────

def _call_groq(api_key: str, model: str, messages: list) -> str:
    """Call the Groq Chat Completions API (OpenAI-compatible)."""
    model = model or "llama-3.3-70b-versatile"
    resp = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1024,
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def _call_gemini(api_key: str, model: str, messages: list) -> str:
    """Call the Google Gemini (Generative Language) REST API."""
    model = model or "gemini-2.0-flash"
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
        f":generateContent?key={api_key}"
    )

    # Extract system instruction from messages
    system_text = ""
    contents = []
    for msg in messages:
        if msg["role"] == "system":
            system_text = msg["content"]
        else:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": msg["content"]}]})

    payload = {
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
        },
    }
    if system_text:
        payload["systemInstruction"] = {"parts": [{"text": system_text}]}

    resp = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def _call_cohere(api_key: str, model: str, messages: list) -> str:
    """Call the Cohere Chat API."""
    model = model or "command-r-plus"
    resp = requests.post(
        "https://api.cohere.com/v2/chat",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1024,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"][0]["text"]


PROVIDERS = {
    "groq": _call_groq,
    "gemini": _call_gemini,
    "cohere": _call_cohere,
}


# ──────────────────────────────────────────────
# App Factory
# ──────────────────────────────────────────────

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # ── Config from environment ──
    provider_name = os.getenv("LLM_PROVIDER", "groq").lower()
    api_key = os.getenv("LLM_API_KEY", "")
    model_override = os.getenv("LLM_MODEL", "")

    if provider_name not in PROVIDERS:
        raise ValueError(
            f"Unsupported LLM_PROVIDER '{provider_name}'. "
            f"Choose from: {', '.join(PROVIDERS)}"
        )

    call_llm = PROVIDERS[provider_name]

    # ── Routes ──

    # System prompt prepended to every conversation
    SYSTEM_PROMPT = {
        "role": "system",
        "content": (
            "You are CampusPe AI, a highly technical AI assistant. "
            "Always be accurate and concise."
        ),
    }

    @app.route("/api/chat", methods=["POST"])
    def chat():
        body = request.get_json(silent=True)
        if not body or "messages" not in body:
            return jsonify({"error": "Missing 'messages' in request body."}), 400

        conversation = body["messages"]
        if not isinstance(conversation, list) or len(conversation) == 0:
            return jsonify({"error": "'messages' must be a non-empty array."}), 400

        if not api_key:
            return jsonify({
                "error": (
                    f"LLM_API_KEY is not set. Please set it for the "
                    f"'{provider_name}' provider before sending requests."
                )
            }), 500

        # Prepend system prompt to the conversation
        full_messages = [SYSTEM_PROMPT] + conversation

        try:
            reply = call_llm(api_key, model_override, full_messages)
            return jsonify({"reply": reply})
        except requests.exceptions.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else 502
            detail = ""
            try:
                detail = exc.response.json()
            except Exception:
                detail = exc.response.text[:500] if exc.response is not None else str(exc)
            return jsonify({"error": f"LLM API error ({status})", "detail": detail}), 502
        except requests.exceptions.Timeout:
            return jsonify({"error": "LLM API request timed out."}), 504
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500

    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "ok",
            "provider": provider_name,
            "model": model_override or "(default)",
        })

    return app


# ──────────────────────────────────────────────
# Entrypoint
# ──────────────────────────────────────────────

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
