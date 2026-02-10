# 🎙️ Audio Converter for 3CX & Yeastar PBX Systems

**Professional audio converter for Digital Receptionist voice prompts**

Convert MP3/MP4 files to the exact WAV format required by 3CX and Yeastar phone systems.

---

## 📋 About This Tool

This converter was specifically designed to prepare voice prompts for **Digital Receptionist** (IVR) systems used in:
- **3CX Phone Systems**
- **Yeastar PBX Systems**

### Output Specifications
- **Format**: WAV (PCM)
- **Sample Rate**: 8 kHz
- **Bit Depth**: 16 bit
- **Channels**: Mono
- **Max Size**: 100MB

These specifications are **required** by 3CX and Yeastar for optimal voice quality in telephony applications.

---

## 🎯 Use Case: AI-Generated Voice Prompts

This tool is perfect for converting AI-generated voice prompts from services like:
- **[ElevenLabs](https://elevenlabs.io/)** - Professional AI voice generation
- Other text-to-speech services

### Workflow:
1. Generate voice prompts using [ElevenLabs](https://elevenlabs.io/)
2. Download as MP3/MP4
3. Convert using this tool to telephony-compatible WAV
4. Upload to your 3CX or Yeastar Digital Receptionist

---

## 🚀 Quick Start

### For End Users
1. Double-click `QUICK_START.bat` or open `dist\AudioConverter.exe`
2. Drag & drop your MP3/MP4 file
3. Click "Μετατροπή" (Convert)
4. Save the converted WAV file
5. Upload to your PBX system

**No installation required!** The executable is fully standalone.

---

## ✨ Features

- ✅ **Drag & Drop Interface** - Easy to use
- ✅ **3CX/Yeastar Compatible** - Exact format specifications
- ✅ **Progress Tracking** - Real-time conversion progress
- ✅ **File Size Check** - Validates 100MB limit
- ✅ **Duration Display** - Shows audio length
- ✅ **Greek UI** - Fully localized interface
- ✅ **Standalone** - No dependencies or installation needed

---

## 📦 What's Included

```
Call Center Voice Converter/
├── dist/
│   └── AudioConverter.exe      ← Main executable (109MB)
├── QUICK_START.bat             ← Quick launcher
├── ΟΔΗΓΙΕΣ_ΧΡΗΣΗΣ.txt         ← User guide (Greek)
├── README.md                   ← This file
└── logo/
    └── favicon.ico             ← Application icon
```

---

## 🎙️ Recommended Workflow for Digital Receptionist

### Step 1: Create Voice Prompts
Use [ElevenLabs](https://elevenlabs.io/) to generate professional voice prompts:
- Welcome messages
- Menu options
- Hold music announcements
- After-hours messages
- Department routing prompts

### Step 2: Convert to Telephony Format
Use this tool to convert ElevenLabs MP3 files to 3CX/Yeastar compatible WAV format.

### Step 3: Upload to PBX
Upload the converted WAV files to your:
- **3CX**: Digital Receptionist → Prompts
- **Yeastar**: IVR → Voice Prompts

---

## 🔧 Technical Details

### Why These Specifications?

**8 kHz Sample Rate**: Standard for telephony (G.711 codec)
- Optimized for voice frequency range (300-3400 Hz)
- Reduces file size
- Compatible with all phone systems

**16-bit PCM**: Uncompressed audio
- No quality loss
- Maximum compatibility
- Required by most PBX systems

**Mono**: Single channel
- Telephony systems use mono audio
- Reduces file size by 50%

### Technology Stack
- **Python 3.11**
- **PyQt5** - User interface
- **pydub** - Audio processing
- **FFmpeg** - Audio codec (embedded)
- **PyInstaller** - Standalone executable

---

## 📱 Compatible Systems

### Tested With:
- ✅ **3CX Phone System** (v18, v20)
- ✅ **Yeastar PBX** (S-Series, P-Series)
- ✅ **Yeastar Cloud PBX**

### Voice Prompt Services:
- ✅ **[ElevenLabs](https://elevenlabs.io/)** - AI voice generation
- ✅ Any MP3/MP4 audio source

---

## 💡 Tips for Best Results

### Recording Voice Prompts:
1. **Keep it concise** - 10-30 seconds per prompt
2. **Clear pronunciation** - Especially for menu options
3. **Professional tone** - Match your business image
4. **Test before deployment** - Listen to converted files

### ElevenLabs Settings:
- Use **high-quality** voice models
- Export as **MP3** (highest quality)
- Consider **voice cloning** for consistency
- Use **professional voices** for business applications

---

## 📞 Use Cases

### Digital Receptionist Prompts:
- "Thank you for calling [Company Name]..."
- "Press 1 for Sales, Press 2 for Support..."
- "Please hold while we transfer your call..."
- "Our office hours are Monday to Friday..."
- "For emergencies, please press 0..."

### IVR Menu Systems:
- Multi-level menu navigation
- Department routing
- After-hours messages
- Holiday announcements
- Queue announcements

---

## 🔒 Privacy & Security

- ✅ **100% Offline** - No internet required after download
- ✅ **No Data Collection** - Your files stay on your computer
- ✅ **No Cloud Upload** - All processing is local
- ✅ **Secure** - No external dependencies

---

## 📖 Documentation

- **User Guide**: `ΟΔΗΓΙΕΣ_ΧΡΗΣΗΣ.txt` (Greek)
- **Technical Docs**: `README_GREEK.md`
- **Version Info**: `VERSION.txt`
- **Delivery Notes**: `ΠΑΡΑΔΟΣΗ.txt`

---

## 🆘 Support & Troubleshooting

### Common Issues:

**Q: The .exe doesn't open**
A: Install [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

**Q: Conversion fails**
A: Ensure your input file is a valid MP3 or MP4

**Q: File too large**
A: The output exceeds 100MB - use a shorter audio file

**Q: Quality issues**
A: The 8 kHz format is standard for telephony - this is expected

---

## 👨‍💻 Developer

**Διονύσης Πρόκος** (Dionysis Prokos)

Specialized in:
- PBX Systems (3CX, Yeastar)
- Digital Receptionist Solutions
- AI Voice Integration
- Telephony Audio Processing

---

## 🔗 Related Links

- **ElevenLabs**: https://elevenlabs.io/ - AI Voice Generation
- **3CX**: https://www.3cx.com/ - Phone System
- **Yeastar**: https://www.yeastar.com/ - PBX Solutions

---

## 📄 License

Free to use for personal and commercial applications.

---

## 🎯 Perfect For:

- ✅ Call Centers
- ✅ Business Phone Systems
- ✅ Customer Service Departments
- ✅ Reception Automation
- ✅ IVR Systems
- ✅ Auto-Attendant Setup
- ✅ Multi-language Support Systems

---

## 🌟 Why This Tool?

Most audio files from AI services like ElevenLabs come in formats that are **not compatible** with PBX systems. This tool bridges that gap by converting them to the **exact specifications** required by 3CX and Yeastar.

**Save time. Ensure compatibility. Professional results.**

---

**Made with ❤️ for the telephony community**

*Converting AI voices to telephony-ready prompts since 2026*
