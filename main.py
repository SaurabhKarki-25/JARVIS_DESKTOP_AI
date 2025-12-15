from ui.gui import run_ui

def main():
    try:
        run_ui()
    except KeyboardInterrupt:
        print("\n[JARVIS] Shutting down...")
    except Exception as e:
        print("[ERROR]", e)

if __name__ == "__main__":
    main()
