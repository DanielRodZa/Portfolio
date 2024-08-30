from duckduckgo_search import DDGS


class DuckSearch:
    def search(self, query, max_results=10):
        final_result = []
        results = DDGS().text(keywords=query, max_results=max_results)
        cresults = self.custom_result(results)
        final_result.extend(cresults)
        return final_result

    def custom_result(self, results):
        custom_result = []
        for r in results:
            cresults = {}
            cresults['title'] = r['title']
            cresults['href'] = r['href']
            cresults['description'] = r['body']
            custom_result.append(cresults)
        return custom_result
