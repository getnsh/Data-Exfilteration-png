# Data Exfiltration Using Disguised PNG

This project demonstrates how malicious actors can exfiltrate data from a machine using a seemingly innocent PNG image file.

## 🚨 **What This Does**

In this project, I show how a **harmless-looking image file** (a meme, for example) can be used to run a **data-stealing payload** on a victim’s machine. This technique uses a combination of:

- Python scripting to collect data from the system.
- Self-Extracting Archives (SFX) to disguise the payload.
- RTLO (Right-To-Left Override) trick to hide the executable extension.
- Flask listener to capture and store the stolen data.
  
The **data exfiltration** occurs silently, without requiring administrator access, making it a highly effective method for potential attackers.

## 🧑‍💻 **How It Works**

1. **Python Script**: Collects information about the system (like network, hardware, installed apps).
2. **SFX Archive**: Bundles the script with a meme image, making it look like a harmless file.
3. **RTLO Trick**: Hides the `.exe` extension, making it look like a `.png` file.
4. **Flask Listener**: Captures the data sent back from the script and logs it for review.

## 🔧 **Requirements**

- Python 3.x
- `pyinstaller` to compile the Python script
- Flask for the listener
- WinRAR or similar software to create the SFX archive

## ⚠️ **Important Notes**

This project was created for educational purposes in a **controlled environment** (isolated virtual machine) as part of a red team exercise for my resume. The goal was to demonstrate how attackers could potentially hide malicious payloads in seemingly innocent files like PNG images.

## 🚀 **Demo and Code**

You can find the complete code, including the listener, payload, and the disguised image, in the repository files.

### 🔗 [Check out the full code and detailed instructions on my GitHub](#).

## 🔐 **How to Protect Yourself**

- Be cautious when opening files from untrusted sources.
- Always double-check file extensions (like `image.png.exe`).
- Use antivirus software to scan for malicious files.
- Avoid downloading suspicious images from the internet.

## 📖 **Detailed Explanation**

If you're interested in a more detailed technical breakdown of how this works, check out my [blog post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7328233066697547776/).


### 📝 **License**

This project is for educational purposes only. It should not be used for malicious activities.

