import os
clippy = os.environ.get('CLIPBOARD')  # This will return None if the environment variable is not set
if clippy is not None:
    print("CLIPBOARD environment variable is set to:", clippy)
else:
    print("CLIPBOARD environment variable is not set.")    





