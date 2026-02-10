# 🎵 Audio Converter - Μετατροπέας Ήχου

Εφαρμογή μετατροπής αρχείων ήχου MP3/MP4 σε WAV με συγκεκριμένες προδιαγραφές για Call Center.

> **🚀 ΓΡΗΓΟΡΗ ΕΚΚΙΝΗΣΗ:** Κάντε διπλό κλικ στο `QUICK_START.bat` ή ανοίξτε το `dist\AudioConverter.exe`

## 📋 Προδιαγραφές Εξόδου
- **Format**: WAV (PCM)
- **Sample Rate**: 8 kHz
- **Bit Depth**: 16 bit
- **Channels**: Mono
- **Max Size**: 100MB

---

## 🚀 Για Χρήστες

### Χρήση της Εφαρμογής
1. Ανοίξτε το `AudioConverter.exe`
2. Σύρετε ένα αρχείο MP3/MP4 ή κάντε κλικ "Επιλογή Αρχείου"
3. Πατήστε "Μετατροπή"
4. Επιλέξτε που θέλετε να αποθηκευτεί το WAV
5. Περιμένετε να ολοκληρωθεί!

**✨ Δεν χρειάζεται εγκατάσταση - απλά τρέξτε το .exe!**

---

## 💻 Για Developers

### Εκτέλεση από Python
```bash
python audio_converter.py
```
Το FFmpeg θα κατέβει **αυτόματα** την πρώτη φορά!

### Δημιουργία Executable
```bash
python build.py
```
Ή:
```bash
build_exe.bat
```

Το script θα:
1. ✅ Κατεβάσει αυτόματα το FFmpeg (~80MB)
2. ✅ Εγκαταστήσει τα dependencies
3. ✅ Φτιάξει το standalone `AudioConverter.exe`

---

## ✨ Χαρακτηριστικά

- ✅ **Drag & Drop**: Σύρετε αρχεία απευθείας
- ✅ **File Browser**: Επιλογή με browser
- ✅ **Progress Bar**: Παρακολούθηση προόδου
- ✅ **Size Check**: Έλεγχος μεγέθους (100MB max)
- ✅ **Ελληνική Διεπαφή**: Πλήρως στα Ελληνικά
- ✅ **MP3 & MP4**: Υποστήριξη και των δύο
- ✅ **Standalone**: Δεν χρειάζεται εγκατάσταση

---

## 📦 Το Executable

Το `AudioConverter.exe` είναι **πλήρως standalone** (~109MB):
- ✅ Δεν χρειάζεται Python
- ✅ Δεν χρειάζεται FFmpeg
- ✅ Δεν χρειάζεται τίποτα άλλο
- ✅ Μοιράστε το και δουλεύει παντού!

Το FFmpeg είναι embedded μέσα στο executable.

---

## 🔧 Απαιτήσεις (για Development)

- Windows 10/11
- Python 3.8+
- Internet (για αυτόματο κατέβασμα FFmpeg)

---

## 📁 Δομή Project

```
Call Center Voice Converter/
├── audio_converter.py      # Κύρια εφαρμογή
├── build.py               # Build script
├── setup_ffmpeg.py        # FFmpeg downloader
├── build_exe.bat          # Shortcut για build
├── requirements.txt       # Python dependencies
├── README_GREEK.md        # Αυτό το αρχείο
└── dist/
    └── AudioConverter.exe # Το τελικό executable
```

---

## 🔧 Troubleshooting

### Κατά το Build: "FFmpeg not found"
- Το script θα το κατεβάσει αυτόματα
- Αν αποτύχει, τρέξτε: `python setup_ffmpeg.py`

### "DLL load failed" (PyQt5)
- Εγκαταστήστε Visual C++ Redistributable
- Link: https://aka.ms/vs/17/release/vc_redist.x64.exe

### Το .exe είναι μεγάλο (~109MB)
- Αυτό είναι φυσιολογικό
- Περιλαμβάνει Python, PyQt5, και FFmpeg
- Είναι standalone - δεν χρειάζεται εγκατάσταση

---

## 📝 Τεχνικές Λεπτομέρειες

**Τεχνολογίες:**
- **PyQt5**: Γραφικό περιβάλλον
- **pydub**: Επεξεργασία ήχου
- **FFmpeg**: Κωδικοποίηση/αποκωδικοποίηση
- **PyInstaller**: Δημιουργία executable

**Μετατροπή:**
- Φόρτωση MP3/MP4
- Resampling σε 8 kHz
- Μετατροπή σε Mono
- 16-bit PCM encoding
- Export σε WAV

---

## 📄 Άδεια

Free to use για προσωπική και εμπορική χρήση.

---

## 🎯 Credits

Developed for Call Center voice file conversion.
