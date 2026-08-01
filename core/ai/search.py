"""
=========================================
Project : NeelX
Module  : Search
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import webbrowser


class Search:

    @staticmethod
    def google(query: str):

        query = query.replace("search", "").strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching {query}"