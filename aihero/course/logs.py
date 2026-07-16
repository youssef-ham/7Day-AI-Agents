import os
import json
import secrets
from pathlib import Path
from datetime import datetime

from pydantic_ai.messages import ModelMessagesTypeAdapter

LOG_DIR = Path(
    os.getenv(
        "LOGS_DIRECTORY",
        "logs"
    )
)

LOG_DIR.mkdir(exist_ok=True)


def log_entry(agent, messages, source="user"):
    dict_messages = ModelMessagesTypeAdapter.dump_python(
        messages
    )

    return {
        "agent_name": agent.name,
        "messages": dict_messages,
        "source": source,
    }


def serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

    return str(obj)


def log_interaction_to_file(
    agent,
    messages,
    source="user"
):
    try:
        entry = log_entry(
            agent,
            messages,
            source,
        )

        ts_str = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        rand_hex = secrets.token_hex(3)

        filename = (
            f"{agent.name}_{ts_str}_{rand_hex}.json"
        )

        filepath = LOG_DIR / filename

        with filepath.open(
            "w",
            encoding="utf-8"
        ) as f_out:
            json.dump(
                entry,
                f_out,
                indent=2,
                default=serializer,
            )

        return filepath

    except Exception as e:
        print("Logging failed:", e)