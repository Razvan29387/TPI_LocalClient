# TPI_LocalClient

## Start server

```sh
python3 server.py
```

The TCP server listens on `0.0.0.0:8000` and echoes back the bytes sent by each client. Stop it with `Ctrl+C`.

## Connect from a local machine with gh

On the local machine, find the Codespace name and forward its port:

```sh
gh codespace list
gh codespace ports forward 8000:8000 -c <codespace-name>
```

Connect your local TCP client to `127.0.0.1:8000`.