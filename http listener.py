from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def report():
    data = request.get_json()
    print("\n[+] Data Received:")
    print(data)
    
    # Save to file for logging
    with open("received_data.log", "a") as f:
        f.write(str(data) + "\n")
    
    return jsonify({"status": "Data received"}), 200

if __name__ == '__main__':
    print("[+] HTTP Listener Running on Port 8080...")
    app.run(host='0.0.0.0', port=8080)
