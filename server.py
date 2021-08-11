from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
        'corresponsalBancario': {
            'FIIDEntidad': "0140" ,
            'idAdquirente': 10203040,
            'terminal': { 
            'id': "ZWC02001",  
                'tipo': "WEB",
                'capacidadPIN': "Desconocido"
                }, 
            'virtualPAN': {
                'tipo': "Ahorros",
                'numero': "000000053265"
             },
            'contacto': {  
                'Telefono': [7777777],
                'Correo': ["api@ejemplo.com"]
             }
        },
        'transaccion': {
            'modoCapturaPAN': "Banda",
            'idConsecutivoTerminal': 390,   
            'tipo': "Recaudo",
            'tarjeta': {
                'tipo': "Ahorros",
                'numero': "000000053265",
                'fechaExpiracion': "06/21",
                'cvc': "123"
                }
        }, 
        'autorizacion': {
            'id': "X24225",
            'numeroReferencia': "000000053267"
        }   
        }
        ).encode('utf-8'))
        return

    def do_POST(self):
        rawData = (self.rfile.read(int(self.headers['content-length']))).decode()
        post_body = rawData
        data = json.loads(post_body)
        print(data)
        #data = post_body
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(
            {
            'Processing Code': 9300,
            'System Trace Number': 15,
            'NII': 1820,
            'Terminal ID': "QPOS0181",
            'Table Id': 1,
            'Table Length': 5,
            'Table': {
                "IVA":19,
                "INC":12,
                "Pasword Supervisor":"0000",
                "Pasword Administrador":"1234"
            }

            
        }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('',80),RequestHandler)
    print('Starting server at http://localhost:80')
    server.serve_forever()


     