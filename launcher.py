"""
Simple launcher for Phase4-Mol3D
Opens the app in default browser automatically
"""

import webbrowser
import threading
import time
import sys
import os
from app import app

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)  # Wait for Flask to start
    webbrowser.open('http://localhost:5000')

def main():
    print("🧬 Starting Phase4-Mol3D Molecular Visualizer...")
    print("🌐 Opening in your default browser...")
    print("🔗 URL: http://localhost:5000")
    print("⚠️  Keep this window open while using the app")
    print("❌ Close this window to stop the app")
    print("-" * 50)
    
    # Start browser in separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    try:
        # Start Flask app
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n👋 Phase4-Mol3D stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()