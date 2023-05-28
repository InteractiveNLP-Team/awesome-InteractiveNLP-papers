from typing import List

import pandas as pd
import pnlp


class Formater:

    base = "https://img.shields.io/badge/"

    @classmethod
    def abbr_format(cls, abbr):
        return f"{cls.base}-{abbr}-blue"

    @classmethod
    def method_format(cls, method):
        return f"{cls.base}-{method}-orange"

    @classmethod
    def interface_format(cls, interface):
        return f"{cls.base}-{interface}-lightgrey"

    @classmethod
    def misc_format(cls, misc):
        return f"{cls.base}{misc}-green"


def trans(s: str) -> str:
    return s.replace(" ", "%20")


def df2md(df: pd.DataFrame) -> List[str]:
    data = []
    needs = ["abbr", "method", "interface", "misc"]
    for v in df.itertuples():
        line = f"- **[{v.title}]({v.url})**, {v.date} "
        badges = []
        for col in needs:
            val = getattr(v, col)
            if pd.isna(val):
                continue
            func = getattr(Formater, col + "_format")
            val = trans(val)
            val_format = func(val)
            badges.append(f"![img]({val_format})")
        line += " ".join(badges)
        line += "\n\n"
        line += f"  *{v.author}*."
        data.append(line + "\n")
    return data


def main():
    cols = [
        "title",
        "url",
        "date",
        "abbr",
        "method",
        "interface",
        "misc",
        "author"]
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Transfer pandas excel to markdown needed")
    parser.add_argument("-i", "--input_file", default=None,
                        help=f"Input excel file with {cols} columns, without header")
    args = parser.parse_args()

    if not args.input_file:
        print("An input_file is needed, run `-h` to get more info")

    out_file = Path(args.input_file).stem

    df = pd.read_excel(
        args.input_file,
        header=None,
        names=cols)
    data = df2md(df)
    pnlp.write_file(out_file + ".md", data)


if __name__ == "__main__":
    main()
