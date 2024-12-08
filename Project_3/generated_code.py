try:
    from pathlib import Path
    import os

    BASE_DIR = Path(__file__).resolve().parent.parent
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    print("Program executed successfully.")

except Exception as e:
    print("Program execution failed:", e)