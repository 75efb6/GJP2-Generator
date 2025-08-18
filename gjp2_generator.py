import hashlib
import bcrypt
import sys

class PasswordHasher:
  def __init__(self, password):
    self.password = password
  
  @property
  def gen_sha1(self):
    salt = "mI29fmAnxgTs" # Hardcoded salt
    self.password = (self.password + salt).encode("utf-8")
    return hashlib.sha1(self.password).hexdigest()
  
  @property
  def gen_gjp2(self):
    bpasswd = self.gen_sha1.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bpasswd, salt).decode("utf-8")
  
  @property
  def gen_gjp1(self):
    bpasswd = self.password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bpasswd, salt).decode("utf-8")
    
def main():
  args = sys.argv
  if not len(args) == 2:
    return print("No password inputed or inputs surpass one\nUSAGE: python gjp2_generator.py <password>")
  passwd = args[1]
  print("Hashing...")
  hasher = PasswordHasher(passwd)
  print(f"Generated GJP1 hash (password field): {hasher.gen_gjp1}\nGenerated GJP2 hash (gjp2 field): {hasher.gen_gjp2}")

if __name__ == "__main__":
    main()