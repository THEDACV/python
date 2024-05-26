def is_spam(text):
  """
  This function checks for basic spam indicators in a text.

  Args:
      text: The text of the email to be checked.

  Returns:
      True if the text has some spam indicators, False otherwise.
  """
  # Convert to lowercase for case-insensitive check
  text = text.lower()

  # Common spam indicators
  indicators = [
      "urgent", "free", "million", "click here", "winner", "!",
      "$", "**", "%%%"
  ]

  # Check if any indicator is present multiple times
  for indicator in indicators:
    if text.count(indicator) >= 2:
      return True

  # Check for excessive use of uppercase characters
  if sum(c.isupper() for c in text) / len(text) > 0.2:
    return True

  # Not conclusive evidence of spam
  return False

# Example usage
email_text = "Congratulations! You've won a million dollars! Click here to claim your prize!!! $"
if is_spam(email_text):
  print("This email is likely spam.")
else:
  print("This email may not be spam.")
