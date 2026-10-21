from collections import Counter
import re


def analyse_text(text):
  if not text or not text.strip():
    return {
        "word_count": 0,
        "unique_word_count": 0,
        "vowel_count": 0,
        "longest_word": None,
        "shortest_word": None,
        "most_common_word_length": None,
    }

  # 3) Count no of vowels (checking both lowercase and uppercase)
  vowels = "aeiouAEIOU"
  vowel_count = sum(1 for char in text if char in vowels)

  # Extract words using regex (ignores punctuation attached to words)
  words = re.findall(r"\b\w+\b", text)

  if not words:
    return {
        "word_count": 0,
        "unique_word_count": 0,
        "vowel_count": vowel_count,
        "longest_word": None,
        "shortest_word": None,
        "most_common_word_length": None,
    }

  # 1) Count no of words
  word_count = len(words)

  # 2) Count no of unique words (case-insensitive)
  unique_words = set(w.lower() for w in words)
  unique_word_count = len(unique_words)

  # 4) Find the longest word
  longest_word = max(words, key=len)

  # 5) Find the shortest word
  shortest_word = min(words, key=len)

  # 6) Find the most common length word
  word_lengths = [len(w) for w in words]
  length_counts = Counter(word_lengths)
  most_common_length = length_counts.most_common(1)[0][0]

  return {
      "word_count": word_count,
      "unique_word_count": unique_word_count,
      "vowel_count": vowel_count,
      "longest_word": longest_word,
      "shortest_word": shortest_word,
      "most_common_word_length": most_common_length,
  }


# --- Example Usage ---
sample_text = (
    "Hello world! Programming in Python is fun, and learning to code is"
    " rewarding."
)
results = analyse_text(sample_text)

for key, value in results.items():
  print(f"{key}: {value}")



#   Assignment4 No2
# Temporary data storage dictionary
accounts = {}
account_counter = 1001  # Used to generate unique account IDs


def create_account(name, balance=0):
  """Creates a new bank account with a unique account ID and initial balance."""
  global account_counter
  account_id = f"ACC{account_counter}"
  account_counter += 1

  if balance < 0:
    print("Initial balance cannot be negative. Setting balance to 0.")
    balance = 0

  accounts[account_id] = {"name": name, "balance": balance}
  print(
      f"Account successfully created! ID: {account_id} | Name: {name} | Initial"
      f" Balance: ${balance}"
  )
  return account_id


def deposite(account, amount):
  """Deposits a specified amount into the given account."""
  if account not in accounts:
    print(f"Error: Account {account} not found.")
    return

  if amount <= 0:
    print("Deposit amount must be greater than zero.")
    return

  accounts[account]["balance"] += amount
  print(
      f"Deposited ${amount:.2f} into account {account}."
      f" New Balance: ${accounts[account]['balance']:.2f}"
  )


def withdraw(account, amount):
  """Withdraws a specified amount from the given account if funds are sufficient."""
  if account not in accounts:
    print(f"Error: Account {account} not found.")
    return

  if amount <= 0:
    print("Withdrawal amount must be greater than zero.")
    return

  if accounts[account]["balance"] >= amount:
    accounts[account]["balance"] -= amount
    print(
        f"Withdrew ${amount:.2f} from account {account}."
        f" Remaining Balance: ${accounts[account]['balance']:.2f}"
    )
  else:
    print(
        f"Error: Insufficient balance in account {account}. Current Balance:"
        f" ${accounts[account]['balance']:.2f}"
    )


def checkbalance(account):
  """Checks and returns the current balance of the given account."""
  if account not in accounts:
    print(f"Error: Account {account} not found.")
    return None

  balance = accounts[account]["balance"]
  name = accounts[account]["name"]
  print(f"Account: {account} ({name}) | Balance: ${balance:.2f}")
  return balance


def transfer_money(sender, receiver, amount):
  """Transfers money from a sender account to a receiver account."""
  if sender not in accounts or receiver not in accounts:
    print("Error: Sender or receiver account not found.")
    return

  if amount <= 0:
    print("Transfer amount must be greater than zero.")
    return

  if accounts[sender]["balance"] >= amount:
    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount
    print(
        f"Successfully transferred ${amount:.2f} from {sender} ("
        f"{accounts[sender]['name']}) to {receiver} ("
        f"{accounts[receiver]['name']})."
    )
  else:
    print(
        f"Error: Insufficient funds in sender account {sender} to complete"
        " transfer."
    )


# --- Example Usage ---
if __name__ == "__main__":
  # 1. Create accounts
  acc1 = create_account("Alice Smith", 500)
  acc2 = create_account("Bob Jones", 200)

  print("-" * 40)

  # 2. Deposit money
  deposite(acc1, 150)

  # 3. Withdraw money
  withdraw(acc2, 50)

  print("-" * 40)

  # 4. Check balance
  checkbalance(acc1)
  checkbalance(acc2)

  print("-" * 40)

  # 5. Transfer money
  transfer_money(acc1, acc2, 100)

  print("-" * 40)

  # Final balance check
  checkbalance(acc1)
  checkbalance(acc2)


#   Assignment4 No3
words = ["madam", "apple", "noon", "python", "racecar", "banana", "level"]

# Filter out palindromes
palindromes = list(filter(lambda s: s == s[::-1], words))

print("Original Words:", words)
print("Palindromes:", palindromes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Square the number if it's odd, otherwise leave it as is
modified_numbers = list(map(lambda x: x**2 if x % 2 != 0 else x, numbers))

print("Original Numbers:", numbers)
print("Modified Numbers:", modified_numbers)

strings = ["hello", "world", "apple", "test", "python", "cat"]

# Filter strings where length of unique characters (set) is less than total length
has_duplicates = list(filter(lambda s: len(set(s)) < len(s), strings))

print("Original Strings:", strings)
print("Strings with Duplicate Characters:", has_duplicates)

texts = ["Hello World", "python", "Data Science", "machine learning", "Java"]

# Apply swapcase() if the string is NOT a title, otherwise leave it unchanged
result_texts = list(map(lambda s: s.swapcase() if not s.istitle() else s, texts))

print("Original Texts:", texts)
print("Processed Texts:", result_texts)