import hashlib
import bcrypt
import sys
import secrets
import string

class PasswordGenerator:
  def __init__(self, lenght: int):
    self.pw_lenght = lenght
    self.char_set = string.ascii_letters + string.digits # No simbols due to passwords cannot contain symbols in geometry dash.
  
  @property
  def gen_pw(self):
    return "".join(secrets.choice(self.char_set) for _ in range(self.pw_lenght))

class PasswordHasher:
  def __init__(self, password: str):
    self.password = password
  
  # Legacy bCrypt only password (GD 2.113 and inwards)
  @property
  def gen_gjp1(self):
    bpasswd = self.password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bpasswd, salt).decode("utf-8")
  
  @property
  def gen_sha1(self):
    salt = "mI29fmAnxgTs" # Hardcoded salt
    salted = (self.password + salt).encode("utf-8")
    return hashlib.sha1(salted).hexdigest()
  
  # Newer SHA1 + bCrypt password (GD 2.2 and onwards)
  @property
  def gen_gjp2(self):
    bpasswd = self.gen_sha1.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bpasswd, salt).decode("utf-8")
    
def main():
  args = sys.argv
  if not len(args) == 2:
    try:
      pw_lenght = int(input("No password inputted or inputs surpass one\nProceeding with generating a password, input what lenght you would like it to have: "))
      if pw_lenght < 8:
        raise ValueError("Lenght too short")
    except ValueError as e:
      print(f"No lenght specified or lenght is not valid ({e}), proceeding with 16 characters.")
      pw_lenght = 16
    
    generator = PasswordGenerator(pw_lenght)
    print("Generating...")
    passwd = generator.gen_pw
    print(f"Generated password is: {passwd}")
  else:
    passwd = args[1]
    if lenght(passwd) < 8:
      raise ValueError("Password is too short (min 8 chars)")
  print("Hashing...")
  hasher = PasswordHasher(passwd)
  print(f"Generated GJP1 hash (password field): {hasher.gen_gjp1}\nGenerated GJP2 hash (gjp2 field): {hasher.gen_gjp2}")

if __name__ == "__main__":
    main()
