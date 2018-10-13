from flask import Flask, request, send_from_directory

from app import app

@app.route('/<path:path>')
def static_file_server(path):
    
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()