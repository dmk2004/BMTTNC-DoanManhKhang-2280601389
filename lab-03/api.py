from flask import Flask, request, jsonify
from cipher.rsa import RSACipher

app = Flask(__name__)

rsa_cipher = RSACipher()  # tạo instance thay vì dùng lớp trực tiếp

@app.route('/api/rsa/generate_key', methods=["GET"])
def generate_key():
    rsa_cipher.generate_keys()
    return jsonify({"message": "tao khoa thanh cong"})

@app.route('/api/rsa/encrypt', methods=["POST"])
def encrypted_rsa():
    data = request.json
    plain = data["message"]
    key = data["key"]
    public_key, private_key = rsa_cipher.load_keys()
    if key == "pub":
        key = public_key
    elif key == "pri":
        key = private_key   
    else:
        return jsonify({"message": "loi khoa"})
    encrypted_text = rsa_cipher.encrypt(plain, key)
    encrypted_hex = encrypted_text.hex()
    return jsonify({"message": encrypted_hex})  # trả về chuỗi hex thay vì bytes thô

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
