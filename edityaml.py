def parsesimpleyaml(yaml: str) -> dict:
    return dict(x.split(": ") for x in yaml.split("\n"))


def readparseyaml(file: str) -> str:
    with open(file) as f:
        return parsesimpleyaml(f.read())


def writeyaml(file: str, yaml: dict) -> None:
    with open(file, "w") as f:
        f.write("\n".join(": ".join(x) for x in zip(yaml.keys(), yaml.values())))


def updateyaml(file: str, update: dict) -> None:
    yaml = readparseyaml(file)
    yaml.update(update)
    writeyaml(file, yaml)


updateyaml(
    "data.yaml",
    {sys.argv[1]: str(int(readparseyaml("data.yaml")[sys.argv[1]]) + int(sys.argv[2]))},
)
