def parsesimpleyaml(yaml: str) -> dict:
  return dict((x.split(": ")[0],int(x.split(": ")[1])) for x in yaml.split("\n"))

def writeyaml(file: str, yaml: dict) -> None:
  with open(file, "w") as f:
    f.write('\n'.join(': '.join(x) for x in zip(yaml.keys(), yaml.values())))
  
def updateyaml(file: str, update: dict) -> None:
  with open(file) as f:
    yaml = parsesimpleyaml(f.read())
  yaml.update(update)
  writeyaml(file, yaml)

updateyaml("data.yaml", {sys.argv[1]: sys.argv[2]})
