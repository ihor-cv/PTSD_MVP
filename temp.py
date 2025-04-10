import whisper
import os


def transcribe_and_translate():
    # Available models with their approximate memory requirements
    models = {
        'tiny': "~1GB RAM",
        'base': "~1.5GB RAM",
        'small': "~5GB RAM",
        'medium': "~10GB RAM",
        'large': "~20GB RAM"
    }

    print("Available Whisper models:")
    for name, ram in models.items():
        print(f"- {name.ljust(6)} ({ram})")

    # Model selection
    while True:
        model_name = input("\nChoose model (tiny/base/small/medium/large): ").lower()
        if model_name in models:
            break
        print("Invalid choice! Please select from the available models.")

    # Audio file input
    while True:
        audio_path = input("\nEnter path to Ukrainian audio file: ").strip('"')
        if os.path.exists(audio_path):
            break
        print("File not found! Please try again.")

    print(f"\nLoading {model_name} model... (This may take a moment)")
    model = whisper.load_model(model_name)

    print("\nTranscribing Ukrainian audio...")
    uk_result = model.transcribe(audio_path, language="uk")

    print("Translating to English...")
    en_result = model.transcribe(audio_path, language="uk", task="translate")

    # Generate output filenames
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    uk_file = f"{base_name}_UA.txt"
    en_file = f"{base_name}_EN.txt"

    # Save files
    with open(uk_file, 'w', encoding='utf-8') as f:
        f.write(uk_result['text'])

    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(en_result['text'])

    # Print results
    print("\n" + "=" * 40)
    print(f"UKRAINIAN TRANSCRIPTION ({model_name} model)")
    print("=" * 40)
    print(uk_result['text'])

    print("\n" + "=" * 40)
    print(f"ENGLISH TRANSLATION ({model_name} model)")
    print("=" * 40)
    print(en_result['text'])

    print(f"\n✅ Saved to:\n- {os.path.abspath(uk_file)}\n- {os.path.abspath(en_file)}")


if __name__ == "__main__":
    print("=== Ukrainian Audio Transcription & Translation ===")
    transcribe_and_translate()