#!/usr/bin/env python3

import argparse
import json
from libs.search_func import search_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    with open("data/movies.json", "r", encoding="utf-8") as f:
        data = json.load(f) 

    match args.command:
        case "search":
            print(f'Searching for: {args.query}')
            results = search_command(data, args.query)
            # print(results)
            for i in range(len(results)):
                print(f"{i+1}. {results[i]['title']}")

            # More optimized one

            # results = [m for m in data["movies"] if args.query in m["title"]]
            # results.sort(key=lambda m: m["id"])
            # for i, movie in enumerate(results[:5], start=1):
            #     print(f"{i}. {movie['title']}")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()