from selenium import webdriver
from selenium.webdriver.edge.service import Service
import pywhatkit as kit

options.add_argument("user-data-dir=C:\\caminho\\para\\perfil\\selenium")
driver = webdriver.Edge(service=Service("C:\\webdriver\\msedgedriver.exe"), options=options)

# Inicia o Edge
driver = webdriver.Edge(service=service)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda o usuário escanear o QR Code (caso necessário)
kit.sendwhatmsg_instantly("+5531998186472", "Olá! Esta é uma mensagem automatizada.", wait_time=10)

# Encerra o navegador depois do teste
driver.quit()
