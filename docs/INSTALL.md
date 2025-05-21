# Installation Guide — IX-GhostProtocol

This guide walks you through setting up the IX-GhostProtocol environment for testing, experimentation, or contribution.

---

## 🧰 System Requirements

- OS: Linux, macOS, or Windows 10/11 with WSL2
- Python: 3.9 or newer
- Node.js: v18+ (for optional GUI components)
- Git
- Make (optional but recommended)
- pipx (recommended for isolated Python tools)

---

## 📦 Core Dependencies

Clone the repository:

```bash
git clone https://github.com/BryceWDesign/IX-GhostProtocol.git
cd IX-GhostProtocol

Install Python environment: python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

Optional GUI dashboard (WIP): cd gui
npm install
npm run dev

📁 File Structure
/core — core IX protocol files

/client — minimal test interface (CLI)

/docs — documentation and schematics

/gui — browser-accessible node monitor

/utils — developer tools and test injectors

🧪 Running the Protocol Locally
Simulate encrypted relay with two CLI clients: python client/client.py --peer testnode
To test multiple routes, launch with flags: python client/client.py --simulate 3 --verbose
✅ Final Checks
Ensure Python dependencies are installed

Try running python client/client.py --help

If GUI fails to build, ensure Node v18+ and npm are correctly installed

🛠️ Troubleshooting
If setup fails:

Check Python version: python3 --version

Delete and recreate .venv

Re-run pip install -r requirements.txt

Use Issues tab to report reproducible bugs

🧾 License
This software is licensed under the GNU Affero General Public License v3. See LICENSE.md for details.

IX-GhostProtocol is built for secure, censorship-resistant communication — help us make it better.

