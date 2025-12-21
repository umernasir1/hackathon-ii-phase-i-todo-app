from jose import jwt
from app.config import settings

# Token from the frontend
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImV4cCI6MTc2NjY2MTgxNH0.4XbIEya8yY10M6DW1QhfPDlIBpf1hPOj-noX-0-Klsw"

print(f"JWT Secret (first 20 chars): {settings.jwt_secret[:20]}...")
print(f"JWT Algorithm: {settings.jwt_algorithm}")
print(f"\nAttempting to decode token...")

try:
    payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    print(f"✓ Successfully decoded!")
    print(f"Payload: {payload}")
except Exception as e:
    print(f"✗ Failed to decode!")
    print(f"Error: {type(e).__name__}: {str(e)}")
