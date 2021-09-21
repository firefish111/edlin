import sys

# "fake header not in the original" noises intensify
print("\033[2J\033[HLine Editor for MS-DOS\n(c) Copyright 1981-1993 Microsoft Corp.\n")

# "fake file creation prompt not in the original" noises intensify
#fname = input("What do you wish to call your file? ")

fname = "test.txt"
fname = fname.upper()


line = 1
sel = 1
buf = []
try:
  with open(fname, "r") as file:
    buf = file.read().split("\n")
    file.close()
  print("\033[2J\033[HEnd of input file")
except FileNotFoundError:
  print("\033[2J\033[HNew file")


while True:
  # cmnd
  cmd = input("*")
  match cmd[0]:
    case "i":
      while True:
        try:
          buf.append(input(f"\t{len(buf) + 1}:*"))
        except KeyboardInterrupt:
          break
      print("\n")
    case ["e", "w"]:
      with open(fname, "w") as file:
        file.write("\n".join(buf))
        file.close()
    case "e":
      sys.exit()
    case "q":
      yn = ""
      while not yn in ["y", "n", "Y", "N"]:
        yn = input("Abort edit (Y/N)? ").lower()
      if yn == "y":
        sys.exit(0)
    case "l":
      i = 0
      for lin in buf:
        i += 1
        print(f"\t{i}:{('*' if i == sel else ' ')}{lin}")
    case cm if cm.isdigit():
      sel = int(cm)
      print(f"\t{sel}*{buf[sel - 1]}")
      buf[sel - 1] = input(f"\t{sel}*")
    case _:
      print("Entry error")