from os import environ
from waitress import serve
from app import app

def main() -> int:
    if 'PORT' in environ:
        port = int(environ['PORT'])
    else:
        port = 8080

    print(f"Starting server on port {port}!")
    serve(app, host='0.0.0.0', port=port)

    return 0

if __name__ == "__main__":
    main()
