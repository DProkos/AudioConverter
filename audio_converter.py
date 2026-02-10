import sys
import os
from pathlib import Path
import warnings

# Suppress pydub warnings before importing
warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub")

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QLabel, QFileDialog, QProgressBar, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QDragEnterEvent, QDropEvent, QIcon
from pydub import AudioSegment
import zipfile
import urllib.request


# Set FFmpeg path for bundled executable
def setup_ffmpeg():
    """Setup FFmpeg path for both development and bundled executable"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        application_path = sys._MEIPASS
    else:
        # Running as script
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    ffmpeg_path = os.path.join(application_path, 'ffmpeg', 'ffmpeg.exe')
    ffprobe_path = os.path.join(application_path, 'ffmpeg', 'ffprobe.exe')
    
    # Set environment variables for pydub
    if os.path.exists(ffmpeg_path):
        AudioSegment.converter = ffmpeg_path
        AudioSegment.ffmpeg = ffmpeg_path
        AudioSegment.ffprobe = ffprobe_path
        
        # Also set in environment for pydub to find
        os.environ["PATH"] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ.get("PATH", "")
        return True
    return False


def download_ffmpeg_auto():
    """Automatically download FFmpeg if not present"""
    ffmpeg_dir = Path("ffmpeg")
    ffmpeg_exe = ffmpeg_dir / "ffmpeg.exe"
    
    # Check if already exists
    if ffmpeg_exe.exists():
        return True
    
    # Create directory
    ffmpeg_dir.mkdir(exist_ok=True)
    
    # Download URL
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    zip_path = "ffmpeg_temp.zip"
    
    try:
        print("Κατέβασμα FFmpeg... (μία φορά μόνο)")
        urllib.request.urlretrieve(url, zip_path)
        
        # Extract
        print("Εξαγωγή FFmpeg...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith('bin/ffmpeg.exe') or file.endswith('bin/ffprobe.exe'):
                    filename = os.path.basename(file)
                    source = zip_ref.open(file)
                    target = open(ffmpeg_dir / filename, "wb")
                    target.write(source.read())
                    target.close()
                    source.close()
        
        # Cleanup
        os.remove(zip_path)
        print("✓ FFmpeg έτοιμο!")
        return True
        
    except Exception as e:
        print(f"Σφάλμα κατεβάσματος FFmpeg: {e}")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return False


class ConversionThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, input_path, output_path):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path
    
    def run(self):
        try:
            self.progress.emit(10)
            
            # Check input file exists
            if not os.path.exists(self.input_path):
                self.error.emit("Το αρχείο δεν βρέθηκε!")
                return
            
            self.progress.emit(20)
            
            # Load audio file
            file_ext = Path(self.input_path).suffix.lower()
            if file_ext == '.mp3':
                audio = AudioSegment.from_mp3(self.input_path)
            elif file_ext == '.mp4':
                audio = AudioSegment.from_file(self.input_path, format="mp4")
            else:
                audio = AudioSegment.from_file(self.input_path)
            
            self.progress.emit(50)
            
            # Get original info
            original_duration = len(audio) / 1000.0  # seconds
            
            # Convert to required format: PCM, 8 kHz, 16 bit, Mono
            audio = audio.set_frame_rate(8000).set_channels(1).set_sample_width(2)
            
            self.progress.emit(70)
            
            # Export WAV
            audio.export(self.output_path, format="wav")
            
            self.progress.emit(90)
            
            # Check file size (max 100MB)
            file_size = os.path.getsize(self.output_path) / (1024 * 1024)  # MB
            
            self.progress.emit(100)
            
            # Build success message
            message = f"✓ Επιτυχής μετατροπή!\n\n"
            message += f"Διάρκεια: {original_duration:.1f} δευτερόλεπτα\n"
            message += f"Μέγεθος: {file_size:.2f} MB"
            
            if file_size > 100:
                message += f"\n\n⚠️ ΠΡΟΣΟΧΗ: Το αρχείο ξεπερνά τα 100MB!"
            
            self.finished.emit(message)
                
        except Exception as e:
            self.error.emit(f"Σφάλμα μετατροπής:\n{str(e)}")


class AudioConverterUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input_file = None
        self.conversion_thread = None
        self.init_ui()
    
    def get_icon_path(self):
        """Get the path to the icon file"""
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            application_path = sys._MEIPASS
        else:
            # Running as script
            application_path = os.path.dirname(os.path.abspath(__file__))
        
        icon_path = os.path.join(application_path, 'logo', 'favicon.ico')
        return icon_path
    
    def init_ui(self):
        self.setWindowTitle("Audio Converter - MP3/MP4 to WAV")
        self.setGeometry(100, 100, 600, 400)
        self.setAcceptDrops(True)
        
        # Set window icon
        icon_path = self.get_icon_path()
        if icon_path and os.path.exists(icon_path):
            from PyQt5.QtGui import QIcon
            self.setWindowIcon(QIcon(icon_path))
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Audio Converter")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Format info
        format_info = QLabel("Μετατροπή σε: WAV (PCM, 8 kHz, 16 bit, Mono)\nΜέγιστο μέγεθος: 100MB")
        format_info.setAlignment(Qt.AlignCenter)
        format_info.setStyleSheet("color: #666; font-size: 12px;")
        layout.addWidget(format_info)
        
        # Drag & Drop area
        self.drop_label = QLabel("Σύρετε το αρχείο εδώ\nή\nκάντε κλικ για επιλογή")
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setStyleSheet("""
            QLabel {
                border: 3px dashed #aaa;
                border-radius: 10px;
                padding: 40px;
                background-color: #f5f5f5;
                font-size: 14px;
                color: #666;
            }
        """)
        self.drop_label.setMinimumHeight(150)
        layout.addWidget(self.drop_label)
        
        # File info label
        self.file_label = QLabel("Δεν έχει επιλεγεί αρχείο")
        self.file_label.setAlignment(Qt.AlignCenter)
        self.file_label.setStyleSheet("font-size: 12px; color: #333;")
        layout.addWidget(self.file_label)
        
        # Select file button
        self.select_btn = QPushButton("Επιλογή Αρχείου")
        self.select_btn.setMinimumHeight(40)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.select_btn.clicked.connect(self.select_file)
        layout.addWidget(self.select_btn)
        
        # Convert button
        self.convert_btn = QPushButton("Μετατροπή")
        self.convert_btn.setMinimumHeight(40)
        self.convert_btn.setEnabled(False)
        self.convert_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover:enabled {
                background-color: #0b7dda;
            }
            QPushButton:disabled {
                background-color: #ccc;
            }
        """)
        self.convert_btn.clicked.connect(self.convert_file)
        layout.addWidget(self.convert_btn)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #ddd;
                border-radius: 5px;
                text-align: center;
                height: 25px;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
            }
        """)
        layout.addWidget(self.progress_bar)
        
        layout.addStretch()
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            file_path = files[0]
            if file_path.lower().endswith(('.mp3', '.mp4')):
                self.set_input_file(file_path)
            else:
                QMessageBox.warning(self, "Σφάλμα", "Παρακαλώ επιλέξτε αρχείο MP3 ή MP4")
    
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Επιλογή Αρχείου",
            "",
            "Audio Files (*.mp3 *.mp4);;All Files (*.*)"
        )
        if file_path:
            self.set_input_file(file_path)
    
    def set_input_file(self, file_path):
        self.input_file = file_path
        file_name = Path(file_path).name
        self.file_label.setText(f"Επιλεγμένο: {file_name}")
        self.convert_btn.setEnabled(True)
    
    def convert_file(self):
        if not self.input_file:
            return
        
        # Get output path
        input_path = Path(self.input_file)
        output_path, _ = QFileDialog.getSaveFileName(
            self,
            "Αποθήκευση ως",
            str(input_path.parent / f"{input_path.stem}_8k_pcm_mono.wav"),
            "WAV Files (*.wav)"
        )
        
        if not output_path:
            return
        
        # Disable buttons and show progress
        self.select_btn.setEnabled(False)
        self.convert_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Start conversion thread
        self.conversion_thread = ConversionThread(self.input_file, output_path)
        self.conversion_thread.progress.connect(self.update_progress)
        self.conversion_thread.finished.connect(self.conversion_finished)
        self.conversion_thread.error.connect(self.conversion_error)
        self.conversion_thread.start()
    
    def update_progress(self, value):
        self.progress_bar.setValue(value)
    
    def conversion_finished(self, message):
        self.progress_bar.setVisible(False)
        self.select_btn.setEnabled(True)
        self.convert_btn.setEnabled(True)
        QMessageBox.information(self, "Επιτυχία", message)
    
    def conversion_error(self, error_msg):
        self.progress_bar.setVisible(False)
        self.select_btn.setEnabled(True)
        self.convert_btn.setEnabled(True)
        QMessageBox.critical(self, "Σφάλμα", error_msg)


def main():
    # Auto-download FFmpeg if not present (only in development mode)
    if not getattr(sys, 'frozen', False):
        if not setup_ffmpeg():
            print("FFmpeg δεν βρέθηκε. Αυτόματο κατέβασμα...")
            if download_ffmpeg_auto():
                setup_ffmpeg()
            else:
                print("ΣΦΑΛΜΑ: Δεν ήταν δυνατό το κατέβασμα του FFmpeg")
        else:
            print("✓ FFmpeg βρέθηκε και ρυθμίστηκε")
    else:
        # In frozen mode, just setup
        setup_ffmpeg()
    
    app = QApplication(sys.argv)
    window = AudioConverterUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
