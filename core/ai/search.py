"""
=========================================
Project : NeelX
Module  : Search
Author  : Nilesh Vishwakarma
Version : 1.2.0
=========================================
"""

import webbrowser
from urllib.parse import quote_plus

from core.ai.search_router import SearchRouter
from android.app_manager import AppManager


class Search:

    @staticmethod
    def google(query: str):

        query = Search._clean_query(query)

        if not query:
            return "What should I search for?"

        url = f"https://www.google.com/search?q={quote_plus(query)}"

        webbrowser.open(url)

        print(f"🌐 Google Search: {query}")

        return f"Searching {query} on Google"

    @staticmethod
    def youtube(query: str):

        query = Search._clean_query(query)

        if not query:
            return "What should I search for?"

        AppManager.search_youtube(query)

        return f"Searching {query} on YouTube"

    @staticmethod
    def chrome(query: str):

        return Search.google(query)

    @staticmethod
    def search(text: str):

        target = SearchRouter.route(text)

        query = Search._clean_query(text)

        if target == "youtube":
            return Search.youtube(query)

        if target == "chrome":
            return Search.chrome(query)

        return Search.google(query)

    @staticmethod
    def _clean_query(text: str):

        query = text.lower().strip()

        prefixes = [
            "search",
            "google",
            "find"
        ]

        for prefix in prefixes:

            if query.startswith(prefix):
                query = query[len(prefix):].strip()
                break

        suffixes = [
            " on youtube",
            " on google",
            " on chrome"
        ]

        for suffix in suffixes:

            if query.endswith(suffix):
                query = query[:-len(suffix)].strip()
                break

        return query
