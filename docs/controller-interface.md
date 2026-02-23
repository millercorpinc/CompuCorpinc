# Controller Interface (Local-First)

Defines how the external controller drives the DOS operator loop.

## Runtime target

- Local model host: **Ollama** on same PC (`http://127.0.0.1:11434`).
- GPU target: **NVIDIA RTX 3070 Ti** (CUDA).
- Recommended model for planning/action drafting: `llama3.1:8b-instruct-q4_K_M`.

## Inputs

1. Latest inbox `.MSG` file.
2. Operator constitution (`agent/operator_prompt.txt`).
3. Safety policy (`agent/behavior_contract.md`).

## Outputs

1. Proposed DOS command sequence (`ops/logs/controller-actions.log`).
2. Reply draft body (`work/C_WORK/MAIL/OUTBOX/*.MSG` via DOS workflow).
3. Structured telemetry entry per cycle.

## API contract (controller -> local model)

POST `/api/generate` body:

```json
{
  "model": "llama3.1:8b-instruct-q4_K_M",
  "prompt": "<prompt>",
  "stream": false,
  "options": {
    "temperature": 0.2,
    "num_predict": 512
  }
}
```

Response must be parsed as plain text command plan.

## Safety guardrails

- Block commands matching: `FORMAT`, `DELTREE`, `FDISK`, `SYS C:`.
- Require explicit allowlist for write paths outside `C:\WORK\`.
- If uncertain, emit `NEEDS_HUMAN_REVIEW` and stop.

## Reference implementation

See `scripts/local_controller.py` for a minimal local-model controller loop.
