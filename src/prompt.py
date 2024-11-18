PROMPT = """
Generate a valid SQL query for the following natural language instruction:

Query: ${query}

Only generate SQL code and nothing else. name the columns.  Do not include formatting or string escaping.
${gr.complete_json_suffix_v3}
"""
