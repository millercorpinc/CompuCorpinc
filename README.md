# dos-ai-operator

DOS operated entirely by a realistic AI bot.

A **DOSBox-X workstation** driven by an AI operator at human typing speed, with a
file-backed email inbox, live-capture support (OBS / ffmpeg), and full GitHub
agent best-practice scaffolding.

## Quick start

1. Install [DOSBox-X](https://dosbox-x.com/).
2. Launch the workstation:

   ```bash
   dosbox-x -conf ops/dosbox/dosbox-x.conf
   ```

3. In the DOS prompt:

   ```dos
   cd \WORK
   MAIL LIST
   ```

4. Drop a `.MSG` file into `work/C_WORK/MAIL/INBOX/` on the host.
5. Back in DOS: `MAIL LIST` – it appears immediately.

See [docs/runbook.md](docs/runbook.md) for full setup and operation instructions.

See [docs/dev-deployment-plan.md](docs/dev-deployment-plan.md) for the engineering roadmap and deployment plan.

## Repo layout

```text
.github/          GitHub workflows, templates, agent instructions
agent/            AI operator prompt, pacing profile, behaviour contract
docs/             Architecture, runbook, inbox schema, Outlook import plan
ops/dosbox/       DOSBox-X config + autoexec
ops/stream/       ffmpeg recording script + OBS notes
work/C_WORK/      Host folder mounted as C:\WORK inside DOSBox-X
  MAIL/INBOX      Drop .MSG files here to deliver mail to the AI
  MAIL/OUTBOX     AI-composed replies waiting for pickup
  MAIL/SENT       Sent mail archive
  MAIL/ARCHIVE    Processed-inbox archive
  MAIL/FAILED     Undeliverable mail
  MAIL/LEDGER     Processing log
  JOURNAL/        AI daily journal files
  ARTIFACTS/      Work products produced by the AI
  NOTES/          Scratch notes
```

## License

MIT – see [LICENSE](LICENSE).


## Local AI (RTX 3070 Ti)

Run the controller with a local CUDA-backed model via Ollama:

```bash
ollama serve
ollama pull llama3.1:8b-instruct-q4_K_M
python3 scripts/local_controller.py
```

Use `scripts/preflight.sh` before first run to verify host readiness.
