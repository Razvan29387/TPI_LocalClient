import argparse
import socket
import threading


def handle_client(client_socket, address):
	print(f"Client connected: {address[0]}:{address[1]}", flush=True)
	try:
		while True:
			data = client_socket.recv(4096)
			if not data:
				break
			client_socket.sendall(data)
	except OSError as error:
		print(f"Client error ({address[0]}:{address[1]}): {error}", flush=True)
	finally:
		client_socket.close()
		print(f"Client disconnected: {address[0]}:{address[1]}", flush=True)


def main():
	parser = argparse.ArgumentParser(description="Simple TCP echo server")
	parser.add_argument("--host", default="0.0.0.0")
	parser.add_argument("--port", type=int, default=5000)
	args = parser.parse_args()

	if not 1 <= args.port <= 65535:
		parser.error("--port must be between 1 and 65535")

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind((args.host, args.port))
		server_socket.listen()
		print(f"TCP echo server listening on {args.host}:{args.port}", flush=True)

		try:
			while True:
				client_socket, address = server_socket.accept()
				threading.Thread(
					target=handle_client,
					args=(client_socket, address),
					daemon=True,
				).start()
		except KeyboardInterrupt:
			print("\nServer stopped", flush=True)


if __name__ == "__main__":
	main()
