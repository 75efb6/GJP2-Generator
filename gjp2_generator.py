import hashlib
import bcrypt
import sys

class PasswordHasher:
  def __init__(self, password):
    self.password = password
  
  def gen_sha1(self):
    salt = "mI29fmAnxgTs" # Hardcoded salt
    self.password = (self.password + salt).encode()
    return hashlib.sha1(self.password).hexdigest()
  
  def gen_gjp2(self):
    bpasswd = self.gen_sha1().encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bpasswd, salt).decode("utf-8")
    
def main():
  args = sys.argv
  if not len(args) == 2:
    return print("No password inputed or inputs surpass one\nUSAGE: python gjp2_generator.py <password>")
  passwd = args[1]
  print("Hashing...")
  hasher = PasswordHasher(passwd)
  print(f"Generated hash: {hasher.gen_gjp2()}")

if __name__ == "__main__":
    main()
