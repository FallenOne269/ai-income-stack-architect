import time
from typing import Type, TypeVar, List, Tuple, Optional
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

def call_with_retries_meta(
    llm,
    model_cls: Type[T],
    system_prompt: str,
    user_payload: str,
    max_retries: int = 3,
) -> Tuple[Optional[T], dict]:
    """Structured-output call with validation-aware retries + metrics."""
    error_messages: List[str] = []
    start = time.perf_counter()

    for attempt in range(1, max_retries + 1):
        error_block = (
            "\n\nPrevious validation errors:\n" + "\n".join(error_messages)
            if error_messages
            else ""
        )
        try:
            # Placeholder: LLM call would go here
            elapsed = time.perf_counter() - start
            meta = {
                "success": True,
                "attempts": attempt,
                "latency_sec": elapsed,
                "errors": error_messages,
            }
            return None, meta
        except Exception as e:
            error_messages.append(f"Attempt {attempt} failed: {repr(e)}")

    elapsed = time.perf_counter() - start
    meta = {
        "success": False,
        "attempts": max_retries,
        "latency_sec": elapsed,
        "errors": error_messages,
    }
    return None, meta
