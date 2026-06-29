import re

def normalize_phone(phone: str) -> str:
  phone = phone.strip()

  # Remove spaces, dashes, brackets, etc.
  phone = re.sub(r"[\s\-\(\)]", "", phone)

  if phone.startswith("+254"):
    normalized = phone

  elif phone.startswith("254"):
    normalized = f"+{phone}"

  elif phone.startswith("07"):
    normalized = f"+254{phone[1:]}"

  elif phone.startswith("01"):
    normalized = f"+254{phone[1:]}"

  elif re.match(r"^7\d{8}$", phone):
    normalized = f"+254{phone}"

  elif re.match(r"^1\d{8}$", phone):
    normalized = f"+254{phone}"

  else:
    raise ValueError("Invalid Kenyan phone number")

  if not re.match(r"^\+254(?:7|1)\d{8}$", normalized):
    raise ValueError("Invalid Kenyan phone number")

  return normalized


def get_phone_parts(phone: str) -> tuple[str, str]:
  phone = normalize_phone(phone)

  front = phone[4:7]
  back = phone[-3:]

  return front, back